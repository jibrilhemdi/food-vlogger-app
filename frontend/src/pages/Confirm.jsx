import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import { PERSONAS } from "../data/personas";
import LoadingOverlay from "../components/LoadingOverlay";
import Header from "../components/Header";
import "../styles/confirm.css";

export default function Confirm() {
  const navigate = useNavigate();
  const location = useLocation();

  const personaId = location.state?.persona;
  const ingredients = location.state?.ingredients;

  const [loading, setLoading] = useState(false);

  if (!personaId || !ingredients) {
    navigate("/");
    return null;
  }

  const persona = PERSONAS.find((p) => p.id === personaId);

  async function handleGenerate() {
  setLoading(true);

  try {
    const response = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        persona: personaId,
        ingredients: ingredients,
      }),
    });

    if (!response.ok) {
      throw new Error(`Backend error: ${response.status}`);
    }

    const data = await response.json();

    console.log("✅ Backend response:", data);

    navigate("/results", {
      state: {
        results: data,
        persona: personaId,
        ingredients,
      },
    });
  } catch (error) {
    console.error("❌ Generation failed:", error);
    setLoading(false);
    alert("Something went wrong. Please try again.");
  }
}

  return (
    <>
        {loading && <LoadingOverlay />}
        <div className="app-layout">
        {/* Header */}
        <Header onClick={() => navigate("/")} />

        {/* Main */}
        <main className="confirm-page">
            <h1>Ready to create your next post?</h1>
            <p className="confirm-subtitle">
                Here’s what we’ll use to generate your content.
            </p>

            <div className="confirm-card">
            {/* Left: image */}
            <div className="confirm-image">
                <img src={persona.image} alt={persona.title} />
            </div>

            {/* Right: details */}
            <div className="confirm-details">
                <h3>{persona.title}</h3>
                <p>
                {persona.description}
                </p>

                <div className="confirm-ingredients">
                <span className="label">Ingredients</span>
                {ingredients.split(",").map((item, idx) => (
                    <div key={idx} className="ingredient-item">
                    {item.trim()}
                    </div>
                ))}
                </div>
            </div>
            </div>

            {/* Actions */}
            <div className="confirm-actions">
            <button
                className="secondary"
                disabled={loading}
                onClick={() =>
                navigate("/ingredients", {
                    state: { persona: personaId },
                })
                }
            >
                Make changes
            </button>

            <button
                className="primary"
                disabled={loading}
                onClick={handleGenerate}
            >
                {loading ? "Generating…" : "Generate my content"}
            </button>
            </div>
        </main>
        </div>
    </>
  );
}