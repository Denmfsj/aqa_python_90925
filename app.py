from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

upload_directory = './uploads'
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(upload_directory, image.filename)
    image.save(filename)

    return jsonify({'image_url': request.host_url + 'uploads/' + image.filename}), 201


@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    content_type = request.headers.get('Content-Type')
    filepath = os.path.join(upload_directory, filename)
    if os.path.exists(filepath):
        if content_type == 'text':
            return jsonify({'image_url': request.host_url + 'uploads/' + filename}), 200
        elif content_type == 'image':
            return send_from_directory(upload_directory, filename)
        else:
            return jsonify({'error': 'Unsupported Content-Type'}), 400
    else:
        return jsonify({'error': 'Image not found'}), 404


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    filepath = os.path.join(upload_directory, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404

    os.remove(filepath)
    return jsonify({'message': f'Image {filename} deleted'}), 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)