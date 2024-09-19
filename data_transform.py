import pandas as pd


def data_transform(flattened_track_data):
    df = pd.DataFrame(flattened_track_data)

    data_type_casting = df.astype(
        {
            "track_isrc_number": "string",
            "track_title": "string",
            "track_artists": "string",
            "album_title": "string",
            "album_release_date": "datetime64[ns]",
            "album_type": "string",
            "album_label": "string",
            "album_upc": "int64",
        }
    )

    return data_type_casting
