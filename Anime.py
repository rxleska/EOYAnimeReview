from operator import index
from tokenize import String
from typing import List, Dict
from multiprocessing.dummy import Array
from enum import Enum
from winreg import EnumKey, EnumValue
from xmlrpc.client import boolean

from torch import are_deterministic_algorithms_enabled


def Arr2Str(a):
    x = ""
    for i in a:
        x = x + " " + i.__str__()
    return x


class AnimeSelection(Enum):
    """Defines 5 sub lists from anilist as an Enum"""
    COMPLETED = 'COMPLETED'
    DROPPED = 'DROPPED'
    PLANNING = 'PLANNING'
    PAUSED = 'PAUSED'
    CURRENT = 'CURRENT'


def AnimeSelectionByIndex(index):
    switch = {
        1: AnimeSelection.COMPLETED,
        2: AnimeSelection.DROPPED,
        3: AnimeSelection.PLANNING,
        4: AnimeSelection.PAUSED,
        5: AnimeSelection.CURRENT
    }
    return (AnimeSelection.COMPLETED if not index in switch.keys() else switch[index])


class Anime:
    """The Anime Class contains all the information of an anime"""

    def __init__(self, i, r, p, aimg, n, rec, stf, tgs, des, ems, gen, rel, chars, sdos, surl, defc):
        """
        The Anime Class contains all the information of an anime\n
        :param i: Media Ids object containing the main entrys ids: TYPE MediaIds :
        :param r: Ratings and Scores: TYPE Rating :
        :param p: Progression Data: TYPE Progression :
        :param aimg: Cover and Banner Images: TYPE AniImages :
        :param n: Collection of Names: TYPE AniName :
        :param rec: Recommendations: TYPE Array of TYPE Recommendations:
        :param stf: Staff : TYPE Array of TYPE Staff:
        :param tgs: Tags : TYPE Array of TYPE Tag:
        :param des: Description (media description)
        :param ems: Trailer and External links: TYPE ExternalMediaSet:
        :param gen: Generes : TYPE Array of TYPE String : (media genres)
        :param rel: Related Media: TYPE Array of TYPE RelatedShow
        :param chars: Characters: TYPE Array of TYPE Character
        :param sdos: Studios: TYPE Array of TYPE Studio
        :param surl: Site Url of Anime Entry (media siteUrl)
        :param defc: Defining Characteristics : Type DefiningCharacteristics 
        """
        self.ids: MediaIds
        self.rating: Rating
        self.progression: Progression
        self.img: AniImages
        self.name: AniName
        self.recommendations: List[Recommendations]
        self.staff: List[Staff]
        self.tags: List[Tag]
        self.description: str
        self.externalMedia: ExternalMediaSet
        self.genres: List[str]
        self.relatedMedia: List[RelatedShow]
        self.characters: List[Character]
        self.studios: List[Studio]
        self.siteUrl: str
        self.definingChars: DefiningCharacteristics

        self.ids = i
        self.rating = r
        self.progression = p
        self.imgs = aimg
        self.name = n
        self.recommendations = rec
        self.staff = stf
        self.tags = tgs
        self.description = des
        self.externalMedia = ems
        self.genres = gen
        self.relatedMedia = rel
        self.characters = chars
        self.studios = sdos
        self.siteUrl = surl
        self.definingChars = defc

    def __str__(self):
        return "IDS: " + self.ids.__str__() + "\n\nRatings:" + self.rating.__str__() + "\n\nProgress:" + self.progression.__str__() + "\n\nImg:" + self.imgs.__str__() + "\n\nName:" + self.name.__str__() + "\n\nRecom:" + Arr2Str(self.recommendations) + "\n\nStaff:" + Arr2Str(self.staff) + "\n\nTags:" + self.tags.__str__() + "\n\nDesc:" + self.description.__str__() + "\n\nExternalMedia:" + self.externalMedia.__str__() + "\n\nGenres" + self.genres.__str__() + "\n\nrelated:" + self.relatedMedia.__str__() + "\n\nChars:" + Arr2Str(self.characters) + "\n\nStudios:" + Arr2Str(self.studios) + "\n\nSiteUrl:" + self.siteUrl.__str__() + "defc:" + self.definingChars.__str__()

    def GetTags(self):
        """
        Returns set of all tag names
        """
        ret = set()
        for i in self.tags:
            ret.add(i.name)
        return ret


