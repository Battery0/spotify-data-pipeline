import requests
from spotify_auth import spotify_auth
import pprint

def get_spotify_artist_tracks(artist_id, market):
    get_albums_endpoint = f"https://api.spotify.com/v1/artists/{artist_id}/albums?market={market}&limit=50"
    bearer_token = spotify_auth()["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}

    artist_albums = []
    response_json = requests.get(url=get_albums_endpoint, headers=headers).json()

    if response_json["next"] is None:
        return response_json
    else:
        artist_albums.append(response_json)
        while response_json["next"] is not None:
            print(headers)
            next_api_endpoint = response_json["next"]
            response_json = requests.get(url=next_api_endpoint, headers=headers).json()
            artist_albums.append(response_json)

    print(len(artist_albums))
    return artist_albums



aphex_twin_id = "6kBDZFXuLrZgHnvmPu9NsG"
peter_bruntnell = "6qQpSCDIS4V5Md1sfgaCkh"
pprint.pp(get_spotify_artist_tracks(aphex_twin_id, "GB"))

# print(get_spotify_artist_tracks(aphex_twin_id, "GB")["next"])
# print(get_spotify_artist_tracks(aphex_twin_id, "GB").keys())
# print(get_spotify_artist_tracks(aphex_twin_id, "GB")["total"])
