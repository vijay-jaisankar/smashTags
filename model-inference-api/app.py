from flask import Flask

app = Flask(__name__)

"""
    Base API Route
        - Checks if the site is up
"""
@app.route("/")
def index():
    output_dict = {
        "status" : "up"
    }
    return output_dict


# Launch the app
if __name__ == "__main__":
    app.run(debug = True)