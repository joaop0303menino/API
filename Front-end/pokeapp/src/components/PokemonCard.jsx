import { Link } from "react-router-dom";

export default function PokemonCard({ pokemon }) {
  const id = pokemon.url?.split("/")[6];
  const image = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${id}.png`;

  return (
    <Link to={`/pokemon/${pokemon.name}`} className="pokemon-card">
      <img src={image} alt={pokemon.name} />
      <h3>{pokemon.name}</h3>
    </Link>
  );
}
