import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { PERSONAS } from "../data/personas";
import PersonaCard from "../components/PersonaCard";
import Header from "../components/Header";
import "../styles/persona.css";

export default function PersonaSelection() {
  const [selectedPersona, setSelectedPersona] = useState(null);
  const navigate = useNavigate();

  return (
    <div className="app-layout">
      {/* ✅ Header */}
      <Header onClick={() => navigate("/")} />

      {/* ✅ Page content */}
      <div className="persona-page">
        <h1>What kind of food creator are you?</h1>
        <p>Pick the style that fits your feed.</p>

        <div className="persona-grid">
          {PERSONAS.map((persona) => (
            <PersonaCard
              key={persona.id}
              persona={persona}
              onSelect={(id) => {
                setSelectedPersona(id);
                navigate("/ingredients", {
                    state: { persona: id },
                });
              }}
            />
          ))}
        </div>
      </div>
    </div>
  );
}