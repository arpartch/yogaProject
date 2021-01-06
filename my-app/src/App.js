

import logo from "./logo.svg";
import "./App.css";
async function getData() {
  const response = await fetch("http://127.0.0.1:5000/peter");
  return await response.json();
}
function App() {
  const data = getData();
  console.log("data:", data);
  return <div>athena</div>;
}
export default App;