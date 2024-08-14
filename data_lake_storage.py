from google.cloud import storage


def upload_to_data_lake(bucket_name, contents_to_upload, data_type, destination_blob_name):
    storage_client = storage.Client(project="focal-cipher-432312-h8")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(data=contents_to_upload, content_type=data_type)
