import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import Header from "../components/Header";
import "../styles/ingredients.css";

export default function Ingredients() {
  const navigate = useNavigate();
  const location = useLocation();
  const persona = location.state?.persona;

  const [ingredients, setIngredients] = useState("");

  // Guard: must come from persona selection
  if (!persona) {
    navigate("/");
    return null;
  }

  function handleSubmit() {
    if (!ingredients.trim()) return;

    navigate("/confirm", {
      state: {
        persona,
        ingredients,
      },
    });
  }

  return (
    <div className="app-layout">
      {/* Header */}
      <Header onClick={() => navigate("/")} />

      {/* Main content */}
      <main className="ingredients-page">
        <h1>What are you working with today?</h1>
        <p>Type what you have and we’ll take it from there.</p>

        <input
          type="text"
          className="ingredients-input"
          placeholder="e.g. tomato, milk, pasta"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSubmit();
            }
          }}
        />
      </main>
    </div>
  );
}