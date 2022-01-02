import React from "react";
import { gql, useQuery } from "@apollo/client";
import Anime from './Anime';
import DisplayData from "./DisplayData";

// const client = new ApolloClient({
//     cache: new InMemoryCache(),
//     link: new HttpLink({
//       uri: "https://graphql.anilist.co",
//       fetchOptions: {
//         method: "POST"
//       },
//       headers: {
//         "Content-Type": "application/json",
//         Accept: "application/json"
//       }
//     })
//   });
 

//R3adyplayer2
//Awi1dbird
const GET_ALL_ANIMES = gql`
    query query{
        MediaListCollection(userName: "R3adyplayer2", type:ANIME, status:COMPLETED) {
            lists{
                entries{
                    media{
                        id
                        title{
                            romaji
                            english
                        }
                        season
                        seasonYear
                        episodes
                        duration
                        genres
                        tags{
                            id
                            name
                            rank
                        }
                        meanScore
                        popularity
                        studios{
                            nodes{
                                id
                                name
                            }
                        }
                        coverImage {
                            large
                        }
                    }
                }
            }
        }
    }
`;

// /* Randomize array in-place using Durstenfeld shuffle algorithm */
function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = array[i];
      array[i] = array[j];
      array[j] = temp;
  }
}

// function AniQueryData(){
//     const { loading, error, data} = useQuery(GET_ALL_ANIMES);

//     if (loading) return <p>Loading...</p>;
//     if (error) return <p>Error :(</p>;

//     console.log(data);

//     return data.MediaListCollection.lists[0].entries.map(({media}) => (
//         <div key={media.id}>
//             <p>
//                 {media.id}: {media.title.romaji}
//             </p>
//         </div>
//     ))
// }

function AniQuery(){
    const { loading, error, data} = useQuery(GET_ALL_ANIMES);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error :(</p>;

    // console.log(data);
    var animeList = [];

    data.MediaListCollection.lists[0].entries.forEach(element => {
        animeList.push(
            new Anime(
                element.media.id,
                (element.media.title.english !== null ? element.media.title.english:element.media.title.romaji),
                element.media.season,
                element.media.seasonYear,
                element.media.episodes,
                element.media.duration,
                element.media.genres,
                element.media.tags,
                element.media.meanScore,
                element.media.popularity,
                element.media.studios.nodes,
                element.media.coverImage.large
            ))
    });

    // console.log("oay bud look here the data be this long: " + animeList.length)
    shuffleArray(animeList);
    return <div><DisplayData dataSet={animeList}/></div>;
}

export default AniQuery;
// export default AniQueryList;
