from big_query import upload_to_big_query
from data_lake_storage import upload_to_data_lake
from data_transform import data_transform
from spotify_album_ids import high_level_spotify_album_metadata, extract_album_ids
from spotify_auth import spotify_auth
from spotify_track_ids import detailed_spotify_album_metadata, extract_track_ids


def main():
    artist_id = "6kBDZFXuLrZgHnvmPu9NsG"

    spotify_auth_json = spotify_auth()

    high_level_album_metadata = high_level_spotify_album_metadata(
        spotify_auth_json=spotify_auth_json,
        artist_id=artist_id,
        group_type=["album", "single", "appears_on", "compilation"]
    )

    album_ids = extract_album_ids(high_level_album_metadata)

    detailed_album_metadata = detailed_spotify_album_metadata(
        spotify_auth_json=spotify_auth_json,
        album_ids=album_ids
    )

    track_ids = extract_track_ids(
        albums_data=detailed_album_metadata,
        artist_id=artist_id
    )




    # # ***** Add call to tracks to upload to GCS *****
    # upload_to_data_lake(
    #     bucket_name="spotify-artist-data",
    #     contents_to_upload={
    #         "artist_album_data": album_data,
    #         "artist_detailed_album_info": detailed_albums_data # this needs removing and updating with detailed track metadata
    #     },
    #     data_type="json",
    # )




    # data_transformed_for_big_query = data_transform(flattened_track_data)
    #
    # upload_to_big_query(data_transformed_for_big_query)


if __name__ == '__main__':
    main()
