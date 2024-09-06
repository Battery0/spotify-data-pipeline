import pandas as pd


def data_transform(flattened_track_data):
    df = pd.DataFrame(flattened_track_data)

    return transform_data_types(df)


def transform_data_types(df):
    data_type_casting = df.astype({
       "upc_num": "int64",
       "label_name": "string",
       "album_type": "string",
       "album_release_date": "datetime64[ns]",
       "album_name": "string",
       "track_title": "string",
       "artist_name": "string"
    })

    return data_type_casting


# flat_track = [
#     {
#         "upc_num": "5056321616197",
#         "label_name": "Hidden Art Recordings",
#         "album_type": "compilation",
#         "album_release_date": "2002-10-04",
#         "album_name": "The Fire This Time",
#         "track_title": "Say Hello To Allah - \"Come To Daddy\" RE-MIXED by Black Lung",
#         "artist_name": [
#             "Aphex Twin",
#             "Black Lung"
#         ]
#     },
#     {
#         "upc_num": "5056321616197",
#         "label_name": "Hidden Art Recordings",
#         "album_type": "compilation",
#         "album_release_date": "2002-10-04",
#         "album_name": "The Fire This Time",
#         "track_title": "Come To Daddy - RE-MIXED by Black Lung",
#         "artist_name": [
#             "Aphex Twin",
#             "Black Lung"
#         ]
#     }
# ]
#
# data_transform(flat_track)
