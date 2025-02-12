from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        

    return render_template("logins.html")