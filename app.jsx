import { useEffect, useState } from "react";

function App() {
  const [result, setResult] = useState("Loading...");

  useEffect(() => {
    fetch("https://crime-backend.onrender.com/predict")
      .then(res => res.json())
      .then(data => setResult(data.result))
      .catch(() => setResult("Backend not reachable"));
  }, []);

  return (
    <div>
      <h1>Crime Prediction System</h1>
      <h2>{result}</h2>
    </div>
  );
}

export default App;
