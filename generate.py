from audioop import reverse
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

    print(type(posts))
    
    dynam = ""
    number = 4
    #number = len(posts)
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
    

def generate_user(posts):
    #print(posts)
    #sys.stdout.flush()
    dynam = ""
    i = 0
    number = len(posts)
    while(i<number):
        current = posts[i]
        pname = current[1]
        dynam += "<img src=/hash/"+ pname +".jpg><br>"
        i+=1
    return dynam

#generate_image("cheating", "test1", "test2", "white")

def generate_search_results(posts):
    print("IN GENERATE SEAARCH RESULST")
    sys.stdout.flush()
    print(posts)
    sys.stdout.flush()
    dynam = ""
    print("for loop in gen search")
    sys.stdout.flush()
    for item in posts:
        # print(item)
        # sys.stdout.flush()
        # img = imagestore.imgbyhash(item)
        # uname = img[0]
        # print(uname)
        # sys.stdout.flush()
        # pname = img[1]
        # print(pname)
        # sys.stdout.flush()
        # imagebyte = img[2]
        dynam += "<img src=/hash/"+ item +".jpg><br>"
    return dynam
