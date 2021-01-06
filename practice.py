import * as R from "ramda";
import { useEffect, useState } from "react";
import "./App.css";
async function getData(url, setData) {
  const response = await fetch(url);
  const data = await response.json();
  setData(data);
}
function App() {
  const url = "http://127.0.0.1:5000/athena";
  const [data, setData] = useState();
  const poses = R.prop("poses", data);
  useEffect(() => {
    getData(url, setData);
  }, []);
  if (!data) return null;
  const username = R.path(["data", "username"], data);
  return (
    <section>
      <pre>{JSON.stringify(data, null, 2)}</pre>
      <dt>Username:</dt>
      <dd>{username}</dd>
    </section>
    <img src = "myproject/yogaPoses/pose.jpg">
    const poses = R.prop("poses", data)
    const poses = [{ name: "pose1" }, { name: "pose2" }];
    <section>
<section>
  <ul>
    {R.map(
      pose => (
        <li>{R.prop("name", pose)}</li>
      ),
      poses
    )}
  </ul>
</section>
  );
}
export default App;