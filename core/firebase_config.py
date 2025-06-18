import os
import json
import firebase_admin
from firebase_admin import credentials, auth
from django.conf import settings
from pathlib import Path

# Firebase Web App Configuration
FIREBASE_CONFIG = {
    "apiKey": "AIzaSyD1z25MWrimY5Mfj2nHvoj3yTMgkSZMj68",
    "authDomain": "primehive-a6e2c.firebaseapp.com",
    "projectId": "primehive-a6e2c",
    "storageBucket": "primehive-a6e2c.firebasestorage.app",
    "messagingSenderId": "799270848700",
    "appId": "1:799270848700:web:cffa5316a9343d9388a8b9",
    "measurementId": "G-9ZG5Z01G5Q",
    "databaseURL": "https://primehive-a6e2c.firebaseio.com"
}

def get_credentials():
    try:
        # First try to load from environment variable
        if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
            return credentials.ApplicationDefault()
        
        # Then try to load from service account file
        cred_path = os.path.join(settings.BASE_DIR, "primehive-a6e2c-firebase-adminsdk-fbsvc-9e726226c9.json")
        if os.path.exists(cred_path):
            return credentials.Certificate(cred_path)
        
        raise FileNotFoundError("Firebase credentials file not found")
    except Exception as e:
        print(f"Error loading credentials: {str(e)}")
        return None

def initialize_firebase():
    try:
        if not firebase_admin._apps:
            cred = get_credentials()
            if cred:
                firebase_admin.initialize_app(cred, {
                    'databaseURL': 'https://primehive-a6e2c.firebaseio.com'
                })
                print("Firebase initialized successfully")
                return True
            else:
                print("Failed to load Firebase credentials")
                return False
        return True
    except Exception as e:
        print(f"Firebase initialization error: {str(e)}")
        return False

# Initialize Firebase when module is loaded
if not initialize_firebase():
    print("Warning: Firebase initialization failed. Some features may not work.")

def verify_firebase_token(id_token):
    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Token verification error: {str(e)}")
        return None

def get_user_info(uid):
    try:
        # Get user info from Firebase
        user = auth.get_user(uid)
        return user
    except Exception as e:
        print(f"Error getting user info: {str(e)}")
        return None