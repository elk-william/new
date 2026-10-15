#minigame_processing_python_day1minigame_processing_python_day1
def setup():
    size(1000,650)
start=False
start_circle=True
a="start"
player_y=490
vy=0
gy=0.6
air=False
def draw():
    global start_circle,a,start,player_y,vy,gy,air
    background(61,132,242)
    fill(116,75,22)
    noStroke()
    rect(0,550,1000,100)
    if start_circle:
        fill(100,0,0)
        ellipse(500,325,100,100)
        fill(0)
        textSize(45)
        text(a,455,338)
    if start:
        fill(214,70,17)
        rect(70,player_y,60,60)
        vy+=gy
        player_y+=vy
        if player_y>=490:
            player_y=490
            vy=0
            air=False
def keyPressed():
    global vy,air
    if key==' ' and air==False:
        vy=-18
        air=True
def mousePressed():
    global start_circle,start
    if 450 <= mouseX <= 550 and 275<=mouseY<=375:
        start=True
        start_circle=False
