from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from .firebase_config import verify_firebase_token, get_user_info
import json

@csrf_exempt
def handle_firebase_auth(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_token = data.get('idToken')
            
            # Verify the token
            decoded_token = verify_firebase_token(id_token)
            if not decoded_token:
                return JsonResponse({'error': 'Invalid token'}, status=400)
            
            # Get user info
            uid = decoded_token['uid']
            user_info = get_user_info(uid)
            
            if not user_info:
                return JsonResponse({'error': 'User not found'}, status=404)
            
            # Get or create Django user
            email = user_info.email or f"{uid}@primehive.com"
            user, created = User.objects.get_or_create(
                username=email,
                defaults={
                    'email': email,
                    'is_active': True
                }
            )
            
            # Log the user in
            login(request, user)
            
            return JsonResponse({
                'success': True,
                'user': {
                    'email': user.email,
                    'uid': uid
                }
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def sign_out(request):
    logout(request)
    messages.success(request, 'You have been signed out successfully.')
    return redirect('home')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'core/signup.html', {
        'firebase_config': json.dumps(settings.FIREBASE_CONFIG)
    })

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'core/signin.html', {
        'firebase_config': json.dumps(settings.FIREBASE_CONFIG)
    })
