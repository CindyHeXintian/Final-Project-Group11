import json
from flask import Flask, render_template
from dateutil.parser import parse as dparse

from bitcoin.data.base import get_dataframe

app = Flask(__name__)

@app.route("/<crypto>")
def main(crypto):
    crypto = crypto.upper()  # btc -> BTC
    data = get_dataframe(crypto)

    # Sort data by datetime.asc()
    converted = dict()
    for key, values in data.items():
        lst = [[dparse(k), k, v] for k, v in values.items()]
        lst.sort(key=lambda x: x[0])
        converted[key] = [[x[1], x[2]] for x in lst]
    return render_template('main.j2', data=json.dumps(converted), crypto=crypto)
