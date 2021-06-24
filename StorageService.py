from minio import Minio
from config import *


client = Minio(

    endpoint=minio_host,
    access_key=minio_access_key,
    secret_key=minio_secret_key,
    secure=False
)


def upload_file(file, bucket, dir_path):

    found = client.bucket_exists(bucket)
    if not found:
        client.make_bucket(bucket)
    else:
        print('bucket already exists')
    client.fput_object(bucket, dir_path + '/' + file.filename,
                       file_path=file_upload_path + '/' + file.filename),
    print(
        'the file was uploaded onto bucket:{0}'.format(bucket)
    )


def list_buckets():
    buckets = client.list_buckets()
    return buckets


def list_files(bucket_name):
    files = client.list_objects(bucket_name=bucket_name, prefix='/', recursive=True)

    list_of_content = []
    for file in files:
        list_of_content.append(file)
    return list_of_content


def read(bucket_name, object_path, file_path):

    object_name = object_path + '/' + file_path
    file = client.fget_object(bucket_name, str(object_name), local_download_path + file_path)

    return file


def archive():
    pass
