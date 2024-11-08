from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Fetch air quality data from OpenAQ API
def get_air_quality_data(city):
    url = f"https://api.openaq.org/v2/latest?city={city}"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())  # Check the output in the terminal
        return response.json()
    else:
        print("Error fetching data.")
        return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/air_quality/<city>')
def air_quality(city):
    data = get_air_quality_data(city)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
