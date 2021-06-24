import os

env = os.environ

file_upload_path = '/tmp'
local_download_path = '/download'

minio_host = 'minio:9000/'
minio_access_key = env.get('MINIO_ACCESS_KEY', 'minio')
minio_secret_key = env.get('MINIO_SECRET_KEY', 'minio123')





