// import logo from './logo.svg';
import './App.css';
import { ApolloClient, HttpLink, InMemoryCache, ApolloProvider} from "@apollo/client"
import AniQuery from './AniQuery';

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "https://graphql.anilist.co",
    fetchOptions: {
      method: "POST"
    },
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    }
  })
});

function App() {
  return (
    <div className="App">
      <ApolloProvider client={client}>
        <AniQuery client={client}/>
      </ApolloProvider>
    </div>
  );
}

export default App;
