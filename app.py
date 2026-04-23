from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)

# List your 10 folders here
BASE_DIRS = ['folder1', 'folder2', 'folder3'] # etc...

def find_script(name):
    """Search for the script in all defined folders."""
    for folder in BASE_DIRS:
        path = os.path.join(folder, f"{name}.py")
        if os.path.exists(path):
            return path
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    filename = request.json.get('filename')
    path = find_script(filename)
    if path:
        return jsonify({"status": "found", "path": path})
    return jsonify({"status": "not_found"})

@app.route('/view/<path:path>')
def view_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return f"<pre>{content}</pre>"

@app.route('/run/<path:path>')
def run_file(path):
    try:
        # Executes the script and captures output
        result = subprocess.check_output(['python', path], stderr=subprocess.STDOUT, text=True)
        return f"<pre>Output:\n{result}</pre>"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)