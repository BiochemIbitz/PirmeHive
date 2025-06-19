// Netlify serverless function for Django
exports.handler = async function(event, context) {
  // This is a simplified serverless function that returns a static HTML page
  // Since running Django directly in serverless functions is challenging
  
  // Set up headers for the response
  const headers = {
    'Content-Type': 'text/html',
    'Cache-Control': 'no-cache',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'strict-origin-when-cross-origin'
  };
  
  // Create a simple HTML response
  const html = `
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PrimeHive - Deployment Status</title>
    <style>
      body {
        font-family: 'Poppins', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        color: #333;
        background-color: #f8f9fa;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
      }
      .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        text-align: center;
      }
      h1 {
        color: #2c3e50;
        margin-bottom: 1rem;
      }
      .card {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      }
      .status {
        font-size: 1.2rem;
        margin-bottom: 1rem;
      }
      .next-steps {
        background-color: #f1f8ff;
        border-left: 4px solid #3498db;
        padding: 1rem;
        text-align: left;
        margin-top: 2rem;
      }
      .btn {
        display: inline-block;
        background-color: #3498db;
        color: white;
        padding: 0.5rem 1rem;
        text-decoration: none;
        border-radius: 5px;
        margin-top: 1rem;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="card">
        <h1>PrimeHive Deployment Status</h1>
        <div class="status">
          <p>Your Django application is partially deployed to Netlify.</p>
          <p>The static files have been successfully deployed, but the dynamic functionality requires additional configuration.</p>
        </div>
        <div class="next-steps">
          <h3>Next Steps:</h3>
          <ol>
            <li>Configure a production database (PostgreSQL recommended)</li>
            <li>Set up environment variables in Netlify dashboard</li>
            <li>Consider using a different hosting platform for Django applications, such as:
              <ul>
                <li>Heroku</li>
                <li>PythonAnywhere</li>
                <li>DigitalOcean App Platform</li>
                <li>AWS Elastic Beanstalk</li>
              </ul>
            </li>
          </ol>
        </div>
        <p>For more information, see the <a href="https://docs.netlify.com/" class="btn">Netlify Documentation</a></p>
      </div>
    </div>
  </body>
  </html>
  `;
  
  return {
    statusCode: 200,
    headers: headers,
    body: html
  };
};
