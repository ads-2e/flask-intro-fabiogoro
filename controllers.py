from flask import flash, render_template, redirect, request, session
from server import app

@app.route('/')
def index():
    return render_template(
        'index.html',
    )