class MediaIds:
    """Contains Ids from both anilist and MAL"""

    def __init__(self, a, m, ei, eu, em):
        """
        Contains Ids from both anilist and MAL\n
        :param a: Anilist ID (Media ID)
        :param m: My Anime List ID (Media malId)
        :param ei: entry Id (Entry id)
        :param eu: entry UserId (Entry userId)
        :param em: entry MediaId (Entry mediaId)
        """
        self.anilist: str
        self.MAL: str
        self.entryId: str
        self.entryUserId: str
        self.entryMediaId: str

        self.anilist = a
        self.MAL = m
        self.entryId = ei
        self.entryUserId = eu
        self.entryMediaId = em

    def __str__(self):
        return "ani ID:" + self.anilist.__str__() + " MALid:" + self.MAL.__str__() + " Eid:" + self.entryId.__str__() + " EUid:" + self.entryUserId.__str__() + " EMid:" + self.entryMediaId.__str__()


class Rating:
    """Contains the Different Scores and Ratings"""

    def __init__(self, s, advs, avs, ms, p, f, isf, rks, medStat):
        """
        Contains the Different Scores and Ratings\n
        :param s: Score (Entry score)
        :param advs: AdvancedScore (Entry advancedScores): TYPE AdancedScores Object:
        :param avs: Average Score (Media averageScore)
        :param ms: Mean Score (Media meanScore)
        :param p: Populatrity (Media popularity)
        :param f: Number Of Favorites (Media favourites)
        :param isf: isFavorite (media isFavorite)
        :param rks: Rankings its in (media rankings): TYPE Array of TYPE Ranking : 
        :param medStat: Media Stats : Type MediaStatsDistribution
        """
        self.score: float
        self.advancedScore: AdvancedScores
        self.averageScore: float
        self.meanScore: float
        self.popularity: int
        self.favorites: int
        self.isFavorite: bool
        self.rankings: List[Rankings]
        self.mediaStats: MediaStatsDistribution

        self.score = s
        self.advancedScore = advs
        self.averageScore = avs
        self.meanScore = ms
        self.popularity = p
        self.favorites = f
        self.isFavorite = isf
        self.rankings = rks
        self.mediaStats = medStat

    def __str__(self):
        return "score:" + self.score.__str__() + " AdvScore:" + self.advancedScore.__str__() + " aveScore:" + self.averageScore.__str__() + " meanScore:" + self.meanScore.__str__() + " pop:" + self.popularity.__str__() + " favorites:" + self.favorites.__str__() + " Rankings:" + Arr2Str(self.rankings)


class AdvancedScores:
    """Advanced Score Catagories"""

    def __init__(self, s, c, v, a, e):
        """
        Advanced Score Catagories\n
        :param s: Story Score (Entry advancedScores Story)
        :param c: Character Score (Entry advancedScores Characters)
        :param v: Visuals Score (Entry advancedScores Visuals)
        :param a: Audio Score (Entry advancedScores Audio)
        :param e: Enjoyment Score (Entry advancedScores Enjoyment)
        """
        self.story: float
        self.character: float
        self.visuals: float
        self.audio: float
        self.enjoyment: float

        self.story = s
        self.character = c
        self.visuals = v
        self.audio = a
        self.enjoyment = e

    def __str__(self):
        return "story:" + self.story.__str__() + " character:" + self.character.__str__() + " visuals:" + self.visuals.__str__() + " audio:" + self.audio.__str__() + " enjoyment:" + self.enjoyment.__str__()


