from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    """Serve the homepage"""
    return send_from_directory('.', 'pt.html')

@app.route('/pt.html')
def periodic_table():
    """Serve the periodic table page"""
    return send_from_directory('.', 'pt.html')

@app.route('/index.html')
def index():
    """Serve the old index page"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve any other static files"""
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
