import hashlib
import os
import sys
from unicodedata import name
from PIL import Image, ImageDraw, ImageFont
import hashlib
import os
import imagestore

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

def generate_image(username, start, text1, text2, color, tags):
    hhh = hashlib.md5(os.urandom(32)).hexdigest()
    print(hhh)
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

    image.save(str(hhh)+".jpg")

    imagestore.imgstore(username, hhh, tags)
    
    os.remove(hhh+".jpg")
    return hhh
    

def get_tags(tags):
    test = tags.replace(" ", '')
    tags2 = test.split(",", 4)
    tagsList = []
    for item in tags2:
        tagsList.append(item[0:15])
    while len(tagsList) < 5:
        tagsList.append("NULL")
    return tagsList


def generate_home(posts):
    dynam = ""
    number = 2
    #len(posts)
    i = 0
    while( i < number):
        current = posts[i]
        uname = current[0]
        pname = current[1]
        imagebyte = current[2]
        dynam += "<tr><td><p>"+ uname +"</p><img src=/hash/"+ pname +".jpg></td>"
        i += 1
        if( number > i):
            current = posts[i]
            uname = current[0]
            pname = current[1]
            imagebyte = current[2]
            dynam += "<td><p>"+ uname +"</p><img src=/hash/"+ pname +".jpg></td></tr>"
        i+=1
    return dynam
    

#generate_image("cheating", "test1", "test2", "white")