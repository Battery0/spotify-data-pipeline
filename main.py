from big_query import upload_metadata_to_big_query, database_table_schema
from data_lake_storage import upload_metadata_to_gcs
from data_transform import data_transform
from spotify_album_ids import high_level_spotify_album_metadata, extract_album_ids
from spotify_auth import spotify_auth
from spotify_track_and_album_metadata import spotify_track_and_album_metadata, extract_album_and_track_metadata
from spotify_track_ids import detailed_spotify_album_metadata, extract_artist_track_ids


def main():
    artist_id = "6kBDZFXuLrZgHnvmPu9NsG"

    spotify_auth_json = spotify_auth()

    high_level_album_metadata = high_level_spotify_album_metadata(
        spotify_auth_json=spotify_auth_json,
        artist_id=artist_id,
        group_type=["album", "single", "appears_on", "compilation"]
    )

    grouped_album_ids = extract_album_ids(high_level_album_metadata)

    detailed_album_metadata = detailed_spotify_album_metadata(
        spotify_auth_json=spotify_auth_json,
        grouped_album_ids=grouped_album_ids
    )

    grouped_artist_track_ids = extract_artist_track_ids(
        detailed_albums_metadata=detailed_album_metadata,
        artist_id=artist_id
    )

    album_and_track_metadata = spotify_track_and_album_metadata(spotify_auth_json, grouped_artist_track_ids)

    upload_metadata_to_gcs(
        bucket_name="spotify-artist-data",
        contents_to_upload={
            "artist_high_level_album_metadata": high_level_album_metadata,
            "artist_detailed_album_metadata": detailed_album_metadata,
            "artist_track_and_album_metadata": album_and_track_metadata
        },
        data_type="json"
    )

    extracted_flattened_metadata = extract_album_and_track_metadata(
        album_and_track_metadata=album_and_track_metadata,
        detailed_album_metadata=detailed_album_metadata)

    metadata_transformed_for_big_query = data_transform(flattened_track_data=extracted_flattened_metadata)

    upload_metadata_to_big_query(
        data_transformed_for_big_query=metadata_transformed_for_big_query,
        table_id="focal-cipher-432312-h8.spotify_album_data.aphex_twin_album_data",
        table_schema=database_table_schema()
    )


if __name__ == "__main__":
    main()
