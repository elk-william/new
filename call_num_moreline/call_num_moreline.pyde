#call_num_moreline
import random
#textFont_call_num
def setup():
    size(500,300)
    textSize(50)
    background(234,216,92)
words=""
n=0
font=None
wordlist=[]
new=""
def draw():
    global words,n,font
    background(234,216,92)
    fill(255,0,0)
    rect(450,150,50,50)
    fill(0)
    #text(words,40,n*30+20)
    for i in range(len(wordlist)):
        text(wordlist[i],40,i*30+20)
    font=createFont("PingFang TC", 20)
    textFont(font)
def mousePressed():
    global words,n,wordlist,new
    if mouseX<=500 and mouseX>=450 and mouseY>=150 and mouseY<=200:
        fill(0)  
        num=random.randint(1000, 9999)
        p=random.randint(1, 9)      
        new=u"請{}號到{}號櫃檯".format(num, p)
        #n+=1
        wordlist.append(new)
