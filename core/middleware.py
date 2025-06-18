from django.contrib.auth.models import User
from django.contrib.auth import login
from firebase_admin import auth
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.middleware import SessionMiddleware

class FirebaseAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        id_token = auth_header.split('Bearer ')[1]
        try:
            # Verify the ID token
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            email = decoded_token.get('email', '')
            
            # Get or create user
            user, created = User.objects.get_or_create(
                username=email,
                defaults={
                    'email': email,
                    'is_active': True
                }
            )
            
            # Update last login
            if not created:
                user.last_login = decoded_token.get('auth_time')
                user.save()

            # Log the user in
            login(request, user)
            
            # Add Firebase user info to request
            request.firebase_user = decoded_token
            
        except Exception as e:
            print(f"Firebase Auth Error: {str(e)}")
            return None
