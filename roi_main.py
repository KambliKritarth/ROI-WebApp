from flask import Flask, render_template, url_for

# initialise Flask as app
app = Flask("__main__")

@app.route("/main", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    # renders the main page
    return render_template("index.html")

# run the webapp
if __name__ == "__main__":
    app.run(port=7777)
