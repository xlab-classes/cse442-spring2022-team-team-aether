const url = "http://127.0.0.1:5000/login";

var xrequest = new XMLHttpRequest();


xrequest.open("POST", url);
xrequest.setRequestHeader("Accept", "application/json");
xrequest.setRequestHeader("Content-Type", "application/json");


function submitdata(){
    var name = document.getElementById("username");
    var pass = document.getElementById("password");
    var payload = { "username" : name, "password" : pass };
    xrequest.send(JSON.stringify(payload));
}