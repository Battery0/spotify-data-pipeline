import requests


def detailed_spotify_album_metadata(spotify_auth_json, album_ids):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    detailed_album_data = []

    for twenty_album_ids in album_ids:
        for album_id in twenty_album_ids:
            url_endpoint = f"https://api.spotify.com/v1/albums?ids={album_id}"
            json_response = requests.get(url=url_endpoint, headers=headers).json()

            detailed_album_data.append(json_response)

    return detailed_album_data


def extract_track_ids(albums_data, artist_id):
    artists_complete_track_ids = []

    for album in albums_data:
        for track_data in album["albums"][0]["tracks"]["items"]:
            id_check = _artist_id_check(track_data=track_data, artist_id=artist_id)
            if id_check: artists_complete_track_ids.append(track_data["id"])

    print(artists_complete_track_ids)
    print(len(artists_complete_track_ids))
    return artists_complete_track_ids


def _artist_id_check(track_data, artist_id):
    artist_on_track = []

    for artist in track_data["artists"]:
        artist_on_track.append(artist["id"] == artist_id)

    is_artist_on_track = any(artist_on_track)
    return is_artist_on_track
