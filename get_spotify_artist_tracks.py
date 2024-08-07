import requests
from spotify_auth import spotify_auth


def get_spotify_artist_tracks(artist_id, market):
    get_albums_endpoint = f"https://api.spotify.com/v1/artists/{artist_id}/albums?market={market}"
    headers = {"Authorization": f"Bearer {spotify_auth()['access_token']}"}

    response_json = requests.get(url=get_albums_endpoint, headers=headers).json()
    return response_json


aphex_twin_id = "6kBDZFXuLrZgHnvmPu9NsG"
print(get_spotify_artist_tracks(aphex_twin_id, "GB"))
