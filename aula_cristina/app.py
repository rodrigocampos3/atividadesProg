from flask import Flask, request, jsonify, render_template
import pandas as pd
from scipy.stats import ttest_ind

app = Flask(__name__)


def perform_t_test(data1, data2, alternative):
    # Perform a t-test for independent samples
    t_statistic, p_value = ttest_ind(data1, data2, alternative=alternative)
    return t_statistic, p_value

@app.route('/test_hypothesis', methods=['POST'])
def test_hypothesis():
    try:
        if 'file' not in request.files:
            return render_template('error.html', error='No file provided'), 400

        file = request.files['file']
        alternative = request.args.get('alternative', 'two-sided')

        df = pd.read_excel(file)

        if 'data1' not in df.columns or 'data2' not in df.columns:
            return render_template('error.html', error='Missing required columns (data1, data2)'), 400

        data1 = df['data1']
        data2 = df['data2']

        t_statistic, p_value = perform_t_test(data1, data2, alternative)

        result = {
            't_statistic': t_statistic,
            'p_value': p_value,
            'alternative': alternative
        }

        return render_template('results.html', result=result), 200

    except Exception as e:
        return render_template('error.html', error=str(e)), 500


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
