import urllib2
import json
import random, os
import copy

add_library('minim')
path=os.getcwd()

player=Minim(this)

def get_data():
    dic = {}
    with open('exit.json') as j:
        dic = json.load(j)
    return dic

song_data = get_data()

songs = []

for key in song_data:
    songs.append(key)

songschoices = copy.deepcopy(songs)

# right now I am assuming that each round has ten songs

class Emojified():
    
    #constructor of the class
    def __init__(self):

        # choose ten songs randomly
        global songschoices, song_data
        emoji_song = []
        artists_ten = []
        emojis = []
    
        for i in range(10):
            song = random.choice(songschoices)
            emoji_song.append(song)
            emojiartist = song_data[song]["artist"]
            artists_ten.append(emojiartist)
            emojilyrics = song_data[song]["lyrics"]["emojified"]
            emojis.append(emojilyrics)
            
        #the data for questions
        self.songs = emoji_song
        self.artist = artists_ten
        self.emojilyrics = emojis
        
        #data for score options and answer selection
        self.optionchoices=[]
        self.score=0
        self.click=False
        self.option=''
        self.realanswer=''
        
        #selections
        self.sel1=''
        self.sel2=''
        self.sel3=''
        self.sel4=''
        
        #question num updates
        self.questions=0
        self.questionnum=0
        
        #the ones to display on screen one by one
        self.realsong=''
        self.realartist=''
        self.reallyrics=''
        
        #music
        self.correctmusic=player.loadFile(path+"/sounds/nice.mp3")
        self.wrongmusic=player.loadFile(path+"/sounds/nope.mp3")
        self.bgmusic=player.loadFile(path+"/sounds/bensound-retrosoul.mp3")
        self.endmusic=player.loadFile(path+"/sounds/ending.mp3")
    
        
    #the data needed for all the questions
    def theQ(self):

        global songschoices
        
        if self.questions==0:
            self.realsong = self.songs[self.questions]
            self.realartist = self.artist[self.questions]
            self.reallyrics = self.emojilyrics[self.questions]
        
            # now we need to choose three mixed up choices
            try:
                songschoices.remove(self.realsong)
            except:
                pass
                
            for i in range(3):
                otherthree = random.choice(songschoices)
                songschoices.remove(otherthree)
                self.optionchoices.append(otherthree)
                
            #add the realsong into the choices    
            self.optionchoices.append(self.realsong)
            #update the question numbers
            self.questions+=1
            self.questionnum+=1
            
            #set what each selection would be and identify the right answer
            self.sel1=random.choice(self.optionchoices)
            self.optionchoices.remove(self.sel1)
            if self.sel1==self.realsong:
                self.realanswer='A'
                
            self.sel2=random.choice(self.optionchoices)
            self.optionchoices.remove(self.sel2)
            if self.sel2==self.realsong:
                self.realanswer='B'
                
            self.sel3=random.choice(self.optionchoices)
            self.optionchoices.remove(self.sel3)
            if self.sel3==self.realsong:
                self.realanswer='C'
                
            self.sel4=random.choice(self.optionchoices)
            if self.sel4==self.realsong:
                self.realanswer='D'
                
            self.optionchoices=[]
            
    #show the first question and update after each selection total of ten questions
    def update(self):
        
        global songschoices
            
        #continue to update the questions    
        self.click=False        
        self.realsong = self.songs[self.questions]
        self.realartist = self.artist[self.questions]
        self.reallyrics = self.emojilyrics[self.questions]
                
        # now we need to choose three mixed up choices
        try:
            songschoices.remove(self.realsong)
        except:
            pass
            
        for i in range(3):
            otherthree = random.choice(songschoices)
            songschoices.remove(otherthree)
            self.optionchoices.append(otherthree)
        
        #add the realsong into the choices    
        self.optionchoices.append(self.realsong)    
        #update the question nums        
        self.questions+=1
        self.questionnum+=1
        
        #set what each selection would be and identify the right answer
        self.sel1=random.choice(self.optionchoices)
        self.optionchoices.remove(self.sel1)
        if self.sel1==self.realsong:
            self.realanswer='A'
            
        self.sel2=random.choice(self.optionchoices)
        self.optionchoices.remove(self.sel2)
        if self.sel2==self.realsong:
            self.realanswer='B'
            
        self.sel3=random.choice(self.optionchoices)
        self.optionchoices.remove(self.sel3)
        if self.sel3==self.realsong:
            self.realanswer='C'
            
        self.sel4=random.choice(self.optionchoices)
        if self.sel4==self.realsong:
            self.realanswer='D'
            
        self.optionchoices=[]
        
    #show on the interface
    def showtheq(self):
        
        #number of question
        number = str(self.questionnum)
        stroke(255, 255, 255)
        strokeWeight(7)
        fill(255, 255, 255)
        rect(50, 50, 200, 200)
        fill(0)
        textSize(150)
        
        # text("1",50,50)
        text(number, 70, 70, 400, 200)
        
        # lyrics text box
        lyrics = self.reallyrics
        stroke(200, 200, 200)
        strokeWeight(9)
        fill(255, 255, 255)
        rect(300, 100, 1100, 300)
        fill(0)
        textSize(40)
        # text(lyrics, 300, 100)
        text(lyrics, 350, 110, 1000, 300)
        
        # score box
        score = 'score'
        number= str(self.score)
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 255)
        rect(100, 500, 250, 150)
        fill(0)
        textSize(45)
        text(score, 150, 550)
        text(number,200, 600)
        
        # hint box
        image(loadImage("hintbutton.png"), 100, 750, 250, 100)
        
        # choice 1
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(500, 450, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel1, 520, 520, 380, 230)
        
        # choice 2
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(1000, 450, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel2, 1020, 520, 380, 230)
        
        # choice 3
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(500, 750, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel3, 520, 820, 380, 230)
        
        # choice 4
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(1000, 750, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel4, 1020, 820, 380, 230)

        
    #display function    
    def display(self):
        
        #as long as it is not 10th question yet it is updating questions
        #the first q    
        self.theQ()
        self.showtheq()
        self.bgmusic.play()
        
        #the other 9 of the questions
        try:
            for r in range(9) :
                if self.click==True and self.questions<=9:
                    self.update()
                    self.showtheq()
        except:
            global state
            state=5
            
                

