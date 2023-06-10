from flask import Flask, render_template
import csv
import os
import time

app = Flask(__name__)

def get_last_entry(csv_file_path):
    # Check if the CSV file exists
    if os.path.isfile(csv_file_path):
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            last_entry = None

            # Iterate over the rows in reverse order
            for row in reversed(list(csv_reader)):
                last_entry = row
                break  # Only need the last entry, so break after the first row

            if last_entry:
                # Extract the desired values
                image_path = last_entry[0]
                number_plate_image_path = last_entry[1]
                date_time = last_entry[2]
                number_plate = last_entry[3]
                color = last_entry[4]
                print(image_path)
                return {
                    'image_path': image_path,
                    'number_plate_image_path': number_plate_image_path,
                    'date_time': date_time,
                    'number_plate': number_plate,
                    'color': color
                    
                }
            else:
                return None
    else:
        return None

@app.route('/')
def render_last_entry():
    csv_file_path = './static/numberplateimages/numberplates_data.csv'
    last_entry = get_last_entry(csv_file_path)

    return render_template('images/index.html', entry=last_entry)



if __name__ == '__main__':
    while True:
        app.run( use_reloader=False, host='0.0.0.0')
        time.sleep(10)
