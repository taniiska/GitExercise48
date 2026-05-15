from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/bookings_360')
def bookings_360():
    return render_template('bookings.html')


@app.route('/book/<facility>', methods=['GET', 'POST'])
def facility_booking(facility):
    # Facility is passed as a plain string in the URL.
    # Form submission is not persisted; page renders for now.
    if facility is None or facility.strip() == "":
        facility = "Facility"

    return render_template('facility_booking.html', facility=facility)



if __name__ == "__main__":
    app.run(debug=True)