class MediaStatsDistribution:
    """Media Statistics on distibution of scores"""

    def __init__(self, scr, stus):
        """
        Media Statistics on distibution of scores\n
        :param scr: Score Distribution map, {score, amount}
        :param stus: Status Distribution map, {status, amount}
        """
        self.scoreDistribution: dict
        self.statusDistribution: dict

        self.scoreDistribution = scr
        self.statusDistribution = stus

    def __str__(self):
        return "Scores:" + self.statusDistribution.__str__() + "\n" + "Statuss:" + self.statusDistribution.__str__()


class Progression:
    """Defines All Parameters of Progression"""

    def __init__(self, f, p, r, s):
        """
        Defines All Parameters of Progression\n
        :param f: finished Date: TYPE ADate :
        :param p: Progression (Entry progress)
        :param r: Times Repeated (Entry repeat)
        :param s: Status (Entry status)
        """
        self.finished: ADate
        self.progress: str
        self.timesRepeated: int
        self.status: str

        self.finished = f
        self.progress = p
        self.timesRepeated = r
        self.status = s

    def __str__(self):
        return "finished:" + self.finished.__str__() + " progress:" + self.progress.__str__() + " timesRepeated:" + self.timesRepeated.__str__() + " status:" + self.status.__str__()


class ADate:
    """Object containing the anilist date type"""

    def __init__(self, y, m, d):
        """
        Object containing the anilist date type\n
        :param y: year (completedAt year)
        :param m: month (completedAt month)
        :param d: day (completedAt day)
        """
        self.year: int
        self.month: int
        self.day: int

        self.year = y
        self.month = m
        self.day = d

    def __str__(self):
        return "Date:" + self.month.__str__() + "/" + self.day.__str__() + "/" + self.year.__str__()


class AniImages:
    """Collection of Images/Banners from the anime"""

    def __init__(self, ci, cic, b):
        """
        Collection of Images/Banners from the anime\n
        :param ci: coverImage Array inOrder of size of image urls (media coverImage)
        :param cic: coverImageColor: Hex of average color in cover (media coverImage)
        :param b: Banner Image (media bannerImage)
        """
        self.coverImage: List[str]
        self.coverImageColor: str
        self.banner: str

        self.coverImage = ci
        self.coverImageColor = cic
        self.banner = b

    def __str__(self):
        return "coverimgurl:" + self.coverImage.__str__() + " coverColor:" + self.coverImageColor.__str__() + " bannerurl:" + self.banner.__str__()


class AniName:
    """Collect of all defining Titles and Names"""

    def __init__(self, tn, tr, te, s, ht):
        """
        Collect of all defining Titles and Names\n
        :param tn: Title Native (media title native)
        :param tr: Title Romaji (media title romaji)
        :param te: Title English (media title english)
        :param s: Synonyms for the shows Name (media synonyms): TYPE Array:
        :param ht: hashtag (media hashtag)
        """
        self.native: str
        self.romaji: str
        self.english: str
        self.synonyms: List[str]
        self.hashtag: str

        self.native = tn
        self.romaji = tr
        self.english = te
        self.synonyms = s
        self.hashtag = ht

    def __str__(self):
        return "NameNative:" + self.native.__str__() + " NameRomaji:" + self.romaji.__str__() + " NameEng:" + self.english.__str__() + " Synonyms:" + self.synonyms.__str__() + " hashtag:" + self.hashtag.__str__()


