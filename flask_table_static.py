from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder='t_templates')

@app.route('/')
def index():
    data = {
        'Column 1': ['A', 'B', 'C'],
        'Column 2': [1, 2, 3],
        'Column 3': [10.1, 20.2, 30.3]
    }
    df = pd.DataFrame(data)
    return render_template('table_static1.html', tables=[df.to_html(classes='data', header="true", index=False)])

if __name__ == '__main__':
    app.run(debug=True)

