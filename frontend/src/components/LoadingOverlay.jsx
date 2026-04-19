import { useEffect, useState } from "react";
import "../styles/loading.css";

const STEPS = [
  {
    text: "Analyzing your ingredients...",
    image: "/loading/cook.png",
  },
  {
    text: "Matching your creator style...",
    image: "/loading/egg.png",
  },
  {
    text: "Designing your next post...",
    image: "/loading/coffee.png",
  },
];

export default function LoadingOverlay() {
  const [step, setStep] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setStep((prev) => (prev + 1) % STEPS.length);
    }, 1500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="loading-overlay">
      <div className="app-header">
        <div className="header-inner">
          <span className="app-logo">FeedChef</span>
        </div>
      </div>

      <div className="loading-content">
        <p className="loading-text">{STEPS[step].text}</p>
        <img
          src={STEPS[step].image}
          alt="Loading illustration"
          className="loading-image"
        />
      </div>
    </div>
  );
}