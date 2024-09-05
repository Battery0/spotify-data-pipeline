from google.cloud import bigquery
import pandas as pd


def upload_to_big_query(artist_album_data):
    # create client object to interact with BQ
    client = bigquery.Client()

    # Set table_id to the ID of the table to create.
    table_id = "focal-cipher-432312-h8.spotify_album_data.aphex_twin_album_data"

    # get the table schema
    schema = database_table_schema()

    df = pd.DataFrame(artist_album_data)

    # create job and make API request to load artist album data to BQ
    job_config = bigquery.LoadJobConfig(schema=schema, write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(dataframe=df, destination=table_id, job_config=job_config)
    job.result()  # Wait for the job to complete.

    # check table was created and print info
    table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows and {} columns to {}".format(table.num_rows, len(table.schema), table_id))


def database_table_schema():
    schema = [
        bigquery.SchemaField(name="upc_num", field_type="STRING", mode="REQUIRED",
                             description="Album unique UPC number"),
        bigquery.SchemaField(name="label_name", field_type="STRING", mode="REQUIRED",
                             description="Record label"),
        bigquery.SchemaField(name="album_type", field_type="STRING", mode="REQUIRED",
                             description="Type of album (album, single, compilation, appeared on)"),
        bigquery.SchemaField(name="album_release_date", field_type="DATE", mode="REQUIRED",
                             description="Date of album release"),
        bigquery.SchemaField(name="album_name", field_type="STRING", mode="REQUIRED",
                             description="Album name"),
        bigquery.SchemaField(name="track_title", field_type="STRING", mode="REQUIRED",
                             description="Track name"),
        bigquery.SchemaField(name="artist_name", field_type="STRING", mode="REQUIRED",
                             description="artists of track")
    ]

    return schema