class DefiningCharacteristics:
    """Collection of characteristics like season, type, and country of origin"""

    def __init__(self, sy, s, sn, t, f, st, fa, coo, ne, de, sc, ia, il):
        """
        Collection of characteristics like season, type, and country of origin\n
        :param sy: Season Year (media seasonYear)
        :param s: Season (media season)
        :param sn: Season Number (media seasonInt)
        :param t: Type (media type)
        :param f: Format (media format)
        :param st: Airing Status (media status)
        :param fa: Date Finished Airing (media endDate): TYPE ADate :
        :param coo: Country of Origin (media countryOfOrigin)
        :param ne: Number of Episodes (media episodes)
        :param de: Average Duration of Episodes (media duration)
        :param sc: Source of Shows Story (media source)
        :param ia: isAdult (media isAdult) 
        :param il: isLicensed (media isLicensed)
        """
        self.seasonYear: int
        self.seasonPeriod: str
        self.seasonNumber: str
        self.type: str
        self.format: str
        self.airingStatus: str
        self.finishedAiringAt: ADate
        self.countryOfOrigin: str
        self.numberOfEpisodes: int
        self.duration: int
        self.source: str
        self.isAdult: bool
        self.isLicensed: bool

        self.seasonYear = sy
        self.seasonPeriod = s
        self.seasonNumber = sn
        self.type = t
        self.format = f
        self.airingStatus = st
        self.finishedAiringAt = fa
        self.countryOfOrigin = coo
        self.numberOfEpisodes = ne
        self.duration = de
        self.source = sc
        self.isAdult = ia
        self.isLicensed = il

    def __str__(self):
        return "SeasonYear:" + self.seasonYear.__str__() + " SeasonPeriod:" + self.seasonPeriod.__str__() + " SeasonNumber:" + self.seasonNumber.__str__() + " Type:" + self.type.__str__() + " Format:" + self.format.__str__() + " AiringStatus" + self.airingStatus.__str__() + " finishedAiringAt:" + self.finishedAiringAt.__str__() + " CountryOfOrigin:" + self.countryOfOrigin.__str__() + " NumEps:" + self.numberOfEpisodes.__str__() + " Duration:" + self.duration.__str__() + " sauce:" + self.source.__str__() + " isAdult" + self.isAdult.__str__() + " isLicensed" + self.isLicensed.__str__()


class Rankings:
    """Rankings seperated by Catagories"""

    def __init__(self, i, r, t, f, y, s, a, c):
        """
        Rankings seperated by Catagories\n
        :param i: ID of Ranking Definition (media rankings id)
        :param r: Rank in Ranking (media rankings rank)
        :param t: Type defined in ranking (media rankings type)
        :param f: Format defined in ranking (media rankings format)
        :param y: Year defined in ranking (media rankings year)
        :param s: Season defined in ranking (media rankings season)
        :param a: is Rankings on the bases of rank of all time (media rankings allTime)
        :param c: context of the basis of the rankings (media rankings context)
        """
        self.id: int
        self.rank: str
        self.type: str
        self.format: str
        self.year: str
        self.season: str
        self.isOfAllTime: bool
        self.context: str

        self.id = i
        self.rank = r
        self.type = t  # null means rating is not by type
        self.format = f  # null means rating is not by format
        self.year = y  # null means rating is not by year
        self.season = s  # null means rating is not by season
        self.isOfAllTime = a  # defines if rating is in place of all time
        self.context = c  # defines context

    def __str__(self):
        return "rID:" + self.id.__str__() + " rnk:" + self.rank.__str__() + " type:" + self.type.__str__() + " format:" + self.format.__str__() + " year:" + self.year.__str__() + " season:" + self.season.__str__() + " isOfAllTime" + self.isOfAllTime.__str__() + " context:" + self.context.__str__()


class Recommendations:
    """Recommendation Show and Rating"""

    def __init__(self, r, i, n, s, ne, iA, g):
        """
        Recommendation Show and Rating\n
        :param r: Rating of how many people recommended the show (media recommendations edges node rating)
        :param i: id of media (media recommendations edges node mediaRecommendation id)
        :param n: Title of recommended Media: TYPE AniName :(media recommendations edges node mediaRecommendation)
        :param s: Status of User for the show (media recommendations edges node mediaRecommendation status)
        :param ne: Number of Episodes in the show (media recommendations edges node mediaRecommendation episodes)
        :param iA: is show Adult (media recommendations edges node mediaRecommendation isAdult)
        :param g: Genres List (media recommendations edges node mediaRecommendation genres)
        """
        self.rank: int
        self.id: int
        self.name: AniName
        self.status: str
        self.numberOfEpisodes: int
        self.isAdult: bool
        self.genres: List[str]

        self.rank = r
        self.id = i
        self.name = n
        self.status = s
        self.numberOfEpisodes = ne
        self.isAdult = iA
        self.genres = g

    def __str__(self):
        return "rnk:" + self.rank.__str__() + " id:" + self.id.__str__() + " name:" + self.name.__str__()


