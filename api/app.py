from flask import Flask, jsonify
import json

app=Flask(__name__)

#Loading JSON data
with open("../data/fuel_prices.json", "r") as file:
    fuel_data = json.load(file)

#Route (endpoint)
@app.route("/fuel_prices", methods=["GET"])
def get_fuel_prices():
    return jsonify(fuel_data)

#Run server
if __name__ == "__main__":
    app.run(debug=True)