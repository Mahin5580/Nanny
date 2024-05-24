from flask import Flask, request, jsonify

app = Flask(__name__)

bookings = []

@app.route('/book', methods=['POST'])
def book_babysitter():
    data = request.json
    babysitter = data.get('babysitter')
    date = data.get('date')
    time = data.get('time')
    duration = data.get('duration')
    instructions = data.get('instructions')
    
    if not babysitter or not date or not time or not duration:
        return jsonify({"error": "Missing required fields"}), 400
    
    booking = {
        "babysitter": babysitter,
        "date": date,
        "time": time,
        "duration": duration,
        "instructions": instructions
    }
    bookings.append(booking)
    return jsonify({"message": "Booking successful!", "booking": booking}), 200

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Babysitter Booking System"}), 200

if __name__ == '__main__':
    app.run(debug=True)
