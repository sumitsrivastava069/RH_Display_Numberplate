from flask import Flask, render_template, send_from_directory
import csv
import os

app = Flask(__name__)

csv_file = './Frames/output.csv'
image_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

def read_csv():
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                image_path, timestamp, number_plate = row
                data.append({
                    'image_path': image_path,
                    'timestamp': timestamp,
                    'number_plate': number_plate
                })
    return data


@app.route('/')
def display_latest_image():
    data = read_csv()
    latest_image = data[-1] if data else None
    if latest_image:
        image_path = latest_image['image_path']
        full_image_path = os.path.join(image_directory, image_path)
    else:
        full_image_path = None
    return render_template('images/latest_image.html', image_path=full_image_path)


@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(image_directory, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
