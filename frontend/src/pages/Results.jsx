import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import Header from "../components/Header";
import "../styles/results.css";

/* Decode &amp; etc. from backend */
function decodeHtml(text) {
  const txt = document.createElement("textarea");
  txt.innerHTML = text;
  return txt.value;
}

export default function Results() {
  const navigate = useNavigate();
  const location = useLocation();

  const results = location.state?.results;
  const [copiedIndex, setCopiedIndex] = useState(null);

  if (!results || !results.suggestions) {
    navigate("/");
    return null;
  }

  return (
    <div className="app-layout">
      <Header onClick={() => navigate("/")} />

      <main className="results-page">
        <h1>Your next post is ready.</h1>
        <p className="results-subtitle">
          Based on what you have and your style.
        </p>

        <div className="suggestions-stack">
          {results.suggestions.map((item, idx) => (
            <div className="suggestion-block">
              {/* Top row: name + reasoning */}
              <div className="idea-row">
                <div className="idea-name-box gray-gradient">
                  <img
                    src="/icons/name.png"
                    className="box-icon"
                  />
                  <h2>{decodeHtml(item.dish_name)}</h2>
                </div>

                <div className="idea-reason-box">
                  <img
                    src="/icons/reasoning.png"
                    className="box-icon"
                  />
                  <p>{item.reasoning}</p>
                </div>
              </div>

              {/* Hashtags box */}
              <div className="hashtag-box">
                <div className="hashtag-list">
                  {item.hashtags.map((tag, i) => (
                    <span key={i} className="hashtag">
                      {tag}
                    </span>
                  ))}
                </div>

                <div className="copy-wrapper">
                  <button
                    className="copy-hashtags"
                    onClick={() => {
                      navigator.clipboard.writeText(item.hashtags.join(" "));
                      setCopiedIndex(idx);
                      setTimeout(() => setCopiedIndex(null), 1500);
                    }}
                  >
                    Copy hashtags
                  </button>

                  {copiedIndex === idx && (
                    <span className="copied-toast">Copied!</span>
                  )}
                </div>
              </div>

              {/* Performance */}
              <div className="performance-section">
                <p className="performance-title">Expected performance</p>

                <div className="performance-cards">
                  <div className="stat-card likes">
                    <span className="stat-label">👍 Likes</span>
                    <span className="stat-value">{item.estimated_likes}</span>
                  </div>

                  <div className="stat-card viewers">
                    <span className="stat-label">👀 Viewers</span>
                    <span className="stat-value">{item.estimated_viewers}</span>
                  </div>

                  <div className="stat-card followers">
                    <span className="stat-label">➕ Followers</span>
                    <span className="stat-value">
                      {item.estimated_followers_gained}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}