from big_query import upload_to_big_query
from data_lake_storage import upload_to_data_lake
from data_transform import data_transform
from spotify_artist_albums import spotify_album_data, extract_album_id, spotify_detailed_album_info
from spotify_auth import spotify_auth
from transform_json import get_flat_track_data


def main():
    artist_id = "6kBDZFXuLrZgHnvmPu9NsG"

    spotify_auth_json = spotify_auth()

    album_data = spotify_album_data(
        spotify_auth_json=spotify_auth_json,
        artist_id="6kBDZFXuLrZgHnvmPu9NsG",
        group_type=["album", "single", "appears_on", "compilation"]
    )

    album_ids = extract_album_id(album_data)

    detailed_albums_data = spotify_detailed_album_info(
        spotify_auth_json=spotify_auth_json,
        album_ids=album_ids)

    upload_to_data_lake(
        bucket_name="spotify-artist-data",
        contents_to_upload={
            "artist_album_data": album_data,
            "artist_detailed_album_info": detailed_albums_data
        },
        data_type="json",
    )

    flattened_track_data = get_flat_track_data(
        albums_data=detailed_albums_data,
        artist_id=artist_id
    )

    data_transformed_for_big_query = data_transform(flattened_track_data)

    upload_to_big_query(data_transformed_for_big_query)


if __name__ == '__main__':
    main()
