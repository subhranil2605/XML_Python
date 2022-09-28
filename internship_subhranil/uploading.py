# s3 bucket connection
import boto
import boto.s3.connection
from io import StringIO
import boto3
import pandas as pd
import os
from pathlib import Path

ACCESS_KEY = 'ACESS_KEY'
SECRETY_KEY = 'SECRET_KEY'
BUCKET_NAME = 'extracted_csv_files'


def create_bucket() -> None:
    """
    Creating bucket
    :return: None
    """

    # connection
    conn = boto.connect_s3(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRETY_KEY)
    # creating bucket
    conn.create_bucket(BUCKET_NAME)


def upload(filename) -> None:
    """
    upload the csv file
    :param filename: csv filename
    :return: None
    """

    # save as a dataframe
    hc = pd.read_csv(filename)

    # creating connection with boto3
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRETY_KEY)

    csv_buf = StringIO()
    hc.to_csv(csv_buf, header=True, index=False)
    csv_buf.seek(0)

    # upload the data in the bucket
    s3.put_object(Bucket=BUCKET_NAME, Body=csv_buf.getvalue(), Key=filename)


if __name__ == "__main__":
    path = Path(os.path.join(os.getcwd(), "files/extracted_csvs"))
    csv_files = (file for file in path.iterdir() if file.suffix == '.csv')
    [upload(csv_file) for csv_file in csv_files]
