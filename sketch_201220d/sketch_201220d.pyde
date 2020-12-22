X=8
Y=8

def setup():
  global img
  size(500,500)
  img = loadImage("map2.jpg")

def draw():
  global img
  background(0)
  image(img,0,0)
  stroke (0, 250, 0)
  line(1,1,1,499)
  line(1,499,499,499)
  line(499,499,499,1)
  line(499,1,1,1)
  line(15,15,15,1)
  line(1,15,15,15)
  line(499,452,485,452)
  line(499,470,485,470)
  line(485,452,485,470)
  fill(250,0,0)
  global X
  global Y
  ellipse (X, Y, 10, 10)
  if (keyPressed):
      if (key == 'w'):
        Y=Y-1
        if Y<5:
         Y=6
      if (key == 's'):
        Y=Y+1 
        if Y>495:
         Y=494 
      if (key == 'd'):
        X=X+1
        if X>495:
         X=494  
      if (key == 'a'): 
        X=X-1 
        if X<5:
         X=6  
         
  if ((15<X<27) and (18<Y<27)):
     X=8
     Y=8
  if ((150<X<250) and (180<Y<270)):
     X=8
     Y=8
  if ((466<X<500) and (379<Y<450)):
     X=8
     Y=8
  if ((378<X<450) and (1<Y<70)):
     X=8
     Y=8
  if ((76<X<103) and (240<Y<270)):
     X=8
     Y=8
  if ((115<X<203) and (399<Y<430)):
     X=8
     Y=8
  if ((180<X<270) and (70<Y<90)):
     X=8
     Y=8
  if ((303<X<360) and (403<Y<429)):
     X=8
     Y=8
  if ((217<X<270) and (218<Y<279)):
     X=8
     Y=8
  if ((40<X<60) and (103<Y<150)):
     X=8
     Y=8
     
  if ((30<X<60) and (250<Y<370)):    #если слишком сложно, можно заковычить последние 10 if. Но вообще и так можно пройти;)
     X=8
     Y=8
  if ((450<X<480) and (452<Y<470)):
     X=8
     Y=8
  if ((200<X<300) and (79<Y<150)):
     X=8
     Y=8
  if ((450<X<480) and (376<Y<470)):
     X=8
     Y=8
  if ((1<X<103) and (440<Y<500)):
     X=8
     Y=8
  if ((134<X<203) and (390<Y<450)):
     X=8
     Y=8
  if ((261<X<270) and (170<Y<190)):
     X=8
     Y=8
  if ((160<X<260) and (43<Y<49)):
     X=8
     Y=8
  if ((50<X<70) and (300<Y<340)):
     X=8
     Y=8
  if ((220<X<260) and (450<Y<500)):
     X=8
     Y=8   
