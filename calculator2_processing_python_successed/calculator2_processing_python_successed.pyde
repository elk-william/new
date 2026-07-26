#calculator2_processing_python_successed
img= None
img1=None
screen=""
num=""
op=""

def setup():
    size(400,650)

    #f = createFont("Arial", 60)
    #textFont(f)
    global img,img1
    img=loadImage("del.png")
    #img1=loadImage("
def draw():
    background(0)
    fill(255)
    text(screen,20,100)
    for i in range(4):
        for j in range(5):
            fill(255)
            ellipse(i*100+50,j*100+200,100,100)
    textSize(60)
    #textMode(CENTER,CENTER)
    fill(0)
    text("0",135,620)
    text("1",35,520)
    text("2",135,520)
    text("3",235,520)
    text("4",35,420)
    text("5",135,420)
    text("6",235,420)
    text("7",35,320)
    text("8",135,320)
    text("9",235,320)
    text("+",335,520)
    text("=",335,620)
    strokeWeight(5)
    line(330,400,370,400)
    strokeWeight(5)
    line(330,280,370,320)
    line(370,280,330,320)
    strokeWeight(5)
    line(330,200,370,200)
    ellipse(350,185,8,8)
    ellipse(350,215,8,8)
    image(img,15,180,70,40)
    text("AC",115,220)
def mousePressed():
    global n,screen,num,op
    a=mouseX//100
    b=float((mouseY-50)//100)
    if mouseY>150:        
        if a==0 and b<=2.5 and b>=1.5:
            screen+="7"
        if a==0 and b<=3.5 and b>=2.5:
            screen+="4"
        if a==0 and b<=4.5 and b>=3.5:
            screen+="1"
        if a==1 and b<=2.5 and b>=1.5:
            screen+="8"
        if a==1 and b<=3.5 and b>=2.5:
            screen+="5"
        if a==1 and b<=4.5 and b>=3.5:
            screen+="2"
        if a==2 and b<=2.5 and b>=1.5:
            screen+="9"
        if a==2 and b<=3.5 and b>=2.5:
            screen+="6"
        if a==2 and b<=4.5 and b>=3.5:
            screen+="3"
        if a==1 and b>=4.5:
            screen+="0"
        if a==1 and b>=0.5 and b<=1.5:
            screen=""
        if a==0 and b>=0.5 and b<=1.5:
            screen=screen[:-1]
        if a==3 and b>=3.5 and b<=4.5:
             num=screen
             screen=""
             op="+"
        if a==3 and b>=1.5 and b<=2.5:
             num=screen
             screen=""
             op="x"
        if a==3 and b>=0.5 and b<=1.5:
             num=screen
             screen=""
             op="/"
        if a==3 and b>=2.5 and b<=3.5:
             num=screen
             screen=""
             op="-"
        if a==3 and b>=4.5 and b<=5.5:            
            if op=="+":
                screen=str(int(num)+int(screen))
            if op=="x":
                screen=str(int(num)*int(screen))
            if op=="/":
                screen=str(int(num)/int(screen))
            if op=="-":
                screen=str(int(num)-int(screen))
       
