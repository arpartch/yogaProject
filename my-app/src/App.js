import * as R from "ramda";
import { useEffect, useState } from "react";
import "./App.css";
import styled from "styled-components"
async function getData(url, setData) {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  setData(data);
}
function App() {
  const baseUrl = "https://athena-peter-yoga-pose-project.s3-us-west-2.amazonaws.com";
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
    <Style>
      <ul>
        {R.map(
          pose => {
            const src = `${baseUrl}/${R.prop("image", pose)}`
            console.log(src)
            return (
            <li>
              <p>
              {R.prop("name", pose)} 
              </p>
              <div>
              <img src={src} width='200px' height='350px'/>
              </div>
              </li>)
          },
          poses
        )}
      </ul>
    </Style>
  );
}
export default App;
/*
remove bullets - done
outline the cards - done
give the cards a width and height - done
give cards a drop shadow - done
add flexbox to wrap cards - done
give the ul a max width - done
center the name - done
put the name at the top of the card
*/
const Style = styled.section`
color: blue;
ul {list-style-type: none;
    display: flex;
    width: 150px
    outline: 1px solid black;
    flex-wrap: wrap;
  }
li {outline: 5px solid green;
    margin: 25px 25px 30px 30px;
    box-shadow: 8px 8px 5px #888888;
    p{text-align: center;
      margin: 0;}
  }
  
img {
  max-width:100%;
  height:auto;
}
`