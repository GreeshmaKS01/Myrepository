from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    """
    Endpoint to return a simple greeting message.
    """
    return 'Hello, Azure! This is a Python web app using Flask and my name is Greeshma.'

# Run the application
if __name__ == '__main__':
    # Use environment variables for host and port for flexibility
    import os
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    
    # Start the Flask application
    app.run(host=host, port=port)
