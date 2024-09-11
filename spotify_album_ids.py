import requests
from grouping_ids import _grouped_ids


def high_level_spotify_album_metadata(spotify_auth_json, artist_id, group_type):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    high_level_album_metadata = []

    for album_type in group_type:
        album_type_endpoint = \
            f"https://api.spotify.com/v1/artists/{artist_id}/albums?&limit=50&include_groups={album_type}&market=GB"
        response_json = requests.get(url=album_type_endpoint, headers=headers).json()

        if response_json["next"] is None:
            high_level_album_metadata.append(response_json)
        else:
            high_level_album_metadata.append(response_json)
            while response_json["next"] is not None and len(response_json["items"]) > 50:
                next_call = response_json["next"]
                response_json = requests.get(url=next_call, headers=headers).json()
                high_level_album_metadata.append(response_json)

    return high_level_album_metadata


def extract_album_ids(high_level_album_metadata):
    album_ids = []

    for album_type in high_level_album_metadata:
        for album in album_type["items"]:
            album_ids.append(album["id"])

    grouped_album_ids = _grouped_ids(ids=album_ids, max_limit=20)
    return grouped_album_ids
