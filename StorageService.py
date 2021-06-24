from minio import Minio


FILE_UPLOADS = '/tmp'
LOCAL_DOWNLOAD_PATH = '/download/'

client = Minio(

    endpoint='minio:9000/',
    access_key='minio',
    secret_key='minio123',
    secure=False
)


def upload_file(file, bucket, dir_path):

    found = client.bucket_exists(bucket)
    if not found:
        client.make_bucket(bucket)
    else:
        print('bucket already exists')
    client.fput_object(bucket, dir_path + '/' + file.filename,
                       file_path=FILE_UPLOADS + '/' + file.filename),
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
    file = client.fget_object(bucket_name, str(object_name), LOCAL_DOWNLOAD_PATH + file_path)

    return file


def archive():
    pass
