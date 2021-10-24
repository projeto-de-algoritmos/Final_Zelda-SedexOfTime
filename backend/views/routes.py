from flask import Blueprint, render_template, request

pd_bp = Blueprint("", __name__)


@pd_bp.route('/knapsack/', methods=["GET", "POST"])
def render_knapsack():
    if request.method == "GET":
        a1 = {
            'url': 'https://slideplayer.com/16452203/96/images/slide_1.jpg',
            'name': 'Weighted interval scheduling',
            'description': '253,5 MiB',
            'tag': 'a1'}
        a2 = {
            'url': 'https://static.preparaenem.com/conteudo_legenda/0c3d1011773a8f288d9386cdc8af3b67.jpg',
            'name': 'Maior subsequência crescente',
            'description': '114,5 MiB',
            'tag': 'a2'}
        a3 = {
            'url': 'https://cdn.shopify.com/s/files/1/0159/0864/products/Knapsack_beige_in_use-1_800x.jpg?v=1605311728',
            'name': 'KnapSack',
            'description': '291,7 MiB',
            'tag': 'a3'}
        a4 = {
            'url': 'https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/figs/coelho-2011/coelho2011-18-2.png',
            'name': 'Bellman-Ford',
            'description': '280,9 MiB',
            'tag': 'a4'}
        a5 = {
            'url': 'https://miro.medium.com/max/1000/1*k38B19pWF7rZpkZlQ9rYag.png',
            'name': 'Alinhamento de sequência - parte 1',
            'description': '190,7 MiB',
            'tag': 'a5'}
        a6 = {
            'url': 'https://aristocratas.files.wordpress.com/2012/02/part21.png',
            'name': 'Alinhamento de sequência - parte 2',
            'description': '468,3 MiB',
            'tag': 'a6'}
        return render_template(
            'knapsack.html', row1=[
                a1, a2, a3, ], row2=[
                a4, a5, a6, ])
    else:
        memory = request.form.get('memory')
        values = [
            request.form.get('a1'),
            request.form.get('a2'),
            request.form.get('a3'),
            request.form.get('a4'),
            request.form.get('a5'),
            request.form.get('a6'),
        ]
        weight = [253, 114, 291, 280, 190, 468]
        values = [int(i) for i in values]
        return render_template('knapsack_result.html', result=knapsack(
            int(memory), weight, values, len(values)), val_max=sum(values))


@pd_bp.route('/', methods=["GET"])
def render_home():
    return render_template('home.html')
