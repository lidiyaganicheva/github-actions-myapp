import configparser
from flask import Flask
import os

config = configparser.RawConfigParser()
config.read('config.properties')

app = Flask(__name__)


f = open('/etc/hostname')
pod_name = f.read()
f.close()


if config.getboolean("features", "feature_1") == True:
	message = f"Hello, Sasha! Current pod name: {pod_name}"
else:
	message = f"Hello, World! Current pod name: {pod_name}"

@app.route("/")
def hello():
	return message 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)
