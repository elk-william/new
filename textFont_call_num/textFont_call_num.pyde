import random
#textFont_call_num
def setup():
    size(500,300)
    textSize(50)
    background(234,216,92)
num=random.randint(1000, 9999)
p=random.randint(1, 9)
words=""
font=None
def draw():
    global words
    background(234,216,92)
    fill(255,0,0)
    rect(450,150,50,50)
    fill(0)
    text(words,40,100)
    font=createFont("PingFang TC", 20)
    textFont(font)
def mousePressed():
    global words,num,p
    if mouseX<=500 and mouseX>=450 and mouseY>=150 and mouseY<=200:
        fill(0)        
        words=u"請{}號到{}號櫃檯".format(num, p)
