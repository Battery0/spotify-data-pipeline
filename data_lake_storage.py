from google.cloud import storage
from get_spotify_artist_tracks import artist_albums


def upload_to_gcs_data_lake(bucket_name, contents_to_upload, data_type, destination_blob_name):
    storage_client = storage.Client(project="focal-cipher-432312-h8")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(data=contents_to_upload, content_type=data_type)


upload_to_gcs_data_lake(
    bucket_name="spotify-artist-data",
    contents_to_upload=str(artist_albums("6kBDZFXuLrZgHnvmPu9NsG")),
    data_type="json",
    destination_blob_name="spotify-artist-complete-album-data")
