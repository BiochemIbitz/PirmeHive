// Netlify serverless function for Django
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

// Helper function to normalize paths for different OS
function normalizePath(p) {
  return path.normalize(p).replace(/\\/g, '/');
}

exports.handler = async function(event, context) {
  // Set environment variables
  process.env.DJANGO_SETTINGS_MODULE = 'primehive.settings_prod';
  
  // Create a temporary file for the request body
  const tmpPath = path.join('/tmp', `django-request-${Date.now()}`);
  
  // Write request body to the temporary file if it exists
  if (event.body) {
    fs.writeFileSync(tmpPath, event.body);
  } else {
    fs.writeFileSync(tmpPath, '');
  }
  
  // Prepare the Django management command
  const args = [
    'manage.py',
    'runserver',
    '--noreload',
    '--insecure',
    '127.0.0.1:8000'
  ];
  
  // Create environment for the Django process
  const env = {
    ...process.env,
    PATH_INFO: event.path,
    QUERY_STRING: new URLSearchParams(event.queryStringParameters || {}).toString(),
    REQUEST_METHOD: event.httpMethod,
    SERVER_NAME: event.headers.host,
    SERVER_PORT: '443',
    HTTP_HOST: event.headers.host,
    HTTPS: 'on',
    CONTENT_LENGTH: event.body ? Buffer.byteLength(event.body) : 0,
    CONTENT_TYPE: event.headers['content-type'] || '',
    HTTP_COOKIE: event.headers.cookie || '',
    HTTP_ACCEPT: event.headers.accept || '',
    HTTP_USER_AGENT: event.headers['user-agent'] || '',
    HTTP_REFERER: event.headers.referer || '',
    REMOTE_ADDR: event.headers['client-ip'] || '',
    REQUEST_URI: event.path + (event.queryStringParameters ? `?${new URLSearchParams(event.queryStringParameters).toString()}` : ''),
    DJANGO_SETTINGS_MODULE: 'primehive.settings_prod',
  };
  
  // Spawn the Django process
  const django = spawn('python', args, { env });
  
  // Collect response data
  let responseData = '';
  let errorData = '';
  
  django.stdout.on('data', (data) => {
    responseData += data.toString();
  });
  
  django.stderr.on('data', (data) => {
    errorData += data.toString();
  });
  
  // Return a Promise that resolves when the Django process exits
  return new Promise((resolve, reject) => {
    django.on('close', (code) => {
      // Clean up the temporary file
      try {
        fs.unlinkSync(tmpPath);
      } catch (err) {
        console.error('Error cleaning up temporary file:', err);
      }
      
      if (code === 0) {
        // Parse the response
        const responseLines = responseData.split('\n');
        const statusLine = responseLines[0];
        const statusMatch = statusLine.match(/(\d{3})/);
        const statusCode = statusMatch ? parseInt(statusMatch[1]) : 200;
        
        // Extract headers
        const headers = {};
        let i = 1;
        while (i < responseLines.length && responseLines[i].trim() !== '') {
          const [key, value] = responseLines[i].split(': ');
          headers[key.toLowerCase()] = value;
          i++;
        }
        
        // Extract body
        const body = responseLines.slice(i + 1).join('\n');
        
        resolve({
          statusCode,
          headers,
          body
        });
      } else {
        // Return error response
        console.error('Django process exited with code:', code);
        console.error('Error output:', errorData);
        
        resolve({
          statusCode: 500,
          body: JSON.stringify({
            error: 'Internal Server Error',
            details: errorData
          })
        });
      }
    });
  });
};
