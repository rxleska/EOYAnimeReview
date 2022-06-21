from typing import Dict
from Anime import AdvancedScores, MediaIds, Rating, AniName, Anime, Progression, Rankings, ADate, AniImages, Recommendations, Character, DefiningCharacteristics, ExternalLink, ExternalMediaSet, MediaStatsDistribution, RelatedShow, Staff, Studio, Tag


def GetContentsFromPath(path, ent):
    pth = path.split("~")
    point = ent
    for i in pth:
        try:
            point = point[i]
        except:
            return None
    return point


def Imgs2Array(dct):
    """
    Creates an Array from the dictionary of images\n
    """
    ret = []
    try:
        for i in dct.keys():
            if not i == 'color':
                ret.append(dct[i])
    except:
        return None
    return ret


def Imgs2Color(dct):
    """
    Attepmts to get the Average Color from the Image Type\n
    """
    c = ""
    try:
        c = dct['color']
    except:
        return None
    return c


def Dict2Array(dct):
    """
    Converts Dictinary to Array of values ignoring keys\n
    """
    ret = []
    try:
        for i in dct.keys():
            ret.append(dct[i])
    except:
        return None
    return ret


def GenerateRankings(listOfEnts):
    """
    Creates a Array of Rankings\n
    :param listOfEnts: List of Rankings Elements
    :returns: Array of Rankings Objects describing Shows Ranking Catagories and rank
    """
    ret = []
    try:
        for ent in listOfEnts:
            ret.append(Rankings(
                GetContentsFromPath('id', ent),
                GetContentsFromPath('rank', ent),
                GetContentsFromPath('type', ent),
                GetContentsFromPath('format', ent),
                GetContentsFromPath('year', ent),
                GetContentsFromPath('season', ent),
                GetContentsFromPath('allTime', ent),
                GetContentsFromPath('context', ent)
            ))
    except:
        return None
    return ret


def GenerateRecommendations(arr):
    """
    Creates an Array of type Recommendations\n
    """
    ret = []
    try:
        for rec in arr:
            ret.append(Recommendations(
                GetContentsFromPath('node~rating', rec),
                GetContentsFromPath('node~mediaRecommendation~id', rec),
                AniName(
                    GetContentsFromPath(
                        'node~mediaRecommendation~title~native', rec),
                    GetContentsFromPath(
                        'node~mediaRecommendation~title~romaji', rec),
                    GetContentsFromPath(
                        'node~mediaRecommendation~title~english', rec),
                    GetContentsFromPath(
                        'node~mediaRecommendation~synonyms', rec),
                    GetContentsFromPath(
                        'node~mediaRecommendation~hashtag', rec),
                )
            ))
    except:
        return None
    return ret


def GenerateStaffList(arr):
    """
    Creates an Array of staff memebers\n
    """
    ret = []
    try:
        for i in arr:
            img = Imgs2Array(GetContentsFromPath('node~image', i))
            if len(img) > 0:
                img = img[0]
            else:
                img = None
            ret.append(Staff(
                GetContentsFromPath('role', i),
                GetContentsFromPath('node~id', i),
                GetContentsFromPath('node~name~native', i),
                GetContentsFromPath('node~name~userPreferred', i),
                img,
                GetContentsFromPath('node~description', i),
                ADate(
                    GetContentsFromPath('node~dateOfBirth~year', i),
                    GetContentsFromPath('node~dateOfBirth~month', i),
                    GetContentsFromPath('node~dateOfBirth~day', i)
                ),
                GetContentsFromPath('node~age', i)
            ))
    except:
        return None
    return ret


def GenerateTagsList(arr):
    """
    Creates an Array of Tags\n
    """
    ret = []
    try:
        for i in arr:
            ret.append(Tag(
                GetContentsFromPath('id', i),
                GetContentsFromPath('name', i),
                GetContentsFromPath('description', i),
                GetContentsFromPath('category', i),
                GetContentsFromPath('rank', i),
                GetContentsFromPath('isGeneralSpoiler', i),
                GetContentsFromPath('isMediaSpoiler', i),
                GetContentsFromPath('isAdult', i),
            ))
    except:
        return None
    return ret


def GenerateExternalLinks(arr):
    """
    Creates a list of all external links from shows page on anilist
    """
    ret = []
    try:
        for i in arr:
            ret.append(ExternalLink(
                GetContentsFromPath('url', i),
                GetContentsFromPath('site', i),
                GetContentsFromPath('type', i),
                GetContentsFromPath('icon', i)
            ))
    except:
        return None
    return ret


def GenerateRelatedMedia(arr):
    """
    Create Array of Simple TYPE RelatedShow
    """
    ret = []
    try:
        for i in arr:
            ret.append(RelatedShow(
                GetContentsFromPath('node~id', i),
                GetContentsFromPath('node~title~userPreferred', i),
                GetContentsFromPath('node~relationType', i)
            ))
    except:
        return None
    return ret


def GenerateCharacterList(arr):
    """
    Creates List of Characters TYPE Character
    """
    ret = []
    try:
        for i in arr:
            img = Imgs2Array(GetContentsFromPath('node~image', i))
            dob = GetContentsFromPath('node~dateOfBirth', i)
            if len(img) > 0:
                img = img[0]
            else:
                img = None
            ret.append(Character(
                GetContentsFromPath('role', i),
                GetContentsFromPath('node~name~full', i),
                GetContentsFromPath('node~name~native', i),
                GetContentsFromPath('node~name~userPreferred', i),
                img,
                GetContentsFromPath('node~description', i),
                ADate(
                    GetContentsFromPath('year', dob),
                    GetContentsFromPath('month', dob),
                    GetContentsFromPath('day', dob)
                ),
                GetContentsFromPath('node~age', i),
                GetContentsFromPath('node~bloodType', i),
                GetContentsFromPath('node~gender', i)
            ))
    except:
        return None
    return ret


def GenerateStudioList(arr):
    """
    Creates a List of Studios
    """
    ret = []
    try:
        for i in arr:
            ret.append(Studio(
                GetContentsFromPath('isMain', i),
                GetContentsFromPath('node~name', i),
                GetContentsFromPath('node~isAnimationStudio', i),
                GetContentsFromPath('node~siteUrl', i)
            ))
    except:
        return None
    return ret


def GenerateMediaStats(ent):
    """
    Creates a MediaStatsDistribution object for the show
    """
    scores = GetContentsFromPath("scoreDistribution", ent)
    statuss = GetContentsFromPath("statusDistribution", ent)
    scoreMap = {}
    statusMap = {}
    for score in scores:
        scoreMap[GetContentsFromPath("score", score)] = GetContentsFromPath(
            "amount", score)
    for status in statuss:
        statusMap[GetContentsFromPath("status", status)] = GetContentsFromPath(
            "amount", status)

    x = MediaStatsDistribution(
        scoreMap,
        statusMap
    )
    return x
