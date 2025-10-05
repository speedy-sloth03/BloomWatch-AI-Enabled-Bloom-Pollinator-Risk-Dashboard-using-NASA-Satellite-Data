from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
import os

router = APIRouter()
oauth = OAuth()

oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID', ''),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET', ''),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@router.post("/login", tags=["Auth"])
async def login(request: Request):
    redirect_uri = os.getenv('OAUTH_REDIRECT_URI', 'http://localhost:8000/auth/callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/auth/callback", tags=["Auth"])
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    # Set session, issue cookie (for demo, return user info)
    return {"email": user['email'], "name": user['name']}