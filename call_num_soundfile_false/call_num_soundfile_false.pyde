#call_num_soundfile_false
import random
add_library('sound')
#textFont_call_num
#words=""
#n=0
font=None
wordlist=[]
new=""
sounds = {}

def setup():
    size(500,300)
    textSize(50)
    background(234,216,92)
    global sounds

    sounds["請"] = SoundFile(this, "請.mp3")
    sounds["號到"] = SoundFile(this, "號到.mp3")
    sounds["號櫃檯"] = SoundFile(this, "號櫃檯.mp3")

    for i in range(10):
        sounds[str(i)] = SoundFile(this, str(i) + ".mp3")
def draw():
    global font
    background(234,216,92)
    fill(255,0,0)
    rect(450,150,50,50)
    fill(0)
    #text(words,40,n*30+20)
    for i in range(len(wordlist)):
        text(wordlist[i],40,i*30+20)
    font=createFont("PingFang TC", 20)
    textFont(font)
def speak(num, counter):

    sounds["請"].play()
    delay(500)

    for d in str(num):
        sounds[d].play()
        delay(350)

    sounds["號到"].play()
    delay(500)

    sounds[str(counter)].play()
    delay(350)

    sounds["號櫃檯"].play()
def mousePressed():
    global words,n,wordlist,new
    if mouseX<=500 and mouseX>=450 and mouseY>=150 and mouseY<=200:
        fill(0)  
        num=random.randint(1000, 9999)
        p=random.randint(1, 9)      
        new=u"請{}號到{}號櫃檯".format(num, p)
        #n+=1
        wordlist.append(new)
        speak(num,p)
