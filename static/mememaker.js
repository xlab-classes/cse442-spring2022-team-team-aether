var file = document.getElementById('templates');
var filename = file.value;
var text1n = document.getElementById('FirstText');
var text1 = text1n.value;
var text2n = document.getElementById('SecondText');
var text2 = text2n.value;
const canvas = document.getElementById('meme');
const filestarter = "../generationFiles/";
const context = canvas.getContext("2d");
let image;

const textPlacement = {
    "drake":[.75, .75, 5, 5],
    "uno":[.25, .75, 3, 1.5],
    "cheating":[.25, .75, 2, 4],
    "trade":[.25, .75, 4.5, 1.37]
};
const imageLinks = {
    "drake": "../generationFiles/drake.jpg",
    "uno": "../generationFiles/uno.jpg",
    "cheating": "../generationFiles/cheating.jpg",
    "trade": "../generationFiles/trade.jpg"
};

function start(){
    var canvas = document.getElementById("meme");
    canvas.style.border = "none";
    startup();
}


function updateCanvas(canvas, image, text1, text2, file, color) {
    const width = image.width;
    const height = image.height;
    console.log(image.crossOrigin);
    console.log("image width");
    console.log(width);
    console.log("image height");
    console.log(height);
    console.log(image);

    const measures = textPlacement[file];
    console.log(measures);
    canvas.width = 225;
    canvas.height = 225;
    //document.getElementById("backup").src = image.src
    console.log("drawing image");
    context.drawImage(image, 0, 0);

    const fontSize = Math.floor(width / 15);
    const yOffset = height / 50;

    const y1 = height / measures[2];
    const y2 = height / measures[3];

    var ctx = context;

    //context.strokeStyle = "black";
    ctx.lineWidth = Math.floor(fontSize / 8);
    ctx.fillStyle = color;
    ctx.textAlign = "center";
    ctx.lineJoin = "round";
    ctx.font = `${fontSize}px sans-serif`;

    // Add top text
    ctx.textBaseline = "top";
    //ctx.strokeText(text1, 3*(width / 4), yOffset);
    ctx.fillText(text1, measures[0]*(width), y1);
    // Add bottom text
    ctx.textBaseline = "bottom";
    //ctx.strokeText(text2, 3*(width / 4), height - yOffset);
    ctx.fillText(text2, measures[1]*(width), height - y2);
    //context.drawImage("../blankmemes/drake.jpg", 0, 0);
}   

//image.addEventListener('load', imageLoaded())

function updateImage(){
    file = document.getElementById('templates');
    filename = file.value;
    text1n = document.getElementById('FirstText');
    text1 = text1n.value;
    text2n = document.getElementById('SecondText');
    text2 = text2n.value;
    textColorn = document.getElementById('TextColor');
    textColor = textColorn.value;
    console.log("updating image");
    console.log(filename);
    console.log(text1);
    console.log(text2);
    image = new Image();

   // image.crossOrigin = "use-credentials";
    image.src =  filestarter.concat(filename.concat('.jpg'));//filestarter.concat((filename.concat('.jpg')));
    //image.crossOrigin = "use-credentials";
    console.log(image.src);

    updateCanvas(canvas, image, text1, text2, filename, textColor);
}
function download() {
    //var canvas = document.getElementById("meme");
    //var ctx = canvas.getContext("2d")
    //var what = ctx.getImageData()
    //console.log(what)
    //var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream"); 
    //console.log(image)
    //var link = document.createElement('a');
    //link.download = "my-image.png";
    //link.href = image;
    //link.click();
    }
    function submitLightOrDarkCookie() {
        // Button reads "Dark Mode" when currently in light mode and vice versa
        var response = checkcookie();
        console.log(response);
        if (response == 1) {
            console.log("in dark mode, switching to light");
        /*TODO: Add code to put into dark mode*/
            newthing = "Light Mode";
        } else {
            console.log("in light mode, switching to dark");
        /*TODO: Add code to put into light mode*/
            newthing = "Dark Mode";
        }
        // Cookie to be sennt to server is a JSON object containing a D or L based off what mode it will be entering
        var payload = "lightOrDark" + "=" + newthing;
        document.cookie = payload;
        startup()
    }
    
    
    function startup(){
        var version = checkcookie();
        if(version == 1){
            swapStyleSheet("../static/darkstyles.css");
            //document.body.style.background = "#000000"
        }else{
            swapStyleSheet("../static/styles.css");
            //document.body.style.background = "#DFD9E2"
        }
    }
    
    function checkcookie(){
        var x = document.cookie;
        console.log("checking cookie");
        var list = x.split(";");
        var newlist = [];
        var holder;
        var status;
        for(i = 0; i< list.length; i++){
    
            holder = list[i].split("=");
            console.log(holder);
            if(holder[0] == " lightOrDark"){
                status = holder[1];
            }
        }
        console.log(status);
        console.log("cookie status ^^");
        if(status == 'Dark Mode'){
            return(1);
        }else{
            return(0);
        }
    }
    function swapStyleSheet(sheet) {
        document.getElementById("sheet").setAttribute("href", sheet);  
    }