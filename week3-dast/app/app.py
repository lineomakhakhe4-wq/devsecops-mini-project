from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Week 3 DAST App</h1>
    <form action="/search">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
    """

@app.route("/search")
def search():
    query = request.args.get("q")
    html = f"""
    <html>
        <body>
            <h2>Search Results</h2>
            <p>You searched for: {query}</p>
        </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
