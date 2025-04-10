from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Map App</title>
</head>
<body>
    <h1>Google Map - Quận Hoàng Mai</h1>
    <iframe
      width="100%"
      height="400"
      frameborder="0"
      src="https://www.google.com/maps/embed/v1/place?key=AIzaSyDDlMQhxVChW59A2alOB3zkAT_XqVd-f3E=Quận+Hoàng+Mai,Hà+Nội"
      allowfullscreen>
    </iframe>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)