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





















# def extract_track_data(detailed_album_info, artist_id):
#     flattened_track_data = []
#
#     for album in detailed_album_info:
#         # setup vars for the levels of json you need so you can loop/extract data where required and pass them to helper functions
#         album_data = album["albums"][0]  # all albums level
#         track_data = album["albums"][0]["tracks"]["items"]  # track level for all albums
#
#         required_track_data = track_extract(current_track=track_data, artist_id=artist_id)
#
#
# def track_extract(current_track, artist_id):  # not working correctly at the moment - probably linked to artist_id_check
#     artists = []
#     is_artist_on_track = artist_id_check(current_track, artist_id)
#
#     if is_artist_on_track:
#         for track in current_track:
#             for artist in track["artists"]:
#                 artists.append(artist["name"])
#             # artists.append(track["name"])
#
#     print(artists)
#
#     return artists
#
#
# def artist_id_check(current_track, artist_id):
#
#     for track in current_track:
#         for artist in track["artists"]:
#             return artist["id"] == artist_id
#
#     #
#     # for artist in current_track["artists"]:  # loops through artists in a track & checks if ID is in ["artists"].OK!
#     #         return artist["id"] == artist_id
