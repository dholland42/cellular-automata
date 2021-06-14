import click
from flask import Flask, jsonify, request

from cellular_automata.ca import transition

app = Flask(__name__)


@app.route("/", methods=["POST"])
def serve():
    data = request.json
    return jsonify({"state": transition(data.get("state"), int(data.get("rule", "30")))})


@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=5000)
def main(host, port):
    app.run(host=host, port=port)

if __name__ == "__main__":
    main()