class Staff:
    """Major Staff From Anime"""

    def __init__(self, r, i, nn, upn, iu, des, dob, a):
        """
        Major Staff From Anime\n
        :param r: Role of Staff (staff edges role)
        :param i: id of staff (staff edges node id)
        :param nn: Native Name of Staff (staff edges node name native)
        :param upn: User Preferred Name of Staff Member (staff edges node name userPreferred)
        :param iu: URL Largest Image available of Staff Member (staff edges node image large or medium)
        :param des: Description of Staff (staff edges node description)
        :param dob: Date of Birth of Staff Member: TYPE ADate (staff edges node dateOfBirth)
        :param a: Age of Staff Member (staff edges node age)
        """
        self.role: str
        self.id: int
        self.nameNative: str
        self.namePrefered: str
        self.image: str
        self.description: str
        self.dateOfBirth: ADate
        self.age: int

        self.role = r
        self.id = i
        self.nameNative = nn
        self.namePrefered = upn
        self.image = iu
        self.description = des
        self.dateOfBirth = dob
        self.age = a

    def __str__(self):
        return "role:" + self.role.__str__() + " id:" + self.id.__str__() + " nameNative:" + self.nameNative.__str__() + " namePref:" + self.namePrefered.__str__() + " imgurl:" + self.image.__str__() + " des:" + self.description.__str__() + " dob:" + self.dateOfBirth.__str__() + " age:" + self.age.__str__()


class Tag:
    """Show Tags"""

    def __init__(self, i, n, des, cat, r, iGS, iMS, iA):
        """
        Show Tags\n
        :param i: Tag id (media tags id)
        :param n: Tag Name (media tags name)
        :param des: Tag Description (media tags description)
        :param cat: Tag Category (media tags category) 
        :param r: Tag Ranking (media tags rank)
        :param iGS: is the Tag a General Spoiler (media tags isGeneralSpoiler)
        :param iMS: is the Tag a Spoiler of the Media (media tags isMediaSpoiler)
        :param iA: is the Tag recognised as Adult (media tags isAdult)
        """
        self.id: int
        self.name: str
        self.description: str
        self.category: str
        self.ranking: int
        self.isGeneralSpoiler: bool
        self.isMediaSpoiler: bool
        self.isAdult: bool

        self.id = i
        self.name = n
        self.description = des
        self.category = cat
        self.ranking = r
        self.isGeneralSpoiler = iGS
        self.isMediaSpoiler = iMS
        self.isAdult = iA

    def __str__(self):
        return "id:" + self.id.__str__() + " name:" + self.name.__str__() + " des:" + self.description.__str__() + " cate:" + self.category.__str__() + " rnk:" + self.ranking.__str__() + " iGS:" + self.isGeneralSpoiler.__str__() + " iMS:" + self.isMediaSpoiler.__str__() + " isAdult" + self.isAdult.__str__()


class ExternalMediaSet:
    """External Media such as trailer and external links"""

    def __init__(self, tu, tt, els):
        """
        External Media such as trailer and external links\n
        :param tu: Trailer URL (media trailer site)
        :param tt: Trailer Thumbnail (media trailer thumbnail)
        :param els: Array of external links: TYPE Array of TYPE ExternalLink
        """
        self.trailer: str
        self.trailerThumbnail: str
        self.externalLinks: List[ExternalLink]

        self.trailer = tu
        self.trailerThumbnail = tt
        self.externalLinks = els

    def __str__(self):
        return "trailerUrl:" + self.trailer.__str__() + " trailerTNUrl" + self.trailerThumbnail.__str__() + " externalLnks:" + self.externalLinks.__str__()


