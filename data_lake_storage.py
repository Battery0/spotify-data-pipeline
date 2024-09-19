from google.cloud import storage


def upload_metadata_to_gcs(bucket_name, contents_to_upload, data_type):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    for key, value in contents_to_upload.items():
        blob = bucket.blob(key)
        blob.upload_from_string(data=str(value), content_type=data_type)

        print(f"{key} uploaded to data lake bucket: {bucket_name}.")
