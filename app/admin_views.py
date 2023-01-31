from app import app

from flask import Flask,request,render_template

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')
    
@app.route('/register')
def register():
    return render_template('admin/register.html')

@app.route('/appointment')
def appoint():
    return render_template('admin/appointment.html')

    