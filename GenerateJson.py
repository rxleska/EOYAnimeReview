from django.http import JsonResponse
import AniQuery
import requests
from urllib import response
from requests.models import requote_uri
import json

query = AniQuery.query
# Anilist public api url
url = 'https://graphql.anilist.co'
nameId = "R3adyplayer2"
variables = {
    'name': nameId  # used in query
}

response = requests.post(url, json={'query': query, 'variables': variables})
jsonRes = response.json()

with open('AnilistJsonResponse.json', 'w', encoding="utf-8") as file:
    json.dump(jsonRes, file)
    file.close()
    # file.write(json)
