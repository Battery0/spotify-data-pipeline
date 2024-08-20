import requests
from spotify_auth import spotify_auth


def spotify_album_data(spotify_auth_json, artist_id, group_type):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    print(bearer_token)
    album_data = []

    for album_type in group_type:
        album_type_endpoint = \
            f"https://api.spotify.com/v1/artists/{artist_id}/albums?&limit=50&include_groups={album_type}&market=GB"

        response_json = requests.get(url=album_type_endpoint, headers=headers).json()

        if response_json["next"] is None:
            album_data.append(response_json)
        else:
            album_data.append(response_json)
            while response_json["next"] is not None:
                next_call = response_json["next"]
                response_json = requests.get(url=next_call, headers=headers).json()
                album_data.append(response_json)

    return album_data


def extract_album_id(album_data):
    album_id = {}

    for album_type in album_data:
        for album in album_type["items"]:
            album_id[f"{album['name']}"] = album["id"]

    chunk_ids = chunk_album_ids(album_id)

    return chunk_ids


def chunk_album_ids(album_id):
    split_ids = []

    for num in range(0, len(album_id), 20):
        set_of_twenty_id = list(album_id.values())[num:num+20]
        split_ids.append(set_of_twenty_id)

    return split_ids


def spotify_detailed_album_info(spotify_auth_json, album_ids):
    bearer_token = spotify_auth_json["access_token"]
    print(bearer_token)
    headers = {"Authorization": f"Bearer {bearer_token}"}
    detailed_album_data = []

    url_endpoint = f"https://api.spotify.com/v1/albums"
