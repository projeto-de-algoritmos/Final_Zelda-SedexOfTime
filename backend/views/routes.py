from flask import Blueprint, render_template, request, Response
from models.chargeList import ChargeList
from models.graph import Graph

import base64
import cv2
import pandas as pd
import json

pd_bp = Blueprint("", __name__)

df = pd.read_csv('./backend/nodes.csv')
edges = []

for i, row in df.iterrows():
    edges.append((row.origem, row.destino, row.peso))

graph = Graph(edges=edges, directed=False)

cities = { 'Castle Town': (620, 170) ,
           'Hyrule Castle': (641, 83) ,
           'Kakarito Village': (827, 167) ,
           'Zoras Domain': (1155, 138),
           'Zora River': (1019, 236) ,
           'The Lost Woods':(938, 339) ,
           'Deku Tree': (1107, 392),
           'Kokiri Forest': (993, 470),
           'Lake Hylia': (449, 665),
           'Gerudo Valley': (293, 314),
           'Gerudo Fortress': (272, 191),
           'Desert Colossus': (35, 150),
           'Lon Lon Ranch': (601, 274),
          }

def position_finder(paths):
    result = []

    for i,city in enumerate(paths[:-1]):
        if i < len(paths[:-1]) - 1:
            current = cities[city]
            the_next = cities[paths[i+1]]
            first = (int(current[0]), int(current[1]))
            second = (int(the_next[0]), int(the_next[1]))
            result.append((first, second))
    return result

def shortest_path(graph, start, target):
    path = []
    visited = []
    temp_parents = {}
    to_visit = [start]
    distances = {key : float("inf") for key in graph.get_vertices()}
    distances[start] = 0
    final_distance = 0

    while to_visit:
        current = min([(distances[vertex], vertex) for vertex in to_visit])[1]
        if current == target:
            break
        visited.append(current)
        to_visit.remove(current)
        for neighbour, distance in graph.get_neighbors()[current].items():
            if neighbour in visited:
                continue
            vertex_distance = distances[current] + distance
            if vertex_distance < distances[neighbour]:
                distances[neighbour] = vertex_distance
                temp_parents[neighbour] = current
                to_visit.append(neighbour)

    final_distance = distances[target]
    if target not in temp_parents:
        return []
    while target:
        path.append(target)
        target = temp_parents.get(target)
    return path[::-1] + [final_distance]

@pd_bp.route('/knapsack/', methods=["POST"])
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

        charge_list = ChargeList(answers, data['pesoMax']['pesoMax'])

        start = "Lon Lon Ranch"
        target = data['city']['value']

        path = shortest_path(graph, start,target)
        print(path)

        image = cv2.imread('./static/map_default.png')

        points = position_finder(path)

        for i in points:
            cv2.line(image, i[0], i[1], (0,0,255), 2)

        image_b64 = base64.b64encode(cv2.imencode('.png', image)[1]).decode()

        result = {'data': charge_list.knapsack(), 'image': image_b64}

        response = Response(
                response=json.dumps(result),
                status=200,
                mimetype='charge_viewlication/json'
            )
        return response

@pd_bp.route('/', methods=["GET"])
def render_home():
    return "Zelda: Sedex of Time"
