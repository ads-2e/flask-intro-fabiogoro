from flask import flash, render_template, redirect, request, session
from server import app

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/entrar/')
def entrar():
    return render_template(
        'entrar.html',
    )

@app.route('/inscrever/')
def inscrever():
    return render_template(
        'inscrever.html',
    )
