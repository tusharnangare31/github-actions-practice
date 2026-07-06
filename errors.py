from flask import Flask

# 1. Initialize the application instance
app = Flask(__name__)

# 2. Define a route and bind it to a function
@app.route("/")
def home():
    return "Hello, World! Welcome to Flask."

# 3. Start the local development server
if __name__ == "__main__":
    app.run(debug=True)
