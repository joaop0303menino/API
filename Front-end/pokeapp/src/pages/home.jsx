import { useEffect, useState } from "react";
import { getPokemons, getPokemonByName } from "../api/api.js";
import PokemonCard from "../components/PokemonCard";
import SearchBar from "../components/SearchBar";

export default function Home() {
  const [pokemons, setPokemons] = useState([]);
  const [searchedPokemon, setSearchedPokemon] = useState(null);
  const [offset, setOffset] = useState(0);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadMorePokemons();
    // eslint-disable-next-line
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      if (
        window.innerHeight + document.documentElement.scrollTop + 100 >=
        document.documentElement.scrollHeight
      ) {
        loadMorePokemons();
      }
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, [offset]);

  const loadMorePokemons = async () => {
    if (loading) return;
    setLoading(true);
    const data = await getPokemons(50, offset);
    setPokemons((prev) => [...prev, ...data]);
    setOffset((prev) => prev + 50);
    setLoading(false);
  };

  const handleSearch = async (name) => {
    try {
      const data = await getPokemonByName(name);
      setSearchedPokemon({
        name: data.name,
        url: `https://pokeapi.co/api/v2/pokemon/${data.id}/`,
      });
    } catch {
      alert("Pokémon não encontrado!");
    }
  };

  return (
    <div className="container">
      <h1>Pokédex</h1>
      <SearchBar onSearch={handleSearch} />

      {searchedPokemon ? (
        <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
          <PokemonCard pokemon={searchedPokemon} />
        </div>
      ) : (
        <div className="pokemon-grid">
          {pokemons.map((p) => (
            <PokemonCard key={p.name} pokemon={p} />
          ))}
        </div>
      )}

      {loading && <p style={{ textAlign: "center", marginTop: "20px" }}>Carregando...</p>}
    </div>
  );
}
