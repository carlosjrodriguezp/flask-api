from flask import Flask, jsonify, make_response, request, abort, url_for
import random

from quotes import funny_quotes
from data_provider_service import DataProviderService

DATA_PROVIDER = DataProviderService(15)

app = Flask(__name__)

@app.route("/api", methods=['GET'])
def list_routes():
	result = []
	for rst in app.url_map.iter_rules():
		result.append({
			"methods": list(rst.methods),
			"route": str(rst)
			})
	return jsonify({"routes": result, "total": len(result)})

def candidate():
	candidates = DATA_PROVIDER.get_candidates()
	return jsonify({"candidates": candidates, "total": len(candidates)})

app.add_url_rule('/api/candidate','candidate',candidate)

@app.route("/api/candidate/<string:id>", methods=['GET'])
def candidate_by_id(id):
	candidate = DATA_PROVIDER.get_candidate(id)
	if candidate:
		return jsonify({"candidate": candidate})
	else:
		abort(404)

@app.route("/api/candidate/<string:id>/name/<string:new_name>", methods=['PUT'])
def update_name(id, new_name):
	nr_of_updated_items = DATA_PROVIDER.update_name(id, new_name)
	if nr_of_updated_items == 0:
		abort(404)
	else:
		return jsonify({"total_updated": nr_of_updated_items})

@app.route("/api/candidate/delete/<string:id>", methods=['DELETE'])
def delete(id):
	if DATA_PROVIDER.delete_candidate(id):
		return make_response('',200)
	else:
		abort(404)

@app.route("/api/candidate", methods=['POST'])
def add_candidate():
	first_name = request.form['first_name']
	last_name = request.form['last_name']

	new_candidate_id = DATA_PROVIDER.add_candidate(first_name, last_name)

	return jsonify({
		"id": new_candidate_id,
		"url": url_for("candidate_by_id", id=new_candidate_id)
		})





@app.route("/api/funny")
def serve_funny_quotes():
	quotes = funny_quotes()
	nr_of_quotes = len(quotes)
	selected_quote = quotes[random.randint(0, nr_of_quotes - 1)]
	return jsonify(selected_quote)

if __name__ == '__main__':
	app.run(debug=True)