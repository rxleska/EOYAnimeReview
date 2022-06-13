
def SortDict(dct):
    """
    Sorts A Dictionary from largest number value to smallest
    :param dict: Dictionary to be sorted
    :returns: Dictionary sorted
    """
    dct = sorted(dct.items(), key=lambda x: x[1])
    dct.reverse()
    return dict(dct)


def GetTopN(lst, n):
    """
    Get Top N number of items in a list or dict largest to smallest
    """
    i = n
    x = None
    if isinstance(lst, dict):
        x = dict()
        for itm in lst.items():
            x[itm[0]] = itm[1]
            i = i - 1
            if i < 1:
                return x
    else:
        x = []
        for itm in lst:
            x.append(itm)
            i = i - 1
            if i < 1:
                return x
    return x


def GenerateOptions(Ani):
    """
    Makes sets of options for tags, genres, year, and season
    """
    ret = {
        'status': {'COMPLETED',
                   'DROPPED',
                   'PLANNING',
                   'PAUSED',
                   'CURRENT'},
        'tags': set(),
        'genres': set(),
        'year': set(),
        'season': set()
    }
    opts = list(ret['status'])
    combinedList = Ani[opts[0]] + Ani[opts[1]] + \
        Ani[opts[2]] + Ani[opts[3]] + Ani[opts[4]]
    for show in combinedList:
        for tag in show.tags:
            if not tag.isAdult:
                ret['tags'].add(tag.name)
        for genre in show.genres:
            ret['genres'].add(genre)
        ret['year'].add(show.definingChars.seasonYear)
        ret['season'].add(show.definingChars.seasonPeriod)
    return ret


# def AnimeFilter(ani, filters):
#     """
#     Filters Anime to only show things that contain the filter
#     :param ani: Dict of TYPE string : Array of TYPE Anime
#     :param filters: Dict of filters from listboxes
#     :returns: Array of TYPE Anime
#     """
#     inConsideration = []
#     for i in filters['status']:
#         inConsideration = inConsideration + ani[i]

#     res = set()
#     for show in inConsideration:
#         if IsSetInSet(filters['tags'], show.GetTags()) and IsSetInSet(filters['genres'], show.genres) and IsAnySetInSet(filters['year'], show.definingChars.seasonYear.__str__()) and IsAnySetInSet(filters['season'], show.definingChars.seasonPeriod.__str__()):
#             res.add(show)

#     return res


def AnimeFilter(ani, filters, toggles):
    """
    Filters Anime to only show things that contain the filter
    :param ani: Dict of TYPE string : Array of TYPE Anime
    :param filters: Dict of filters from listboxes
    :param toggles: Dict of inclucivity toggles
    :returns: Array of TYPE Anime
    """
    inConsideration = []
    for i in filters['status']:
        inConsideration = inConsideration + ani[i]

    res = set()
    for show in inConsideration:
        if GenreAndTagToggle(show, filters, toggles) and IsAnySetInSet(filters['year'], show.definingChars.seasonYear.__str__()) and IsAnySetInSet(filters['season'], show.definingChars.seasonPeriod.__str__()):
            res.add(show)

    return res


def AniArrayToNameString(ani):
    """
    Converts Array of anime types to string of names
    :param ani: Array TYPE Anime
    :returns: string
    """
    ret = ""

    for a in ani:
        ret = ret + (a.name.english if not a.name.english == None else (
            a.name.native if not a.name.native == None else "NONE")) + " ::: "
    return ret[:-5]


def IsSetInSet(filter, mainSet):
    """
    Returns true if all parts of filter are in main set
    """
    for x in list(filter):
        if not x in mainSet:
            return False
    return True


def IsAnySetInSet(filter, mainSet):
    """
    Returns true if 1+ parts of filter are in main set
    """
    if len(filter) < 1:
        return True
    for x in list(filter):
        if x.__str__() in mainSet:
            return True
    return False


def SetToggleCheck(filter, mainSet, inclu):
    """
    :param filter: filter lists
    :param mainSet: set of things to be check against filters
    :param inclu: bool of whether to act as inclusive or excusive selection
    """
    if inclu:
        return IsAnySetInSet(filter, mainSet)
    return IsSetInSet(filter, mainSet)


def GenreAndTagToggle(show, filters, toggles):
    """
    :param show: show to test
    :param filters: dict of filter lists
    :param toggles: dict of iclusivity
    """
    isInclusive = toggles['dual']
    if isInclusive and not (len(filters['tags']) < 1 or len(filters['genres']) < 1):
        return SetToggleCheck(filters['tags'], show.GetTags(), toggles['tags']) or SetToggleCheck(filters['genres'], show.genres, toggles['genres'])
    return SetToggleCheck(filters['tags'], show.GetTags(), toggles['tags']) and SetToggleCheck(filters['genres'], show.genres, toggles['genres'])
