import sys
import requests
from requests.exceptions import ConnectTimeout, ReadTimeout, ConnectionError
import dotenv
import base64
from os import getenv
import time


def spotify_auth():
    dotenv.load_dotenv()
    encoded_client_credentials = base64.b64encode(bytes(f"{getenv('CLIENT_ID')}:{getenv('CLIENT_SECRET')}",
                                                        "utf-8")).decode("utf-8")
    auth_endpoint = "https://accounts.spotify.com/api/token"
    request_headers = {"Content-Type": "application/x-www-form-urlencoded",
                       "Authorization": f"Basic {encoded_client_credentials}"}
    request_body = {"grant_type": "client_credentials"}
    max_tries = 3
    retry_connection_seconds = 10

    for attempt in range(max_tries):
        try:
            response_json = requests.post(
                url=auth_endpoint,
                data=request_body,
                headers=request_headers,
                timeout=10)

            response_json.raise_for_status()
        except (ConnectTimeout, ReadTimeout, ConnectionError) as e:
            print(f"Connection error. Attempt {attempt + 1} of {max_tries}. "
                  f"Retrying authentication in {retry_connection_seconds} seconds")
            if attempt < max_tries - 1:
                time.sleep(retry_connection_seconds)
                continue
            else:
                print(f"Max retries ({max_tries}) occured. Error:\n  {e}")
                sys.exit("Failed to authenticate with Spotify")
        except requests.HTTPError as e:
            print(f"Error with HTTP request:\n  {e}")
            sys.exit("Error with HTTP status code")
        else:
            return response_json.json()
