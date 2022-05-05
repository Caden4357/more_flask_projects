from flask import Flask, render_template,redirect,jsonify,request,session
app = Flask(__name__)
import requests

@app.route('/')
def index():
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h"}

    headers = {
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com",
        "X-RapidAPI-Key": "6fe48baa96mshb163a9419d8ad01p19250bjsn43258ad3dc6c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    desc = data['data']['coin']['description']
    p = float(data['data']['coin']['price'])
    price = "{:.2f}".format(p)
    # print(price)
    return render_template('index.html', desc = desc,price = price)


if __name__ == "__main__":
    app.run(debug=True)