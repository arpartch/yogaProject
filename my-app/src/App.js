import * as R from "ramda";
import { useEffect, useState } from "react";
import "./App.css";
async function getData(url, setData) {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  setData(data);
}
function App() {
  const url = "http://127.0.0.1:5000/users/peter";
  const [data, setData] = useState();
  useEffect(() => {
    getData(url, setData);
  }, [setData]);
  console.log(data);
  if (!data) return null;
  const username = R.path(["username"], data);
  const poses = R.path(["poses"], data);
  return (
    <section>
      <ul>
        {R.map(
          pose => (
            <li>{R.prop("name", pose)} {R.prop("image", pose)}</li>
          ),
          poses
        )}
      </ul>
    </section>
  );
}
export default App;