# Import necesaty libraries for the task

from flask import Flask, jsonify 
import requests  # Import requests module to make request to get the jokes

app = Flask(__name__)  # Create a Flask application instance

# Home url to get a welcome message in case we don't go strait to the /getJokes url

@app.route('/')  
@app.route('/home') 
def home():  
    return 'Welcome Back!!!'  # Welcome message

@app.route('/getJokes')  # /getJokes URL
def jokes():  # Define the jokes function to handle requests to the /getJokes URL
    jokes_list = []  # Initialize an empty list to store jokes

    # url = 'http://api.icndb.com/jokes/random/'  # Original URL for Chuck Norris jokes API, I dismiss this one since it doesn't work when I try to run it 
    url = 'https://api.chucknorris.io/jokes/random'  # New URL for Chuck Norris jokes API found in the web in the following link https://api.chucknorris.io/

    for _ in range(10):  # Loop 10 times to fetch 10 jokes
        response = requests.get(url)  # Make an HTTP GET request to the API
        data = response.json()  # Parse the JSON response
        jokes_list.append(data['value'])  # Append the joke text to the jokes_list, only getting the 'value', in this case, the joke 

    return jsonify(jokes_list)  # Return the list of jokes as a JSON response so it can be displayed in the computer without using a front-end page 

# Run the Flask application 
if __name__ == '__main__':
    app.run(debug=True)  