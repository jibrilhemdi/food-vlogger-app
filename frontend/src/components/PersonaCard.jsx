export default function PersonaCard({ persona, selected, onSelect }) {
  return (
    <div
      className={`persona-card ${selected ? "selected" : ""}`}
      onClick={() => onSelect(persona.id)}
    >
      {/* LEFT: Text content */}
      <div className="persona-content">
        <h3 className="persona-title">{persona.title}</h3>

        <div className="persona-tags">
          {persona.tags.map((tag) => (
            <span
                key={tag}
                className="persona-tag"
                style={{
                    backgroundColor: persona.accent,
                    color: "#ffffff"
                }}
            >
                {tag}
            </span>
          ))}
        </div>

        <p className="persona-description">{persona.description}</p>
      </div>

      {/* RIGHT: Image preview */}
      <div className="persona-preview">
        <img src={persona.image} alt={persona.title} />
      </div>
    </div>
  );
}