from flask import render_template, jsonify
from app import app
from app.utils import get_indicators, get_indicator_data, create_plot

@app.route('/')
def index():
    indicators = get_indicators()
    return render_template('dashboard.html', indicators=indicators)

@app.route('/data/<indicator>')
def get_data(indicator):
    data = get_indicator_data(indicator)
    plot_url = create_plot(data, indicator)
    return jsonify({'plot_url': plot_url, 'data': data.to_dict()})