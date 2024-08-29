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
            timeout=10)

        response_json.raise_for_status()
    except requests.exceptions.ConnectTimeout as e:
        print(f"The Post request took too long to connect to the Spotify authentication server:\n  {e}")
        raise TimeoutError
    except requests.exceptions.ReadTimeout as e:
        print(f"The Spotify authentication server didn't send any data in the allotted time:\n  {e}")
        raise TimeoutError
    except requests.HTTPError as e:
        print(f"Error with HTTP request:\n  {e}")
        raise requests.HTTPError
    else:
        return response_json.json()
