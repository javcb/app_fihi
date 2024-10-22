from flask import Flask, render_template_string
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <h1>Run Python Script</h1>
            <p>Click the link below to execute the Python script:</p>
            <a href="/run-script">Run a_1_pip_installs.py</a>
        </body>
        </html>
    '''

@app.route('/run-script')
def run_script():
    script_path = "C:\\Users\\amrjb\\OneDrive\\1_Dev\\2_Web app2\\a_config\\pip_installs.py" # todo: update to relative path
    try:
        subprocess.Popen([sys.executable, script_path])
        return "Script is running in the background."
    except Exception as e:
        return f"An error occurred while executing the script: {e}"

if __name__ == '__main__':
    app.run(debug=True)
