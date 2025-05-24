from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load data
result = pd.read_csv("result.csv", index_col=0)

@app.route('/')
def index():
    return render_template("index.html", tables=[result.to_html(classes='data')], titles=result.columns.values)

@app.route('/statistics')
def statistics():
    stats = {
        "Transpose": result.T.to_html(),
        "Columns": result.columns.tolist(),
        "Indexes": result.index.tolist(),
        "Shape": result.shape,
        "Dimension": result.ndim,
        "Data Types": result.dtypes.to_dict(),
        "Size": result.size
    }
    return render_template("statistics.html", stats=stats)

@app.route('/plot/<chart_type>/<metric>')
def plot(chart_type, metric):
    fig, ax = plt.subplots()
    if chart_type == "line":
        result[metric].plot(ax=ax)
    elif chart_type == "bar":
        result[metric].plot(kind='bar', ax=ax)
    elif chart_type == "barh":
        result[metric].plot(kind='barh', ax=ax)
    elif chart_type == "hist":
        result[metric].plot(kind='hist', bins=5, ax=ax)
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template("plot.html", plot_url=plot_url, chart_type=chart_type, metric=metric)

@app.route('/analytics')
def analytics():
    data = {
        "Max Average": result['average'].max(),
        "Min Average": result['average'].min(),
        "Max Highest": result['highest'].max(),
        "Min Highest": result['highest'].min(),
        "Max % A1+A2": result['per'].max(),
        "Min % A1+A2": result['per'].min()
    }
    return render_template("analytics.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
