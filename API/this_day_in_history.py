import requests

url = "https://api-nba-v1.p.rapidapi.com/games"

querystring = {"date":"2022-04-21"}

headers = {
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "6fe48baa96mshb163a9419d8ad01p19250bjsn43258ad3dc6c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.json()
# print(res)
print(f"{res['response'][1]['teams']['visitors']['name']} @ {res['response'][1]['teams']['home']['name']}")
print(f"Score: {res['response'][1]['teams']['visitors']['name']}: {res['response'][1]['scores']['visitors']['points']} {res['response'][1]['teams']['home']['name']}: {res['response'][1]['scores']['home']['points']}")