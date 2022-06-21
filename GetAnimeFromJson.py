from Anime import Anime
import ResponseManuver as rm
import json
from typing import List


def GenerateAnimeFromJson():
    data = None

    file = open("AnilistJsonResponse.json", 'r', encoding="utf-8")

    data = json.load(file)

    file.close()

    listsJS = {
        'COMPLETED': [],
        'DROPPED': [],
        'PLANNING': [],
        'PAUSED': [],
        'CURRENT': []
    }

    lists: dict[str, List[Anime]]
    lists = {
        'COMPLETED': [],
        'DROPPED': [],
        'PLANNING': [],
        'PAUSED': [],
        'CURRENT': []
    }

    for x in data['data']['MediaListCollection']['lists']:
        listsJS[x['status']] = x['entries']
        # print(len(lists[x['status']]))

    for list in listsJS.keys():
        for show in listsJS[list]:
            lists[list].append(rm.CreateAnimeFromEntry(show))

    return lists
