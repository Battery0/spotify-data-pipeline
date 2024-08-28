import requests
import dotenv
from os import getenv


def spotify_auth():
    dotenv.load_dotenv()
    auth_endpoint = "https://accounts.spotify.com/api/token"
    request_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_body = {"client_id": getenv("CLIENT_ID"),
                    "client_secret": getenv("CLIENT_SECRET"),
                    "grant_type": "client_credentials"}

    try:
        response_json = requests.post(
            url=auth_endpoint,
            data=request_body,
            headers=request_headers,
            timeout=0.000000001)
    except requests.exceptions.ConnectTimeout:
        raise TimeoutError("The Post request took too long to connect to the Spotify authentication server")
    except requests.exceptions.ReadTimeout:
        raise TimeoutError("The Spotify authentication server didn't send any data in the allotted time")

    return response_json.json()
