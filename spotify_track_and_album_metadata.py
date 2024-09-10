import requests


def spotify_track_and_album_metadata(spotify_auth_json, grouped_track_ids):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    track_and_album_metadata = []

    for set_of_track_ids in grouped_track_ids:
        joined_track_ids = ",".join(set_of_track_ids)
        params = {"ids": f"{joined_track_ids}"}
        url_endpoint = "https://api.spotify.com/v1/tracks"

        response_json = requests.get(url=url_endpoint, headers=headers, params=params).json()
        track_and_album_metadata.append(response_json)

    return track_and_album_metadata



    # extraction of required metadata



def extract_album_and_track_metadata(album_and_track_metadata):


