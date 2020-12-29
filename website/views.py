#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-14
@note    0.0.1 (2020-12-14) : Init file
"""

import os
from typing import Dict
from flask import Flask, jsonify, render_template, Response, request
from grandpy.app import App

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return render_template(
        "home.html", google_api_public_key=os.environ.get("GOOGLE_API_PUBLIC_KEY")
    )


@app.route("/ask_grandpy", methods=["POST"])
def ask_grandpy() -> Response:
    query: str = request.get_data().decode()
    grandpy: App = App()
    response: Dict[str, any] = grandpy.answer(query)

    print(f"query : {query}")
    print(f"response : {response}")
    if response:
        return jsonify(response), 200
    else:
        return jsonify({"answer": "Erf, pas trouvé"}), 400
