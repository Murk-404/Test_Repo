function getInputValue1(){
    var url = 'http://localhost:4000/user/iuawhdoiuhseoijfhneofihSEOFuh'
    var xhr = new XMLHttpRequest();
    // xhr.onreadystatechange = function() {
    //     if (xhr.readyState == XMLHttpRequest.DONE) {
    //         console.log("IT HAPPENED");
    //         // var link1 = 'http://localhost:4000/user/top-data';
    //         // window.location.href = link1;
    //     }
    // }
    xhr.open('GET', url, true);
    xhr.send();
    // var xhttp = new XMLHttpRequest();
    // xhttp.open("GET", url, true);
    // xhttp.send();
    var link1 = 'http://localhost:4000/user/top-data.html';
    window.location.href = link1;
    // // print("lmao");
}
// function getInputValue2(){
    
// }