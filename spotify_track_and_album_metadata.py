import requests


def spotify_track_and_album_metadata(spotify_auth_json, grouped_artist_track_ids):
    bearer_token = spotify_auth_json["access_token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    track_and_album_metadata = []

    for set_of_track_ids in grouped_artist_track_ids:
        joined_track_ids = ",".join(set_of_track_ids)
        params = {"ids": f"{joined_track_ids}"}
        url_endpoint = "https://api.spotify.com/v1/tracks"

        response_json = requests.get(url=url_endpoint, headers=headers, params=params).json()
        track_and_album_metadata.append(response_json)

    return track_and_album_metadata


def extract_album_and_track_metadata(album_and_track_metadata, detailed_album_metadata):
    extracted_track_and_album_metadata = []

    for set_of_tracks in album_and_track_metadata:
        for top_level_metadata in set_of_tracks["tracks"]:
            album_id = top_level_metadata["album"]["id"]
            track_metadata = extract_track_metadata(top_level_metadata)
            album_metadata = extract_album_metadata(top_level_metadata, detailed_album_metadata, album_id)

            combined_track_album_metadata = track_metadata | album_metadata
            extracted_track_and_album_metadata.append(combined_track_album_metadata)

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


def extract_album_metadata(top_level_metadata, detailed_album_metadata, album_id):
    label_and_upc = extract_label_and_upc(detailed_album_metadata, album_id)

    album_metadata = {
        "album_title": f"{top_level_metadata['album']['name']}",
        "album_release_date": f"{top_level_metadata['album']['release_date']}",
        "album_type": f"{top_level_metadata['album']['type']}",
        "album_label": f"{label_and_upc[0]}",
        "album_upc": f"{label_and_upc[1]}"
    }

    return album_metadata


def extract_label_and_upc(detailed_album_metadata, album_id):
    label_and_upc = []

    for set_of_albums in detailed_album_metadata:
        for album in set_of_albums["albums"]:
            if album['id'] == album_id:
                album_label = f"{album['label']}"
                album_upc = f"{album['external_ids']['upc']}"
                label_and_upc.extend([album_label, album_upc])

    return label_and_upc
