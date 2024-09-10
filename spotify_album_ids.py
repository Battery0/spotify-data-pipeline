import requests


def high_level_spotify_album_metadata(spotify_auth_json, artist_id, group_type):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    album_data = []

    for album_type in group_type:
        album_type_endpoint = \
            f"https://api.spotify.com/v1/artists/{artist_id}/albums?&limit=50&include_groups={album_type}&market=GB"
        response_json = requests.get(url=album_type_endpoint, headers=headers).json()

        if response_json["next"] is None:
            album_data.append(response_json)
        else:
            album_data.append(response_json)
            while response_json["next"] is not None and len(response_json["items"]) > 50:
                next_call = response_json["next"]
                response_json = requests.get(url=next_call, headers=headers).json()
                album_data.append(response_json)

    return album_data


def extract_album_ids(album_data):
    album_ids = {}

    for album_type in album_data:
        for album in album_type["items"]:
            album_ids[f"{album['name']}"] = album["id"]

    chunk_ids = _chunk_album_ids(album_ids)
    return chunk_ids


def _chunk_album_ids(album_id):
    split_ids = []

    for num in range(0, len(album_id), 20):
        twenty_album_ids = list(album_id.values())[num:num + 20]
        split_ids.append(twenty_album_ids)

    return split_ids
