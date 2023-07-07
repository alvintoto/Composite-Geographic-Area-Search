from flask import Flask
from project.views.geo import geo_blueprint

app = Flask(__name__)
app.register_blueprint(geo_blueprint)
