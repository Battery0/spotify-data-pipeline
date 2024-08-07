import requests
import dotenv
import os


def spotify_auth():
    dotenv.load_dotenv()
    auth_endpoint = "https://accounts.spotify.com/api/token"
    request_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_body = {"client_id": os.getenv("CLIENT_ID"),
                    "client_secret": os.getenv("CLIENT_SECRET"),
                    "grant_type": "client_credentials"}

    response_json = requests.post(url=auth_endpoint, data=request_body, headers=request_headers).json()
    return response_json
