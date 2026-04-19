import { Routes, Route } from "react-router-dom";
import PersonaSelection from "./pages/PersonaSelection";
import Ingredients from "./pages/Ingredients";
import Confirm from "./pages/Confirm";
import Results from "./pages/Results";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<PersonaSelection />} />
      <Route path="/ingredients" element={<Ingredients />} />
      <Route path="/confirm" element={<Confirm />} />
      <Route path="/results" element={<Results />} />
    </Routes>
  );
}
