#python module imports, notice the boto3 import

import logging
import boto3
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name

    if object_name is None:
        object_name = file_name

    # Create an S3 client first
    s3_client = boto3.client('s3')

    #now attempt to upload the file
    try:

        response = s3_client.upload_file(file_name, bucket, object_name)

    except ClientError as e:

        logging.error(e)

        return False

    return True


# test.txt is our sample file.  This file MUST BE in the same directory
# in which you are running this python code
# Invoke the upload_file function by calling it

upload_file('test.txt', 'inet4031-lab8bucket', 'test.txt')