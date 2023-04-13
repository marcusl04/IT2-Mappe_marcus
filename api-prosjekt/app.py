from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

fil = open("sharks.json")
sharks = json.load(fil)

shark_url = "https://www.mapotic.com/api/v1/maps/3413/pois.geojson/?h=30"
res = requests.get(shark_url)
chart = json.loads(res.text)
chart = chart["features"][:25]
# fil_chart = open("shark.json")
# chart = json.load(fil)
# chart = chart["features"]

favorites = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sharks")
def rute_sharks():
    return render_template("sharks.html", sharks=sharks)

@app.route("/chart")
def rute_chart():
    return render_template("chart.html", chart=chart)

@app.route("/shark/<id>")
def rute_shark(id):
    shark = sharks[id]
    return render_template("shark.html", id=id, shark=shark)

@app.route("/about")
def rute_about():
    return render_template("about.html")

@app.route("/shark/<id>/add-to")
def rute_add_to(id):
    favorites.append(id)
    return rute_shark(id)

@app.route("/favorites")
def rute_favorites():
    return render_template("favorites.html", favorites=favorites, sharks=sharks)

@app.route("/favorites/delete/<id>")
def rute_delete(id):
    favorites.remove(id)
    return rute_favorites()
