def get_flat_track_data(albums_data, artist_id):
    artists_complete_track_ids= []

    for album in albums_data:
        # album_data = album["albums"][0]

        for track_data in album["albums"][0]["tracks"]["items"]:
            id_check = artist_id_check(track_data=track_data, artist_id=artist_id)
            if id_check:
                track_id = extract_track_id(track_data)
                # upc_num = extract_upc_num(album_data)
                # artist_names = extract_track_artist_names(track_data)
                # label_name = extract_label_name(album_data)
                # album_name = extract_album_name(album_data)
                # album_type = extract_album_type(album_data)
                # release_date = extract_album_release_date(album_data)
                artists_complete_track_ids.append(
                    track_id
                    # "upc_num": upc_num,
                    # "label_name": label_name,
                    # "album_type": album_type,
                    # "album_release_date": release_date,
                    # "album_name": album_name,
                    # "track_title": track_title,
                    # "artist_name": artist_names
                )
    print(artists_complete_track_ids)
    return artists_complete_track_ids


def artist_id_check(track_data, artist_id):
    artist_on_track = []
    for artist in track_data["artists"]:
        artist_on_track.append(artist["id"] == artist_id)
    is_artist_on_track = any(artist_on_track)
    return is_artist_on_track


def extract_track_id(track_data):
    return track_data["id"]


# def extract_track_artist_names(track_data):
#     track_artists = []
#     for artist in track_data["artists"]:
#         track_artists.append(artist["name"])
#     return track_artists


# def extract_upc_num(album_data):
#     return album_data["external_ids"]["upc"]
#
#
# def extract_album_name(album_data):
#     return album_data["name"]


# def extract_upc_num(album_data):
#     return album_data["external_ids"]["upc"]
#
#
# def extract_track_title(track_data):
#     return track_data["name"]
#
#
# def extract_album_name(album_data):
#     return album_data["name"]
#
#
# def extract_label_name(album_data):
#     return album_data["label"]
#
#
# def extract_album_type(album_data):
#     return album_data["album_type"]
#
#
# def extract_album_release_date(album_data):
#     return album_data["release_date"]
