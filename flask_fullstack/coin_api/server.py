from flask import Flask, render_template,redirect,jsonify,request,session
import os 
from dotenv import load_dotenv
app = Flask(__name__)
app.config['API_KEY'] = os.environ.get("API_KEY")
import requests

# @app.route('/')
# def index():
#     url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd"

#     querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h"}

#     headers = {
#         "X-RapidAPI-Host": "coinranking1.p.rapidapi.com",
#         "X-RapidAPI-Key": "6fe48baa96mshb163a9419d8ad01p19250bjsn43258ad3dc6c"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     data = response.json()
#     desc = data['data']['coin']['description']
#     p = float(data['data']['coin']['price'])
#     price = "{:.2f}".format(p)
#     # print(price)
#     return render_template('index.html', desc = desc, price = price)

@app.route('/')
def index():
    url = "https://coinranking1.p.rapidapi.com/coins"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

    headers = {
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com",
        "X-RapidAPI-Key": app.config['API_KEY']
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    data = response.json()['data']['coins']
    # data = data['data']['coins']
    lst_of_coins = []
    for coin in data:
        # print(coin['name'])
        lst_of_coins.append(coin['name'])
    return render_template('index.html', coins = lst_of_coins)


if __name__ == "__main__":
    app.run(debug=True)