#class for textlyrics mode        
class Textlyrics():
    
    #constructor of the class
    def __init__(self):

        global songschoices, song_data

        text_song = []

        artists_ten = []

        text_ly = []
        
        #randomly choosing songs
        for i in range(10):
            song = random.choice(songschoices)
            text_song.append(song)
            textartist = song_data[song]["artist"]
            artists_ten.append(textartist)
            textlyrics = song_data[song]["lyrics"]["original"]
            text_ly.append(textlyrics)
            
        #data needed for all the songs
        self.songs = text_song
        self.artist = artists_ten
        self.textlyrics = text_ly
        
        #data for score options and answer selection
        self.optionchoices=[]
        self.score=0
        self.click=False
        self.option=''
        self.realanswer=''
        
        #selections
        self.sel1=''
        self.sel2=''
        self.sel3=''
        self.sel4=''
        
        #to update questions numbers
        self.questions=0
        self.questionnum=0
        
        #the ones showing up on screen
        self.realsong=''
        self.realartist=''
        self.reallyrics=''
        
        #music
        self.correctmusic=player.loadFile(path+"/sounds/nice.mp3")
        self.wrongmusic=player.loadFile(path+"/sounds/nope.mp3")
        self.bgmusic=player.loadFile(path+"/sounds/bensound-retrosoul.mp3")
        self.endmusic=player.loadFile(path+"/sounds/ending.mp3")
        
   #the data needed for all the questions
    def theQ(self):
        
        global songschoices
        
        if self.questions==0:
            self.realsong = self.songs[self.questions]
            self.realartist = self.artist[self.questions]
            self.reallyrics = self.textlyrics[self.questions]
    
            # now we need to choose three mixed up choices
            try:
                songschoices.remove(self.realsong)
            except:
                pass
                
            for i in range(3):
                otherthree = random.choice(songschoices)
                songschoices.remove(otherthree)
                self.optionchoices.append(otherthree)
            
            #add the realsong into the choices    
            self.optionchoices.append(self.realsong)
            #update the question numbers
            self.questions+=1
            self.questionnum+=1
        
            #set what each selection would be and identify the right answer
            self.sel1=random.choice(self.optionchoices)
            self.optionchoices.remove(self.sel1)
            if self.sel1==self.realsong:
                self.realanswer='A'
            
            self.sel2=random.choice(self.optionchoices)
            self.optionchoices.remove(self.sel2)
            if self.sel2==self.realsong:
                self.realanswer='B'
            
            self.sel3=random.choice(self.optionchoices)
            self.optionchoices.remove(self.sel3)
            if self.sel3==self.realsong:
                self.realanswer='C'
            
            self.sel4=random.choice(self.optionchoices)
            if self.sel4==self.realsong:
                self.realanswer='D'
            
            self.optionchoices=[]

            
    #show the first question and update after each selection total of ten questions
    def update(self):
        
        global songschoices
            
        #continue to update the questions 
        self.click=False        
        self.realsong = self.songs[self.questions]
        self.realartist = self.artist[self.questions]
        self.reallyrics = self.textlyrics[self.questions]

        # now we need to choose three mixed up choices
        try:
            songschoices.remove(self.realsong)
        except:
            pass
            
        for i in range(3):
            otherthree = random.choice(songschoices)
            songschoices.remove(otherthree)
            self.optionchoices.append(otherthree)
        
        #add the realsong into the choices    
        self.optionchoices.append(self.realsong)    
        #update the question nums        
        self.questions+=1
        self.questionnum+=1
        
        #set what each selection would be and identify the right answer
        self.sel1=random.choice(self.optionchoices)
        self.optionchoices.remove(self.sel1)
        if self.sel1==self.realsong:
            self.realanswer='A'
            
        self.sel2=random.choice(self.optionchoices)
        self.optionchoices.remove(self.sel2)
        if self.sel2==self.realsong:
            self.realanswer='B'
            
        self.sel3=random.choice(self.optionchoices)
        self.optionchoices.remove(self.sel3)
        if self.sel3==self.realsong:
            self.realanswer='C'
            
        self.sel4=random.choice(self.optionchoices)
        if self.sel4==self.realsong:
            self.realanswer='D'
            
        self.optionchoices=[]
    
    #present in the interface        
    def showtheq(self):
        
        myFont = loadFont("Arial-Black-100.vlw");
        textFont(myFont)
        
        #number of question
        number = str(self.questionnum)
        stroke(255, 255, 255)
        strokeWeight(7)
        fill(255, 255, 255)
        rect(50, 50, 200, 200)
        fill(0)
        textSize(100)
        
        # text("1",50,50)
        text(number, 70, 70, 200, 400)
        
        # lyrics text box
        lyrics = self.reallyrics
        stroke(200, 200, 200)
        strokeWeight(9)
        fill(255, 255, 255)
        rect(300, 100, 1100, 300)
        fill(0)
        textSize(40)
        # text(lyrics, 300, 100)
        text(lyrics, 350, 110, 1000, 300)
        
        # score box
        score = 'score'
        number= str(self.score)
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 255)
        rect(100, 500, 250, 150)
        fill(0)
        textSize(45)
        text(score, 150, 550)
        text(number,200, 600)
        
        # hint box
        image(loadImage("hintbutton.png"), 100, 750, 250, 100)
        
        # choice 1
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(500, 450, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel1, 520, 520, 380, 230)
        
        # choice 2
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(1000, 450, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel2, 1020, 520, 380, 230)
        
        # choice 3
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(500, 750, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel3, 520, 820, 380, 230)
        
        # choice 4
        stroke(0)
        strokeWeight(9)
        fill(255, 255, 204)
        rect(1000, 750, 400, 250)
        fill(0)
        textSize(45)
        text(self.sel4, 1020, 820, 380, 230)

            
            
    #display function    
    def display(self):
        
        #as long as it is not 10th question yet it is updating questions
        #the first q    
        self.theQ()
        self.showtheq()
        self.bgmusic.play()
        
        #the other 9 of the questions
        try:
            for r in range(9) :
                if self.click==True and self.questions<=9:
                    self.update()
                    self.showtheq()
        except:
            global state
            state=5
                
        
        
