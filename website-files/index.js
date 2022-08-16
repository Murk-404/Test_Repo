const express = require('express');
// const { symlinkSync } = require('fs');
const fs = require('fs')
const app = express();
app.listen(4000, () => console.log('listening at 4000'));
app.use(express.static('public'));

app.get('/user/iuawhdoiuhseoijfhneofihSEOFuh', callUser);

app.get('/top-tracks', getData);

function getData(req, res) {
  const fs = require("fs");
  // var fileName = 'C:/Spotify_Project/website-files/App_Users/' + user + '.json';
  var fileName = 'C:/Spotify_Project/website-files/App_Users/fullmtyl/_top_artists_long_term_fullmtyl.json'
  fs.readFile(fileName, "utf8", (err, jsonString) => {
    if (err) {
      console.log("File read failed:", err);
    }
    console.log("File data:", jsonString);
    // console.log(user);
  });
}


function callUser(req, res) {
  // globalThis.user = "";
  // Use child_process.spawn method from 
  // child_process module and assign it
  // to variable spawn
  var spawn = require("child_process").spawn;
    
  // Parameters passed in spawn -
  // 1. type_of_script
  // 2. list containing Path of the script
  //    and arguments for the script 
    
  // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will
  // so, first name = Mike and last name = Will
  var process = spawn('python',["./get_top_tracks.py",
                          req.query.username] );

  var user = null;

  process.stdout.on('data', function(data) {
    res.format({
      'text/html' () {
        user = (data.toString());
        console.log(user);
        const jsonString = JSON.stringify(user).slice(0,-5) + "\"";
        // const jsonString = "\"" + user + "\"";
        fs.writeFile('C:/Spotify_Project/website-files/App_Users/current_user.json', jsonString, err => {
            if (err) {
                console.log('Error writing file', err)
            } else {
                console.log('Successfully wrote file')
            }
        })
        // return Promise.resolve("IT WORKED");
        res.redirect('/top-tracks');
      }
    });
  });
  // var url = 'http://localhost:4000/user/top-data'
  // var xhttp = new XMLHttpRequest();
  // xhttp.open("GET", url, true);
  // xhttp.send();
}

// function test_lmao(){
//   var inputVal = document.getElementById("myInput").value;
//   alert(inputVal);
// }

// function test_lmao1(){
//     // function this_is_a_test(){
//   const spawner = require('child_process').spawn;

//   // SEND STRING
//   // const data_to_pass_in = 'Send this to python script';

//   // SEND ARRAY
//   // const data_to_pass_in = ['Send this to python script'];

//   // SEND JSON
//   const data_to_pass_in = {
//     data_sent: 'User_name',
//     data_returned: undefined
//   };
//   console.log('Data sent to python script: ', data_to_pass_in);
//   // \website-files\\app.js

//   const python_process = spawner('python', ['./website-files/python.py', JSON.stringify(data_to_pass_in)]);

//   python_process.stdout.on('data', (data) => {
//     console.log('Data recieved from python script: ', JSON.parse(data.toString()));
//     // alert(JSON.parse(data.toString()));
//   });
//   // }
//   // Run == node website-files/javascript.js
// }