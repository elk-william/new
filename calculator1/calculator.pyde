#calculator1
img= None
img1=None
n=1
def setup():
    size(400,650)
    background(0)
    #f = createFont("Arial", 60)
    #textFont(f)
    global img,img1
    img=loadImage("del.png")
    #img1=loadImage("
def draw():
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
    global n
    a=mouseX//100
    b=float((mouseY-50)//100)
    if mouseY>150:        
        if a==0 and b<=2.5 and b>=1.5:
            fill(255)
            text("7",35*n,120)
            n+=1
        if a==0 and b<=3.5 and b>=2.5:
            fill(255)
            text("4",35*n,120)
            n+=1
        if a==0 and b<=4.5 and b>=3.5:
            fill(255)
            text("1",35*n,120)
            n+=1
        if a==1 and b<=2.5 and b>=1.5:
            fill(255)
            text("8",35*n,120)
            n+=1
        if a==1 and b<=3.5 and b>=2.5:
            fill(255)
            text("5",35*n,120)
            n+=1
        if a==1 and b<=4.5 and b>=3.5:
            fill(255)
            text("2",35*n,120)
            n+=1
        if a==2 and b<=2.5 and b>=1.5:
            fill(255)
            text("9",35*n,120)
            n+=1
        if a==2 and b<=3.5 and b>=2.5:
            fill(255)
            text("6",35*n,120)
            n+=1
        if a==2 and b<=4.5 and b>=3.5:
            fill(255)
            text("3",35*n,120)
            n+=1
        if a==1 and b>=4.5:
            fill(255)
            text("0",35*n,120)
            n+=1
       
