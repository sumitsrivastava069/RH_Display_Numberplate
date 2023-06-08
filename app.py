from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def render_image():
    image_data = []

    # Read the CSV file
    with open('./Frames/output.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            image_path = row[0]
            date_time = row[1]
            number_plate = row[2]

            image_data.append({
                'image_path': image_path,
                'date_time': date_time,
                'number_plate': number_plate
            })

    return render_template('images/latest_image.html', image_data=image_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
