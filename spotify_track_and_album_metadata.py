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


def extract_album_and_track_metadata(album_and_track_metadata):
    extracted_track_and_album_metadata = []

    for track_subset in album_and_track_metadata:
        for top_level_metadata in track_subset["tracks"]:
            track_metadata = extract_track_metadata(top_level_metadata)

            extracted_track_and_album_metadata.append(track_metadata)

    print(extracted_track_and_album_metadata)
    return extracted_track_and_album_metadata


def extract_track_metadata(top_level_metadata):
    track_metadata = {
        "track_isrc_number": f"{top_level_metadata['external_ids']['isrc']}",
        "track_title": f"{top_level_metadata['name']}",
        "track_artists": f"{extract_track_artists(top_level_metadata)}"
    }

    return track_metadata


def extract_track_artists(top_level_meta_data):
    track_artists = []

    if len(top_level_meta_data["artists"]) == 1:
        single_artist = top_level_meta_data["artists"][0]["name"]
        return single_artist
    else:
        for artists in top_level_meta_data["artists"]:
            track_artists.append(artists["name"])

    multiple_artists = ", ".join(track_artists)
    return multiple_artists





