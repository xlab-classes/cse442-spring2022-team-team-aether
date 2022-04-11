var file = document.getElementById('templates');
var filename = file.value;
var text1n = document.getElementById('FirstText');
var text1 = text1n.value;
var text2n = document.getElementById('SecondText');
var text2 = text2n.value;
const canvas = document.getElementById('meme');
const filestarter = "../templates/blankmemes/"
const context = canvas.getContext("2d");
let image;

const textPlacement = {
    "drake":[.75, .75, 5, 5],
    "uno":[.25, .75, 3, 1.5],
    "cheating":[.25, .75, 2, 4],
    "trade":[.25, .75, 4.5, 1.37]
}

function updateCanvas(canvas, image, text1, text2, file, color) {
    const width = image.width;
    const height = image.height;
    console.log("image width")
    console.log(width)
    console.log("image height")
    console.log(height)
    console.log(image)

    const measures = textPlacement[file]
    console.log(measures)
    canvas.width = 225;
    canvas.height = 225;
    //document.getElementById("backup").src = image.src
    console.log("drawing image")
    context.drawImage(image, 0, 0);

    const fontSize = Math.floor(width / 15);
    const yOffset = height / 50;

    const y1 = height / measures[2];
    const y2 = height / measures[3];

    var ctx = context

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
    textColorn = document.getElementById('TextColor')
    textColor = textColorn.value;
    console.log("updating image");
    console.log(filename)
    console.log(text1)
    console.log(text2)
    image = new Image();
    
    image.src = filestarter.concat((filename.concat('.jpg')));
    console.log(image.src);

    updateCanvas(canvas, image, text1, text2, filename, textColor)
}
function download() {
    var canvas = document.getElementById("meme");
    let image = canvas.toDataURL("image/png");
    //var link = document.createElement('a');
    //link.download = "my-image.png";
    //link.href = image;
    //link.click();
    }