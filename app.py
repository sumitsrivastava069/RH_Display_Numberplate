from flask import Flask, render_template
import csv
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def render_image():
    image_data = []

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Read the CSV file
    csv_file_path = os.path.join(current_dir, 'Frames', 'output.csv')
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            image_filename = row[0]
            date_time = row[1]
            number_plate = row[2]

            image_path = os.path.join(image_filename)

            print('image' - image_path)  # Print the image path

            image_data.append({
                'image_path': image_path,
                'date_time': date_time,
                'number_plate': number_plate
            })

    return render_template('images/index.html', image_data=image_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
