from flask import Flask, jsonify, request

from cellular_automata.combinations import CombinationsCA

app = Flask(__name__)

CA = CombinationsCA()


@app.route("/", methods=["POST"])
def serve():
    state = CA.value
    CA.step()
    return jsonify({"state": state})


@app.route("/reset", methods=["POST"])
def reset():
    data = request.json
    CA.reset(state=data.get("state"))
    return jsonify({"state": CA.value})


if __name__ == "__main__":
    app.run()
