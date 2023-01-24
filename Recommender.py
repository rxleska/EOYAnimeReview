from cProfile import label
import math
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import false
from typing import List
from Anime import AniName, Anime, Recommendations
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime

####################################################################
############################ Settings ##############################
####################################################################

midScore = 5  # lowest score before acting as negative recommendations
isRelative = True  # round ratings to a max of 10 in a show
squareMultiples = False  # sqares multiplier for more weighted ratings
includeLargeShows = True  # includes shows over 26 episodes
includePausedAndDropped = False  # include shows that user has paused and or dropped

#####################################################################
########################### The Code ################################
#####################################################################


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


def GetAdjustedRecommendationsLevel(recs: List[Recommendations]):
    """
    Returns all recommendatiosn for a show with scores adjusted to a max of 10
    """
    highest = 0
    for rec in recs:
        if rec.rank > highest:
            highest = rec.rank
    return highest if highest != 0 else 1


# Anime Data
ani = GetAnime()

# Maps and list
recoms = {}
idtoNameMap = {}
showList = ani['COMPLETED'] if not includePausedAndDropped else [].append(
    ani['COMPLETED'], ani['DROPPED'], ani['PAUSED'])  # includes dropped and paused list
idLst = []

# if not includePausedAndDropped:
#     for show in ani['DROPPED']:
#         idLst.append(show.ids.anilist)
#     for show in ani['PAUSED']:
#         idLst.append(show.ids.anilist)

# Generates recommendation maps and id list
for show in showList:
    idLst.append(show.ids.anilist)

    # Creates Multiplier from parent show score compared to desired midpoint
    srate = show.rating.score
    multiplier = srate-midScore

    if squareMultiples:
        multiplier = multiplier * abs(multiplier)
    devisor = 1

    if isRelative:
        devisor = GetAdjustedRecommendationsLevel(show.recommendations)/10

    for recommendation in show.recommendations:
        if recommendation.numberOfEpisodes is not None and (True if not includeLargeShows else recommendation.numberOfEpisodes < 26):
            id = recommendation.id
            idtoNameMap[id] = recommendation.name  # Id to Name map

            # Ids to Recom Value
            if id not in recoms.keys():
                recoms[id] = int(math.floor(
                    (recommendation.rank*multiplier)/divisor))
            else:
                x = recoms[id]
                recoms[id] = int(
                    x + math.floor((recommendation.rank*multiplier)/divisor))

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
