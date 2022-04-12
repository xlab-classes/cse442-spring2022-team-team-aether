from PIL import Image, ImageDraw, ImageFont


textLocations = {
    "drake":[.7, .7, 5, 1.5],
    "uno":[.25, .75, 3, 7],
    "cheating":[.22, .75, 1.6, 1.7],
    "trade":[.17, .67, 4.5, 4.5]
}
colorOptions = {
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

def generate_image(start, text1, text2, color):
    image = Image.open("generationFiles/"+start+".jpg")
    h = image.height
    w = image.width
    print("height: " + str(h))
    print("width: "+ str(w))
    text1h = h / textLocations[start][2]
    text1w = w * textLocations[start][0]
    text2h = h / textLocations[start][3]
    text2w = w * textLocations[start][1]
    font = ImageFont.truetype("generationFiles/arial.ttf", 15)
    colorNums = colorOptions[color]

    edit = ImageDraw.Draw(image)
    edit.text((text1w,text1h), text1, colorNums, font=font)
    edit.text((text2w,text2h), text2, colorNums, font=font)

    image.save("result.jpg")


#generate_image("cheating", "test1", "test2", "white")