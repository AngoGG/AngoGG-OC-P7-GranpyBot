#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-14
@note    0.0.1 (2020-12-14) : Init file
"""
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return render_template("home.html")
