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

    # Usef when Wiki API is dead
    # response = {
    #    "location": {"lat": 48.856614, "lng": 2.3522219},
    #    "title": "Jeux olympiques d'été de 2024",
    #    "summary": "Les Jeux olympiques d'été de 2024",
    #    "url": "https://fr.wikipedia.org/wiki/Jeux_olympiques_d'été_de_2024",
    # }

    if response:
        return jsonify(response), 200
    else:
        return jsonify({"answer": "Erf, pas trouvé"}), 400
