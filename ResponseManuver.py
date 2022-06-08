from Anime import AdvancedScores, MediaIds, Rating, AniName, Anime, Progression, Rankings, ADate, AniImages, Recommendations, Character, DefiningCharacteristics, ExternalLink, ExternalMediaSet, MediaStatsDistribution, RelatedShow, Staff, Studio, Tag
from AnimeTypeGeneration import GenerateExternalLinks, GenerateRecommendations, GenerateStaffList, GenerateTagsList, Imgs2Array, Imgs2Color, AniImages, GenerateRankings, GetContentsFromPath, GenerateRelatedMedia, GenerateCharacterList, GenerateStudioList


def CreateAnimeFromEntry(ent):
    ids = MediaIds(
        GetContentsFromPath('media~id', ent),
        GetContentsFromPath('media~idMal', ent),
        GetContentsFromPath('id', ent),
        GetContentsFromPath('userId', ent),
        GetContentsFromPath('mediaId', ent)
    )
    rating = Rating(
        GetContentsFromPath('score', ent),
        AdvancedScores(
            GetContentsFromPath('advancedScores~Story', ent),
            GetContentsFromPath('advancedScores~Characters', ent),
            GetContentsFromPath('advancedScores~Visuals', ent),
            GetContentsFromPath('advancedScores~Audio', ent),
            GetContentsFromPath('advancedScores~Enjoyment', ent)
        ),
        GetContentsFromPath('media~averageScore', ent),
        GetContentsFromPath('media~meanScore', ent),
        GetContentsFromPath('media~popularity', ent),
        GetContentsFromPath('media~favourites', ent),
        GetContentsFromPath('media~isFavorite', ent),
        GenerateRankings(GetContentsFromPath('media~rankings', ent))
    )
    progression = Progression(
        ADate(
            GetContentsFromPath('completedAt~year', ent),
            GetContentsFromPath('completedAt~month', ent),
            GetContentsFromPath('completedAt~day', ent)
        ),
        GetContentsFromPath('progress', ent),
        GetContentsFromPath('repeat', ent),
        GetContentsFromPath('status', ent)
    )
    imgs = AniImages(
        Imgs2Array(GetContentsFromPath('media~coverImage', ent)),
        Imgs2Color(GetContentsFromPath('media~coverImage', ent)),
        GetContentsFromPath('media~bannerImage', ent)
    )
    name = AniName(
        GetContentsFromPath('media~title~native', ent),
        GetContentsFromPath('media~title~romaji', ent),
        GetContentsFromPath('media~title~english', ent),
        GetContentsFromPath('media~synonyms', ent),
        GetContentsFromPath('media~hashtag', ent)
    )
    recommendations = GenerateRecommendations(
        GetContentsFromPath('media~recommendations~edges', ent))
    staff = GenerateStaffList(GetContentsFromPath('media~staff~edges', ent))
    tags = GenerateTagsList(GetContentsFromPath('media~tags', ent))
    description = GetContentsFromPath('media~description', ent)
    externalMedia = ExternalMediaSet(
        GetContentsFromPath('media~trailer~site', ent),
        GetContentsFromPath('media~trailer~thumbnail', ent),
        GenerateExternalLinks(GetContentsFromPath(
            'media~externalLinks', ent))
    )
    generes = GetContentsFromPath('media~genres', ent)
    relatedMedia = GenerateRelatedMedia(
        GetContentsFromPath('media~relations~edges', ent))
    characters = GenerateCharacterList(
        GetContentsFromPath('media~characters~edges', ent))
    studios = GenerateStudioList(
        GetContentsFromPath('media~studios~edges', ent))
    siteUrl = GetContentsFromPath('media~siteUrl', ent)

    return Anime(ids, rating, progression, imgs, name, recommendations, staff, tags, description, externalMedia, generes, relatedMedia, characters, studios, siteUrl)
