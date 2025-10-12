import axios from "axios";

const api = axios.create({
  baseURL: "https://pokeapi.co/api/v2/"
});

export const getPokemons = async (limit = 3000, offset = 0 ) => {
  const response = await api.get(`pokemon?limit=${limit}&offset=${offset}`);
  return response.data.results;
};

export const getPokemonByName = async (name) => {
  const response = await api.get(`pokemon/${name.toLowerCase()}`);
  return response.data;
};

export default api;
