import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import {BounceLoader, BarLoader, BeatLoader} from 'react-spinners'
import {DisplayMapClass} from './DisplayMapClass';
const H = window.H;
function App() {
  const [isLoading, setLoading] = useState(false)
  const map = <DisplayMapClass/>
  const asyncFunc = async () => {
      
      setLoading(true);
      const response = await fetch('http://68.71.131.14:5000/test/8.8.8.8'  );
      const data = await response.json();
      for(var x in data){
        addMarker(map, x["lat"], x["lng"])
      }
      setLoading(false)
  }
  const addMarker = (map, x, y) => {
    var marker =  new H.map.Marker({"lat": x, "lng": y})
    map.addObject(marker);
  } 
return (
  <div className="App">
    { isLoading ?  
      <header className="App-header">
       
         <p>please type an ip address and when done press the button</p>
         <TextField
           sx=
             {
               {
                 input:
                 {
                   color: 'white'
                 }, root:
                 {
                   color: 'white'
                 }, floatingLabelFocusStyle:
                 {
                   color: "white"
                 }
               }
             }
             id="ipTextArea" label="Enter an  IP address" variant="filled"
          />
          <Button onClick={asyncFunc} variant="outlined">Map My Stalkers</Button>
          <BarLoader/>
       </header>

        :
       <header className="App-header">
 
           <p>please type an ip address and when done press the button</p>
           <TextField
             sx=
               { 
                { 
                   input:
                   {
                     color: 'white'
                   }, root:
                   {
                     color: 'white'
                 }, floatingLabelFocusStyle:
                  {
                     color: "white"
                   }
                 }
               }
               id="ipTextArea" label="Enter an  IP address" variant="filled"
            />
         <Button onClick={asyncFunc} variant="outlined">Map My Stalkers</Button>
         </header>
      }
   <p> <br /> </p>
  <div> {map} </div>
  </div>
);

}

export default App;