class ExternalLink:
    """External Link for the type media"""

    def __init__(self, u, s, t, i):
        """
        External Link for the type media\n
        All items are from (media externalLinks)
        :param u: URL of External Link (url)
        :param s: Site Title (site)
        :param t: Type of  Link (type)
        "param i: Icon of site (icon)
        """
        self.url: str
        self.site: str
        self.type: str
        self.icon: str

        self.url = u
        self.site = s
        self.type = t
        self.icon = i

    def __str__(self):
        return "url:" + self.url.__str__() + " site:" + self.site.__str__() + " type:" + self.type.__str__() + " icon" + self.icon.__str__()


class RelatedShow:
    """Media Related to base show"""

    def __init__(self, i, t, r):
        """
        Item of Content Related to base show\n
        :param i: ID of content (media relations edges node id)
        :param t: Title of the content (media relations edges node title userPreferred)
        :param r: Relation Type (media relations edges relationType)
        """
        self.id: int
        self.title: str
        self.relationship: str

        self.id = i
        self.title = t
        self.relationship = r

    def __str__(self):
        return "id:" + self.id.__str__() + " title:" + self.title.__str__() + " relation:" + self.relationship.__str__()


class Character:
    """Defines Character Type used to describe charcters in a show"""

    def __init__(self, r, fn, nn, upn, img, des, dob, a, bt, g, iF, nF, iFb):
        """
        Defines Character Type used to describe charcters in a show\n
        :param r: Role of Character (media characters edges role)
        :param fn: Full Name (media characters edges node name full)
        :param nn: Native Name (media characters edges node name native)
        :param upn: User Prefered Name (media characters edges node name userPreferred)
        :param img: Largest Image of Character (media characters edges node image large/medium)
        :param des: Description (media characters edges node description)
        :param dob: Date of Birth (media characters edges node dateOfBirth) : Type ADate
        :param a: Age (media characters edges node age)
        :param bt: Blood Type if Available (media characters edges node bloodType)
        :param g: Gender (media characters edges node gender)
        :param iF: is Character favorited by user (media characters edges node isFavorite)
        :param nF: Number of users whom have favorited (media characters edges node favorites) 
        :param iFb: is Character blocked from being favorited? (media characters edges node isFavoriteBlocked)
        """
        self.role: str
        self.fullName: str
        self.nativeName: str
        self.userPreferedName: str
        self.image: str
        self.description: str
        self.birthday: ADate
        self.age: int
        self.bloodType: str
        self.gender: str
        self.isFavorite: bool
        self.numFavorite: int
        self.isFavoriteBlocked: bool

        self.role = r
        self.fullName = fn
        self.nativeName = nn
        self.userPreferedName = upn
        self.image = img
        self.description = des
        self.birthday = dob
        self.age = a
        self.bloodType = bt
        self.gender = g
        self.isFavorite = iF
        self.numFavorite = nF
        self.isFavoriteBlocked = iFb

    def __str__(self):
        return "\n" + self.fullName.__str__() + " aka " + self.nativeName.__str__() + " is a " + self.role.__str__() + " that is " + self.age.__str__() + " and type " + self.bloodType.__str__() + "blood type.\n" + "Des:" + self.description.__str__() + "dob:" + self.birthday.__str__() + "gender:" + self.gender.__str__() + "imgurl:" + self.image.__str__()


class Studio:
    """Studio Object containing defining information"""

    def __init__(self, im, n, iAS, sU):
        """
        Studio Object containing defining information\n
        :param im: isMain (media studios edges isMain)
        :param n: Name of Studio (media studios edges node name)
        :param iAS: isAnimationStudio (media studios edges node isAnimationStudio)
        :param sU: site URL (media studios edges node siteUrl)
        """
        self.isMain: bool
        self.name: str
        self.isAnimationStudio: bool
        self.url: str

        self.isMain = im
        self.name = n
        self.isAnimationStudio = iAS
        self.url = sU

    def __str__(self):
        return ("Main Studio" if self.isMain.__str__() == 'True' else "not Main studio") + " named:" + self.name.__str__() + " and " + ("is an animation studio" if self.isAnimationStudio.__str__() == "True" else "is not an animation studio") + " url:" + self.url.__str__()
