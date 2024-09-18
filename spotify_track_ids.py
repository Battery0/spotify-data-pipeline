import requests
from grouping_ids import _grouped_ids


def detailed_spotify_album_metadata(spotify_auth_json, grouped_album_ids):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    detailed_album_metadata = []

    for set_of_album_ids in grouped_album_ids:
        joined_album_ids = ",".join(set_of_album_ids)
        params = {"ids": f"{joined_album_ids}"}
        url_endpoint = f"https://api.spotify.com/v1/albums"

        json_response = requests.get(url=url_endpoint, headers=headers, params=params).json()
        detailed_album_metadata.append(json_response)

    return detailed_album_metadata


def extract_artist_track_ids(detailed_albums_metadata, artist_id):
    artist_track_ids = []

    for set_of_albums in detailed_albums_metadata:
        for album in set_of_albums["albums"]:
            for track in album["tracks"]["items"]:
                id_check = _artist_id_check(track_metadata=track, artist_id=artist_id)
                if id_check: artist_track_ids.append(track["id"])

    grouped_artist_track_ids = _grouped_ids(ids=artist_track_ids, max_limit=50)
    return grouped_artist_track_ids


def _artist_id_check(track_metadata, artist_id):
    artist_on_track = []

    for artist in track_metadata["artists"]:
        artist_on_track.append(artist["id"] == artist_id)

    is_artist_on_track = any(artist_on_track)
    return is_artist_on_track
