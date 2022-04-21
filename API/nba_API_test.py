import requests

# url = "https://api-nba-v1.p.rapidapi.com/games"
url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
# querystring = {"date":"2022-04-17"}
# querystring = {"season":"2021"}
player_stats = {"season":2019, "id":319}
player_name = {"name": "Lillard"}

headers = {
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "6fe48baa96mshb163a9419d8ad01p19250bjsn43258ad3dc6c"
}

response = requests.request("GET", url, headers=headers, params=player_stats)
print(response)

res = response.json()
res = res['response']
print(res)
# print(res[0]['player']['firstname'], res[0]['player']['lastname'])
# print(res[66]['points'])
pts = 0
for dict in res:
	if dict['points'] == None:
		continue
	else:
		print(dict['points'])
		pts += dict['points']
print(pts)

# print(f"{res['response'][1]['teams']['visitors']['name']} @ {res['response'][1]['teams']['home']['name']}")
# print(f"Score: {res['response'][1]['teams']['visitors']['name']}: {res['response'][1]['scores']['visitors']['points']} {res['response'][1]['teams']['home']['name']}: {res['response'][1]['scores']['home']['points']}")

# def display_who_won(res):
# 	if  res['response'][0]['scores']['visitors']['points'] > res['response'][0]['scores']['home']['points']:
# 		print(f"{res['response'][0]['teams']['visitors']['name']} Beat {res['response'][0]['teams']['home']['name']}\n{res['response'][0]['scores']['visitors']['points']} To {res['response'][0]['scores']['home']['points']}")
# 	else:
# 		print(f"{res['response'][0]['teams']['home']['name']} Beat {res['response'][0]['teams']['visitors']['name']}\n{res['response'][0]['scores']['home']['points']} To {res['response'][0]['scores']['visitors']['points']}")

# display_who_won(res)