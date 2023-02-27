from cProfile import label
import math
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import false
from typing import List
from Anime import AniName, Anime, Recommendations
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime


def GetBestName(name: AniName):
    """Returns Most Recongnisable Name"""
    n = None
    if name.english != None:
        n = name.english
    elif name.synonyms != None and len(name.synonyms) > 0:
        n = name.synonyms[0]
    elif name.romaji != None:
        n = name.romaji
    elif name.native != None:
        n = name.native
    return n.__str__()


def GetReconValue(i):
    if i < 1:
        return -1
    else:
        # returns the number of digits in the number squared
        return math.floor(math.log10(i)) ** 3


# Anime Data
ani = GetAnime()

# Maps and list
recoms = {}
idtoNameMap = {}
showList = ani['COMPLETED']
idLst = []

for show in showList:
    idLst.append(show.ids.anilist)

    for recommendation in show.recommendations:
        if recommendation.numberOfEpisodes is not None:
            id = recommendation.id
            idtoNameMap[id] = recommendation.name  # Id to Name map

            # Ids to Recom Value
            if id not in recoms.keys():
                recoms[id] = GetReconValue(recommendation.rank)
            else:
                x = recoms[id]
                recoms[id] = x + GetReconValue(recommendation.rank)


# sorts recommendations
recoms = sorted(recoms.items(), key=lambda x: x[1])
recoms.reverse()
sortRecom = dict(recoms)
# print(sortRecom)

# Converts ids to names
recomsWName = {}
for recommendationID in sortRecom.keys():
    if recommendationID not in idLst:
        name = GetBestName(idtoNameMap[recommendationID])
        rating = sortRecom[recommendationID]
        recomsWName[name] = rating

print(recomsWName)

# Writes Response to file
out = ""
for item in recomsWName.items():
    out = out + item[0].__str__() + ":" + item[1].__str__() + "\n"

with open('out.txt', 'w', encoding='utf-8') as file:
    file.write(out)
