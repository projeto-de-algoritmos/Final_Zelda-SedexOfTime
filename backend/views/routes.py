from flask import Blueprint, render_template, request, Response
from models.chargeList import ChargeList
import json

pd_bp = Blueprint("", __name__)


@pd_bp.route('/knapsack/', methods=["GET", "POST"])
def render_knapsack():
    data = request.get_json()
    print(data.keys())
    if 'answers' not in data.keys() or 'pesoMax' not in data.keys() or 'city' not in data.keys():
        response = Response(
                status=400,
                mimetype='charge_viewlication/json'
            )
        return response
    else:
        answers = data['answers']
        print(answers[0]['peso'])
        charge_list = ChargeList(answers, data['pesoMax']['pesoMax'])
        result = {'data': charge_list.knapsack()}
        response = Response(
                response=json.dumps(result),
                status=200,
                mimetype='charge_viewlication/json'
            )
        return response

@pd_bp.route('/', methods=["GET"])
def render_home():
    return "Zelda: Sedex of Time"
