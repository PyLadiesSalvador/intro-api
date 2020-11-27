# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request


app = Flask('app')


@app.route("/")
def hello():
    return "Hello World in Flask!"


@app.route("/<name>")
def index(name):
    return "Olá {}".format(name), 200


@app.route("/html/<nome>")
def html_page(nome):
    return render_template("html_page.html", nome=nome)


@app.route("/jsonify")
def json_api_jsonify():
    pessoas = [{"nome": "Ana", "idade": 25},
               {"nome": "Claudia", "idade": 26},
               {"nome": "Priscila", "idade": 27},
               {"nome": "Carine", "idade": 28}]

    return jsonify(pessoas=pessoas, total=len(pessoas))


@app.route("/eleicao2020/")
def get_top_votos_candidatos():
    cargo = request.args.get('cargo', 'Vereador')
    indice = request.args.get('indice', 3)

    candidatos = get_top_votos(cargo, indice)

    return jsonify(candidatos=candidatos)


def get_top_votos(cargo, indice):
    import pandas as pd

    dados = pd.readcsv('dados/dados.csv')
    dados = dados.loc[dados['CARGO'] == cargo]
    dados = dados.sort_values('QTD_VOTOS', ascending=False).head(indice)

    return dados


app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    app.run()
