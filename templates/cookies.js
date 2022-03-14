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
}


