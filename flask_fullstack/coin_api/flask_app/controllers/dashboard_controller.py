from flask import Flask, render_template,redirect,jsonify,request,session
from flask_app import app
import requests

@app.route('/')
def index():
    url = "https://coinranking1.p.rapidapi.com/coins"
# orderBy must be one of price, marketCap, 24hVolume, change, listedAt
    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"24hVolume","orderDirection":"desc","limit":"50","offset":"0"}

    headers = {
        "X-RapidAPI-Host": app.config['API_HOST'],
        "X-RapidAPI-Key": app.config['API_KEY']
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    data = response.json()['data']['coins']
    # print(data)
    # data = data['data']['coins']
    lst_of_coins = []
    for coin in data:
        # print(coin['name'])
        lst_of_coins.append({
            'name': coin['name'],
            'id': coin['uuid'],
            'icon': coin['iconUrl']
            })
    # print(lst_of_coins)
    return render_template('index.html', coins = lst_of_coins)



@app.route('/<string:name>/<string:id>')
def view_one_coin(name, id):
    url = f"https://coinranking1.p.rapidapi.com/coin/{id}"

    querystring = {"timePeriod":"24h"}

    headers = {
        "X-RapidAPI-Host": app.config['API_HOST'],
        "X-RapidAPI-Key": app.config['API_KEY']
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    # print(data)
    desc = data['data']['coin']['description']
    p = float(data['data']['coin']['price'])
    price = "{:.2f}".format(p)
    print(price)
    return render_template('coin_details.html', desc = desc, price = price ,name=name)

@app.route('/search/coin' , methods=['POST'])
def search_for_crypto():
    url = "https://coinranking1.p.rapidapi.com/search-suggestions"
    search_str = request.form['search_string']
    print(search_str)
    # search_for_crypto()
    querystring = {"query":search_str}

    headers = {
        "X-RapidAPI-Host": app.config['API_HOST'],
        "X-RapidAPI-Key": app.config['API_KEY']
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    search_results = data['data']['coins']
    return render_template('search_results.html', search_results=search_results)