emojified=Emojified()
textlyrics=Textlyrics()
                
# transfer to userinterface    
xpos = 0
ypos = 0
state = 0
hints = 3 

def setup():
    size(1600, 1200)
    background(255,255,255)
    textFont(createFont("OpenSansEmoji.ttf", 16, True))
    
def draw():
    if state == 0:
        draw1() #first starting page
        
    elif state == 1:
        draw2() #select mode page
        
    elif state == 2:
        draw3() #textver game page
        
    elif state == 21:
        draw3a() #textver game after selection page
    
    elif state == 3:
        draw4() #emojiver game page
    
    elif state == 31:
        draw4a() #emojiver game after selection page
        
    elif state == 4:
        draw5() #hint page for text
        
    elif state ==41:
        draw5a()#hint page for emojis
        
    elif state == 5:
        draw6() #end page of text
        
    elif state == 51:
        draw6a() #end page of emoji
        

def draw1(): #first starting page
    global state
    global xpos, ypos
    
    background(255,255,255)
    image(loadImage("title.png"),120,200, 1350,190)
    image(loadImage("startbutton.png"), 680, 500, 247, 118)
    image(loadImage("exitbutton.png"), 680, 700, 247, 118)
    
    if 680 < xpos < 927 and 500 < ypos < 618:
        # selectmode page loaded
        #music to begin
        state = 1
        xpos = 0
        ypos = 0
        
    elif 680 < xpos < 927 and 700 < ypos < 818:
        # exit game
        exit()

