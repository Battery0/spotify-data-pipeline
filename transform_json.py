import pandas as pd
from get_spotify_artist_tracks import spotify_album_data


def json_to_flattened_csv(json_data):
    df = pd.json_normalize(json_data,
                           record_path=["items", "artists"],
                           meta=[["items", "album_group"]])
    df.rename(columns={"items.album_group": "album_group"}, inplace=True)

    df.to_clipboard()
    print(df)


json_to_flattened_csv(
    spotify_album_data("6kBDZFXuLrZgHnvmPu9NsG",
                       ["album", "single", "appears_on", "compilation"]
                       )
)
