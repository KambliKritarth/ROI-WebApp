from flask import *

# initialise Flask as app
app = Flask("__main__")

@app.route('/', methods=["GET"])
def index():
    # renders the main page
    return render_template("index.html")

# run the webapp
if __name__ == "__main__":
    app.run(port=7777)
