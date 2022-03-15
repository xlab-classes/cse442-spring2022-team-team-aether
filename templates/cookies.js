// Will need to change this URL as we migrate to servers
const url = "http://127.0.0.1:5000/";

var xrequest = new XMLHttpRequest();

// Set website to current mode:


// xrequest.open("POST", url);
// xrequest.setRequestHeader("Accept", "application/json");
// xrequest.setRequestHeader("Content-Type", "application/json");

function submitLightOrDarkCookie() {
    // Button reads "Dark Mode" when currently in light mode and vice versa
    var switchTo = document.cookie;
    console.log(switchTo)
    var x = switchTo.split("=")
    var newthing = ""
    if (x[1] === 'Dark Mode') {
	/*TODO: Add code to put into dark mode*/
        newthing = "Light Mode"
    } else {
	/*TODO: Add code to put into light mode*/
	    newthing = "Dark Mode"
    }
    // Cookie to be sennt to server is a JSON object containing a D or L based off what mode it will be entering
    var payload = "lightOrDark" + "=" + newthing
    document.cookie = payload
    startup()
}


function startup(){
    var version = checkcookie()
    if(version == 1){
        swapStyleSheet("../static/darkstyles.css")
        //document.body.style.background = "#000000"
    }else{
        swapStyleSheet("../static/styles.css")
        //document.body.style.background = "#DFD9E2"
    }
}

function checkcookie(){
    var x = document.cookie
    console.log("checking cookie")
    var list = x.split("=")
    console.log(list[1])
    console.log("cookie status ^^")
    if(list[1] == 'Dark Mode'){
        return(1)
    }else{
        return(0)
    }
}
function swapStyleSheet(sheet) {
    document.getElementById("sheet").setAttribute("href", sheet);  
}