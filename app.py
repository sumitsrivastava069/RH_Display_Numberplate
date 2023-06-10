from flask import Flask, render_template
import csv
import os

app = Flask(__name__, static_folder='static')
latest_image_data = {}

def update_image_data():
    global latest_image_data

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Read the CSV file
    csv_file_path = os.path.join(current_dir, 'static' , 'numberplateimages', 'numberplates_data.csv')
    latest_entry = {}

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header row
        for row in csv_reader:
            image_filename = row[0]
            number_plate = row[3]
            date_time = row[2]
            color = row[4]

            image_path = os.path.join('static', image_filename)

            if color == 'Green' or color == 'Red':
                entry = {
                    'image_path': image_path,
                    'date_time': date_time,
                    'number_plate': number_plate,
                    'color': color
                }

                if not latest_entry or date_time > latest_entry['date_time']:
                    latest_entry = entry
        print(image_path)
    latest_image_data = latest_entry

@app.route('/')
def render_image():
    return render_template('images/index.html', image_data=latest_image_data)

if __name__ == '__main__':
    update_image_data()  # Initial data update

    app.run(host='0.0.0.0', port=5000,debug=True)
