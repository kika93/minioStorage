from flask import Flask, request
from StorageService import *

app = Flask(__name__)

temp_folder = file_upload_path


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/list_buckets', methods=['GET'])
def list_all():
    """:return: returns list of the available buckets"""

    buckets = list_buckets()

    return str(buckets)


@app.route('/get_content/<bucket>', methods=['GET'])
def get_content(bucket):
    """:return: returns list of names of the content in a specified bucket"""

    content = list_files(bucket)
    content_names = []
    for c in content:
        content_names.append(c.object_name)

    return str(content_names)


@app.route('/upload_file/<bucket>', methods=['POST'])
def upload1(bucket):
    """Uploads any type of file onto the bucket
    :return: returns the filename"""

    dir_path = request.args.get('dir_path')
    print(temp_folder)

    file = request.files['file']
    file.save(os.path.join(temp_folder, file.filename))

    upload_file(file, bucket, dir_path)
    return str(file.filename)


@app.route('/read/<bucket>/<filename>', methods=['GET'])
def download(bucket, filename):

    path = request.args.get('path')
    file = read(bucket, path, filename)

    return str(filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
