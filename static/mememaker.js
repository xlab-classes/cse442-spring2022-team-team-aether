const file = document.getElementById('templates');
const filename = file.value;
const text1n = document.getElementById('FirstText');
const text1 = text1n.value;
const text2n = document.getElementById('SecondText');
const text2 = text2n.value;
const canvas = document.getElementById('meme');
const filestarter = "../templates/blankmemes/"
let image;

function updateCanvas(canvas, image, text1, text2) {
    const context = canvas.getContext("2d");
    const width = image.width;
    const height = image.height;
    console.log("image width")
    console.log(width)
    console.log("image height")
    console.log(height)
    console.log(image)


    canvas.width = width;
    canvas.height = height;
    //const backup = document.getElementById("backup")
    //backup.src = image.src
    context.drawImage("../templates/blankmemes/drake.jpg", 0, 0);
    //context.drawImage("../blankmemes/drake.jpg", 0, 0);
}   

function updateImage(){
    console.log("updating image");
    console.log(filename)
    console.log(text1)
    console.log(text2)
    image = new Image();
    
    image.src = filestarter.concat((filename.concat('.jpg')));
    console.log(image.src);

    updateCanvas(canvas, image, text1, text2)
}