
query = '''
query ($name: String) { # Define which variables will be used in the query (id)
  MediaListCollection (userName: $name, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    lists{
        status
        entries{
          id
          userId
          mediaId

          score
          advancedScores

          progress
          repeat
          startedAt {
            year
            month
            day
          }
          completedAt {
            year
            month
            day
          }
          status

          media{
            id
          	idMal
            title{
              	native
                romaji
                english
            }
            type
            format
            status
            description
            endDate {
              year
              month
              day
            }
            season
            seasonYear
            seasonInt
            episodes
            duration
            countryOfOrigin
            isLicensed
            source
            hashtag
            trailer {
              site
              thumbnail
            }
            updatedAt
            coverImage {
              extraLarge
              large
              medium
              color
            }
            bannerImage
            genres
            synonyms
            averageScore
            meanScore
            popularity
            favourites
            tags {
              id
              name
              description
              category
              rank
              isGeneralSpoiler
              isMediaSpoiler
              isAdult
              
            }
            relations {
              edges {
                id
                relationType
              }
            }
            characters {
              edges {
                role
                node{
                  name {
                    full
                    native
                    userPreferred
                  }
                  image{
                    large
                    medium
                  }
                  description
                  dateOfBirth{
                    year
                    month
                    day
                  }
                  bloodType
                  gender
                  age
                  isFavourite
                  isFavouriteBlocked
                  favourites
                }
              }
            }
            staff {
              edges {
                role
                node{
                  id
                  name {
                    native
                    userPreferred
                  }
                  image {
                    large
                    medium
                  }
                  description
                  dateOfBirth {
                    year
                    month
                    day
                  }
                  age
                }
              }
            }
            studios {
              edges {
                isMain
              	node{
                  name
                  isAnimationStudio
                  siteUrl
                }
              }
            }
            isFavourite
            isAdult
            trends {
              edges {
                node {
                  averageScore
                  popularity
                  inProgress
                  episode
                }
              }
            }
            externalLinks {
              url
              site
              type
              icon
            }
            rankings {
              id
              rank
              type
              format
              year
              season
              allTime
              context
            }
            recommendations(sort:RATING_DESC){
                edges {
                    node {
                        rating
                        mediaRecommendation{
                          	id
                          	idMal
                          	type
                            title{
                                english
                                native
                              	romaji
                            }
                        }
                    }
                }
            }
            stats{
              scoreDistribution {
                score
                amount
              }
              statusDistribution {
                status
                amount
              }
            }
            siteUrl
          }
       }
    }
  }
}
'''