def draw2():
    global state
    global xpos, ypos
    
    background(255,255,255)
    image(loadImage("selecttitle.png"),130,200, 1327,177)
    image(loadImage("textver.png"), 400, 500, 670, 143)
    image(loadImage("emojiver.png"), 400, 700, 741, 127)
    
    
    if 400 < xpos < 1070 and 500 < ypos < 643:
        # textver game loaded
        state = 2
        xpos = 0
        ypos = 0
        
    elif 400 < xpos < 1141 and 700 < ypos < 827:
        # emojiver game loaded
        state = 3
        xpos = 0
        ypos = 0


def draw3(): #textver game
    
    global state
    global hints
    global xpos, ypos
    
    background(255,255,255)

    #game display
    textlyrics.display()
    #check for score updating
    #choose the first choice
    if 500 < xpos < 900 and 450 < ypos < 700:
        textlyrics.click=True
        textlyrics.option='A'
        if textlyrics.option==textlyrics.realanswer:
            textlyrics.score+=1
        else:
            textlyrics.score+=0
        state=21
        xpos=0
        ypos=0

    #choose the second option    
    elif 1000 < xpos < 1400 and 450 < ypos < 700:
        textlyrics.click=True
        textlyrics.option='B'
        if textlyrics.option==textlyrics.realanswer:
            textlyrics.score+=1
        else:
            textlyrics.score+=0
        state=21
        xpos=0
        ypos=0

    #choose the third option    
    elif 500 < xpos < 900 and 750 < ypos < 1000:
        textlyrics.click=True
        textlyrics.option='C'
        if textlyrics.option==textlyrics.realanswer:
            textlyrics.score+=1
        else:
            textlyrics.score+=0
        state=21
        xpos=0
        ypos=0

    #choose the forth option    
    elif 1000 < xpos < 1400 and 750 < ypos < 1000:
        textlyrics.click=True
        textlyrics.option='D'
        if textlyrics.option==textlyrics.realanswer:
            textlyrics.score+=1
        else:
            textlyrics.score+=0
        state=21
        xpos=0
        ypos=0
    
    
    if textlyrics.option==textlyrics.realanswer:
        textlyrics.correctmusic.play()
    else:
        textlyrics.wrongmusic.play()
            
    #hint    
    if 100<xpos<350 and 750<ypos<850:
        background(255,255,255)
        hints -= 1
        state = 4
        xpos = 0
        ypos = 0
        
    
def draw3a(): #text ver - after selection 
    # update block color
    # update score
    
    global state
    global hints
    global xpos, ypos
    
    #choice 1
    stroke(0)
    strokeWeight(9)
    if textlyrics.realanswer=='A':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(500,450,400,250)
    fill(0)
    textSize(45)
    text(textlyrics.sel1,520,470,380,230)
    
    #choice 2 
    stroke(0)
    strokeWeight(9)
    if textlyrics.realanswer=='B':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(1000,450,400,250)
    fill(0)
    textSize(45)
    text(textlyrics.sel2,1020,470,380,230)
    
    #choice 3 
    stroke(0)
    strokeWeight(9)
    if textlyrics.realanswer=='C':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(500,750,400,250)
    fill(0)
    textSize(45)
    text(textlyrics.sel3,520,770,380,230)
    
    #choice 4 
    stroke(0)
    strokeWeight(9)
    if textlyrics.realanswer=='D':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(1000,750,400,250)
    fill(0)
    textSize(45)
    text(textlyrics.sel4,1020,770,380,230)
    
    #if the tenth questions is done we end the game
    if textlyrics.questionnum==10:
        textlyrics.bgmusic.pause()
        textlyrics.endmusic.play()
        state=5
        xpos=0
        ypos=0
        
    #after showing the colors when click you go to the next questions
    if 0<xpos<1600 and 0<ypos<1200:
        state=2
        xpos = 0
        ypos = 0

