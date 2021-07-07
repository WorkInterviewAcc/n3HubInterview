import file_manager
from flask import Flask, json, request

api = Flask(__name__)


@api.route('/file', methods=['GET'])
def get_file():
    contents = ''

    # Get file_name request
    try:
        file_name = request.args["fileName"]
    except IndexError:
        print("Could not find fileName parameter.")

    file_man = file_manager.FileManager()
    file_path = file_man.get_file_path(file_name)

    if file_path:
        contents = file_man.get_content(file_name)

    package = file_name
    if contents:
        package += '\n' + contents

    if not file_path:
        package += '\n No file with that name.'

    return json.dumps(package)


@api.route('/file', methods=['POST'])
def post_file():
    return json.dumps('post_file end point'), 202


if __name__ == '__main__':
    api.run()
