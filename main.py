from get_spotify_artist_tracks import spotify_album_data, extract_album_id
from data_lake_storage import upload_to_data_lake


def main():
    artist_id = "6kBDZFXuLrZgHnvmPu9NsG"

    album_data = spotify_album_data(
        artist_id="6kBDZFXuLrZgHnvmPu9NsG",
        group_type=["album", "single", "appears_on", "compilation"]
    )

    album_ids = extract_album_id(album_data)

    gcs = upload_to_data_lake(
        bucket_name="spotify-artist-data",
        contents_to_upload=str(album_data),
        data_type="json",
        destination_blob_name="spotify-artist-complete-album-data"
    )


if __name__ == '__main__':
    main()