def draw4(): #emoji ver
    
    global state
    global hints
    global xpos, ypos
    
    background(255,255,255)
    
    
    #game display
    emojified.display()
    
    #choose the first choice
    if 500 < xpos < 900 and 450 < ypos < 700:
        emojified.click=True
        emojified.option='A'
        #check for score updating
        if emojified.option==emojified.realanswer:
            emojified.score+=1
        else:
            emojified.score+=0
        state=31
        xpos=0
        ypos=0

    #choose the second option    
    elif 1000 < xpos < 1400 and 450 < ypos < 700:
        emojified.click=True
        emojified.option='B'
        #check for score updating
        if emojified.option==emojified.realanswer:
            emojified.score+=1
        else:
            emojified.score+=0
        state=31
        xpos=0
        ypos=0

    #choose the third option    
    elif 500 < xpos < 900 and 750 < ypos < 1000:
        emojified.click=True
        emojified.option='C'
        #check for score updating
        if emojified.option==emojified.realanswer:
            emojified.score+=1
        else:
            emojified.score+=0
        state=31
        xpos=0
        ypos=0

    #choose the forth option    
    elif 1000 < xpos < 1400 and 750 < ypos < 1000:
        emojified.click=True
        emojified.option='D'
        #check for score updating
        if emojified.option==emojified.realanswer:
            emojified.score+=1
        else:
            emojified.score+=0
        state=31
        xpos=0
        ypos=0
        
    if emojified.option==emojified.realanswer:
        emojified.correctmusic.play()
    else:
        emojified.wrongmusic.play()
        
    #when choosing the hint button    
    if 100<xpos<350 and 750<ypos<850:
        background(255,255,255)
        hints -= 1
        state = 41
        xpos = 0
        ypos = 0

    

def draw4a(): #emoji ver - after selection 
    # update block color
    # update score
    
    global state
    global xpos, ypos
    
    #choice 1
    stroke(0)
    strokeWeight(9)
    if emojified.realanswer=='A':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(500,450,400,250)
    fill(0)
    textSize(45)
    text(emojified.sel1,520,470,380,230)
    
    #choice 2 
    stroke(0)
    strokeWeight(9)
    if emojified.realanswer=='B':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(1000,450,400,250)
    fill(0)
    textSize(45)
    text(emojified.sel2,1020,470,380,230)
    
    #choice 3 
    stroke(0)
    strokeWeight(9)
    if emojified.realanswer=='C':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(500,750,400,250)
    fill(0)
    textSize(45)
    text(emojified.sel3,520,770,380,230)
    
    #choice 4 
    stroke(0)
    strokeWeight(9)
    if emojified.realanswer=='D':
        fill(158,214,255)
    else:
        fill(255,158,158)
    rect(1000,750,400,250)
    fill(0)
    textSize(45)
    text(emojified.sel4,1020,770,380,230)
    
    #if it's the tenth Qs then it ends
    if emojified.questionnum==10:
        emojified.bgmusic.pause()
        emojified.endmusic.play()
        state=51
        xpos=0
        ypos=0
        
    #after showing the colors when click you go to the next questions
    if 0<xpos<1600 and 0<ypos<1200:
        state=3
        xpos = 0
        ypos = 0
        
        
