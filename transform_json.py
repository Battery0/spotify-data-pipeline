def get_flat_track_data(albums_data, artist_id):
    flattened_track_data = []

    for album in albums_data:
        for track_data in album["albums"][0]["tracks"]["items"]:
            id_check = artist_id_check(track_data=track_data, artist_id=artist_id)
            if id_check:
                artist_names = extract_track_artist_names(track_data)
                track_title = extract_track_title(track_data)

                # rest of data extraction calls go here
                flattened_track_data.append({
                    "artist_name": artist_names,
                    "track_title": track_title
                })

    # print(flattened_track_data)
    return flattened_track_data


def artist_id_check(track_data, artist_id):
    artist_on_track = []
    for artist in track_data["artists"]:
        artist_on_track.append(artist["id"] == artist_id)
    is_artist_on_track = any(artist_on_track)
    return is_artist_on_track


def extract_track_artist_names(track_data):
    track_artists = []
    for artist in track_data["artists"]:
        track_artists.append(artist["name"])
    return track_artists


def extract_track_title(track_data):
    return track_data["name"]
