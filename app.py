import os
import sys
import subprocess
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

REPO_ROOT = os.path.abspath('.')
EXCLUDED = {'templates', '__pycache__', '.git', '.github', 'venv', 'env'}

def get_folders():
    """Auto-detect script folders, refreshed on each search."""
    return [
        d for d in os.listdir(REPO_ROOT)
        if os.path.isdir(d) and d not in EXCLUDED and not d.startswith('.')
    ]

def find_script(name):
    """Search all folders for a matching .py file."""
    for folder in sorted(get_folders()):
        path = os.path.join(REPO_ROOT, folder, f"{name}.py")
        if os.path.exists(path):
            return path
    return None

def is_safe_path(path):
    """Ensure path stays within repo root — prevents directory traversal."""
    return os.path.abspath(path).startswith(REPO_ROOT)

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    filename = (request.json.get('filename') or '').strip().replace('.py', '')
    if not filename:
        return jsonify({"status": "error", "message": "No filename provided"}), 400

    path = find_script(filename)
    if path:
        rel = os.path.relpath(path, REPO_ROOT)
        return jsonify({"status": "found", "path": rel})
    return jsonify({"status": "not_found"})


@app.route('/view/<script_name>')
def view_file(script_name):
    path = find_script(script_name.replace('.py', ''))
    if not path or not is_safe_path(path):
        return jsonify({"error": "File not found"}), 404

    try:
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()
        return jsonify({
            "code": code,
            "path": os.path.relpath(path, REPO_ROOT)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/run/<script_name>')
def run_file(script_name):
    path = find_script(script_name.replace('.py', ''))
    if not path or not is_safe_path(path):
        return jsonify({"error": "File not found"}), 404

    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.path.dirname(path)   # run from script's own folder
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Script timed out after 30 seconds"}), 408
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print(f"PyHub running at http://localhost:5000")
    print(f"Repo root: {REPO_ROOT}")
    print(f"Folders detected: {get_folders()}\n")
    app.run(host='0.0.0.0', port=5000, debug=False)