def draw5(): #hint page
    global state
    global hints
    global xpos, ypos
    
    if hints >= 1:
    
        myFont = loadFont("Arial-Black-100.vlw");
        textFont(myFont)
        
        background(255,255,255)
        
        image(loadImage("hinttitle.png"),535,150)
        image(loadImage("singer.png"), 308, 380, 312, 142)
        image(loadImage("closebutton.png"), 680, 900, 250,98)
        
        #singer text box
        singer = textlyrics.realartist
        stroke(200,200,200)
        strokeWeight(7)
        fill(255,255,255)
        rect(670,410,620,80)
        fill(0);
        textSize(45)
        text(singer,690,430,600,60)
    
        if 680 < xpos < 930 and 900 < ypos < 998:
            # after closing the hint page'
            state=2
            xpos=0
            ypos=0

    else:
            
        image(loadImage("outofhint.jpeg"),300,500,411,103)
        
        #after no hints when click you go to the next questions
        if 0<xpos<1600 and 0<ypos<1200:
            state=2
            xpos = 0
            ypos = 0
            
def draw5a(): #hint page for emoji
    global state
    global hints
    global xpos, ypos
    
    if hints >= 1:
    
        myFont = loadFont("Arial-Black-100.vlw");
        textFont(myFont)
        
        background(255,255,255)
        
        image(loadImage("hinttitle.png"),535,150)
        image(loadImage("singer.png"), 308, 380, 312, 142)
        image(loadImage("closebutton.png"), 680, 900, 250,98)
        
        #singer text box
        singer = emojified.realartist
        stroke(200,200,200)
        strokeWeight(7)
        fill(255,255,255)
        rect(670,410,620,80)
        fill(0);
        textSize(45)
        text(singer,690,430,600,60)
    
        if 680 < xpos < 930 and 900 < ypos < 998:
            # after closing the hint page
            state=3
            xpos=0
            ypos=0#temp
            
    else:
            
        image(loadImage("outofhint.jpeg"),300,500,411,103)
        
        #after no hints when click you go to the next questions
        if 0<xpos<1600 and 0<ypos<1200:
            state=3
            xpos = 0
            ypos = 0
    
def draw6(): #end page
    global state
    global xpos, ypos
    
    myFont = loadFont("Arial-Black-100.vlw");
    textFont(myFont)
    background(255,255,255)
    
    #music
    #endmusic=player.loadFile(path+"/sounds/ending.mp3")
    #endmusic.play()
    
    image(loadImage("endtitle.png"),530,150)
    image(loadImage("score1.png"),150,480)
    image(loadImage("score2.png"),1100,480)
    image(loadImage("tryagainbutton.png"),500,900,294,105)
    image(loadImage("closebutton.png"),850,900,250,95)
    
    #score point box
    usrscore = str(textlyrics.score)
    stroke(0)
    strokeWeight(9)
    fill(250,250,250)
    rect(800,480,180,180)
    fill(0)
    textSize(100)
    text(usrscore,850,530,160,160)
    
    #restart game 
    if 500 < xpos < 794 and 900 < ypos < 1005:
        # reload the game
        try:
            state = 1
            xpos = 0
            ypos = 0
            textlyrics.endmusic.pause()
            global emojified
            global textlyrics
            global songchoices
            songschoices = copy.deepcopy(songs)
            emojified=Emojified()
            textlyrics=Textlyrics()
        except:
            state=0
        
    elif 850 < xpos < 1100 and 900 < ypos < 995:
        # exit game
        exit()
        
def draw6a(): #end page
    global state
    global xpos, ypos
    
    myFont = loadFont("Arial-Black-100.vlw");
    textFont(myFont)
    background(255,255,255)
    
    image(loadImage("endtitle.png"),530,150)
    image(loadImage("score1.png"),150,480)
    image(loadImage("score2.png"),1100,480)
    image(loadImage("tryagainbutton.png"),500,900,294,105)
    image(loadImage("closebutton.png"),850,900,250,95)
    
    #score point box
    usrscore = str(emojified.score)
    stroke(0)
    strokeWeight(9)
    fill(250,250,250)
    rect(800,480,180,180)
    fill(0)
    textSize(100)
    text(usrscore,850,530,160,160)
    
    #restart game
    if 500 < xpos < 794 and 900 < ypos < 1005:
        try:
            # reload the game
            state = 1
            xpos = 0
            ypos = 0
            emojified.endmusic.pause()
            global emojified
            global textlyrics
            global songchoices
            songschoices = copy.deepcopy(songs)
            emojified=Emojified()
            textlyrics=Textlyrics()
            
        except:
            global state
            state=0
        
    elif 850 < xpos < 1100 and 900 < ypos < 995:
        # exit game
        exit()
        
def mouseClicked():
    global xpos, ypos
    xpos = mouseX
    ypos = mouseY
