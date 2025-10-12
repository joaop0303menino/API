import { useState } from "react";

export default function SearchBar({ onSearch }) {
  const [value, setValue] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim()) {
      onSearch(value);
      setValue("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="search-bar">
      <input
        type="text"
        placeholder="Buscar Pokémon..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <button type="submit">Buscar</button>
    </form>
  );
}
