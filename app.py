import os
import json
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import NMS
from models import Hosttable

columns = [
    {
        "field": "id",
        "title": "No.",
        "sortable": True,
    },
    {
        "field": "location", # which is the field's name of data key
        "title": "Location", # display as the table header's name
        "sortable": True,
    },
    {
        "field": "oid",
        "title": "IP",
        "sortable": True,
    },
    {
        "field": "uptime",
        "title": "Up Time",
        "sortable": True,
    }
]



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_host():
    ip=request.args.get('ip')
    name=request.args.get('name')
    status=request.args.get('status')
    try:
        hosttable=Hosttable(
            ip=ip,
            name=name,
            status=status
        )
        db.session.add(hosttable)
        db.session.commit()
        return "IP added. IP id={}".format(hosttable.id)
    except Exception as e:
        return(str(e))

@app.route("/getall")
def get_all():
    try:
        nms = NMS.query.all()
        return  jsonify([e.serialize() for e in nms])
    except Exception as e:
        return(str(e))

@app.route("/test")
def test():
    nms = NMS.query.all()
    data = get_all()
    print([e.serialize() for e in nms])
    return data

@app.route("/showall")
def showall():
    try:
        nms = NMS.query.all()
        data = [e.serialize() for e in nms]
        return render_template("showall.html",
                           data=data,
                           columns=columns,
                           title='Data Hasil Scanning')
    except Exception as e:
        return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        hosttable=Hosttable.query.filter_by(id=id_).first()
        return jsonify(hosttable.serialize())
    except Exception as e:
        return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_host_form():
    if request.method == 'POST':
        ip=request.form.get('ip')
        name=request.form.get('name')
        status=request.form.get('status')
        try:
            hosttable=Hosttable(
                ip=ip,
                name=name,
                status=status
            )
            db.session.add(hosttable)
            db.session.commit()
            return "IP added. IP id={}".format(hosttable.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")