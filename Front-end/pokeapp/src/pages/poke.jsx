import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { getPokemonByName } from "../api/api.js";

export default function PokemonDetails() {
  const { name } = useParams();
  const [pokemon, setPokemon] = useState(null);

  useEffect(() => {
    const fetchPokemon = async () => {
      const data = await getPokemonByName(name);
      setPokemon(data);
    };
    fetchPokemon();
  }, [name]);

  if (!pokemon) return <p style={{ textAlign: "center", marginTop: "30px" }}>Carregando...</p>;

  return (
    <div className="details-container">
      <Link to="/" className="back-link">← Voltar</Link>

      <img src={pokemon.sprites.other["official-artwork"].front_default} alt={pokemon.name} />
      <h2>{pokemon.name}</h2>

      <p><strong>Altura:</strong> {pokemon.height / 10} m</p>
      <p><strong>Peso:</strong> {pokemon.weight / 10} kg</p>
      <p><strong>Tipos:</strong> {pokemon.types.map((t) => t.type.name).join(", ")}</p>
      <p><strong>Habilidades:</strong> {pokemon.abilities.map((a) => a.ability.name).join(", ")}</p>
    </div>
  );
}
