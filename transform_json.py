def flatten_json(detailed_album_info, artist_id):
    flattened_track_info = []

    for albums in detailed_album_info:  # list - of 54 albums - looping over every album
        album_tracks = albums["albums"][0]["tracks"]["items"]
        for track in album_tracks:
            if artist_id_check(track, artist_id): flattened_track_info.append({"name": f"{track['name']}"})


def artist_id_check(track, artist_id):
    for artist in track["artists"]:
        if artist["id"] == artist_id: return True
