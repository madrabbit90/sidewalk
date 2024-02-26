#!/usr/bin/env python3

# Pygame Cheat Sheet
# This program should show you the basics of using the Pygame library.
# by Al Sweigart http://inventwithpython.com

# Download files from:
#     http://inventwithpython.com/cat.png
#     http://inventwithpython.com/bounce.wav

import pygame, sys, math
import os, os.path
from pygame.locals import *


pygame.init()
fpsClock = pygame.time.Clock()

icon = []
tool = []
wallpaper = []

copy = 10
paste = 10

windowSurfaceObj = pygame.display.set_mode((0, 0),pygame.RESIZABLE,32)
pygame.display.set_caption('sidewalk')
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(100, 100, 255)
whiteColor = pygame.Color(255, 255, 255)
blackColor = pygame.Color(0, 0, 0)

fontObj = pygame.font.Font('freesansbold.ttf', 40)
#fontObj = pygame.font.Font('/root/digital.ttf', 40)

hide = 0
flash = 0
fpoint = 1
cursorpoint = 0
cursorrow = 0
scroll = 0
scroller = 0
toolcursor = 0
walltic = 0

w, h = pygame.display.get_surface().get_size()
iconsize = math.floor(h/3)
iconspace = iconsize/20
iconposition = (h/2)-(iconsize/2)
offset = iconsize/5
itt = iconsize + iconspace
cursorsize = math.floor(iconsize / 35)
lablex = h/10
labley = w/8
clockx = w-(lablex*3)
toolsize = math.floor(iconsize/3)
toolposition = (h/4)*3
toolspace = toolsize/3

logoart = pygame.image.load("./.config/sidewalk/.misc/logo")
logoart = pygame.transform.scale(logoart, (math.floor(w/3), math.floor(h/6)))

os.system("echo exec sidewalk > .ratpoisonrc")

pcode = 0
exec(open("./.config/sidewalk/.misc/icode.py").read())

exec(open("./.config/sidewalk/.misc/mason.py").read())
toolhide = ""
if icode == pcode:
    #toolhide = "-A"
    toolhide = ""
os.system("echo titles = [  >  sidetemp.py")
os.system("ls ./.config/sidewalk | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")

exec(open("sidetemp.py").read())

for x in range(len(titles)):
    os.system("mv './.config/sidewalk/"+titles[x]+"' './.config/sidewalk/"+str(x+10)+titles[x][2:]+"'")


os.system("echo wallframes = [  > sidetemp.py")
os.system("ls -d ./.config/sidewalk/.wallpaper/* | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo line = [  >> sidetemp.py")
os.system("ls -d ./.config/sidewalk/*/icon | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo launch = [  >> sidetemp.py")
os.system("ls -d ./.config/sidewalk/*/launcher | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo playlist = [  >> sidetemp.py")
os.system("ls -d ./.config/sidewalk/*/playlist | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo titles = [  >>  sidetemp.py")
os.system("ls ./.config/sidewalk | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo tools = [  >> sidetemp.py")
os.system("ls "+toolhide+" ./.config/sidewalk/.tools/ | sed -e 's/^/\".\/.config\/sidewalk\/.tools\//g' | sed -e 's/$/\/icon\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo toolslist = [  >> sidetemp.py")
os.system("ls "+toolhide+" ./.config/sidewalk/.tools/ | sed -e 's/^/\".\/.config\/sidewalk\/.tools\//g' | sed -e 's/$/\/launcher\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
exec(open("sidetemp.py").read())

os.system("rm sidetemp.py")

toolcenter = (w/2)-(((toolsize*len(tools))+(toolspace*(len(tools)-1)))/2)+toolspace

windowSurfaceObj.blit(logoart, ((w/2)-(w/6),(h/2)-(h/12)))
pygame.display.update()
os.system("rm ./.config/sidewalk/.misc/backsplash.jpg")
os.system("scrot -z ./.config/sidewalk/.misc/backsplash.jpg")
os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")

for x in range(len(line)):
    icon.append(pygame.image.load(line[x]))
    icon[x] = pygame.transform.scale(icon[x], (iconsize, iconsize))
for x in range(len(wallframes)):
    wallpaper.append(pygame.image.load(wallframes[x]))
    wallpaper[x] = pygame.transform.scale(wallpaper[x], (w, h))
for x in range(len(tools)):
    tool.append(pygame.image.load(tools[x]))
    tool[x] = pygame.transform.scale(tool[x], (toolsize, toolsize))

pygame.mixer.quit()

while True:

    os.system('sh mustmp &')
    os.system('rm mustmp')

    walltic = walltic + 1
    if walltic > (len(wallframes)-1):
        walltic = 0

    flash = flash + 20*fpoint
    if flash > 255:
        flash = 255
        fpoint = -1
    if flash < 0:
        flash = 0
        fpoint = 1

    try:
        windowSurfaceObj.blit(wallpaper[walltic], (0,0))
    except:
        windowSurfaceObj.fill(blackColor)
    os.system('echo clock = \\"`date +%R`\\" > clock.py')
    exec(open("clock.py").read())

    if hide == 0:

        clockObj = fontObj.render(clock, True, whiteColor)
        windowSurfaceObj.blit(clockObj, (clockx, labley))
        if ".lock" in titles[cursorpoint]:
            lableObj = fontObj.render(titles[cursorpoint][3:][:-5], True, whiteColor)
        else:
            lableObj = fontObj.render(titles[cursorpoint][3:], True, whiteColor)
        windowSurfaceObj.blit(lableObj, (lablex, labley))

        scroll = 0
        if (offset+(itt*cursorpoint)+iconsize+offset) > w:
            scroll = (w - (offset+(itt*cursorpoint)+iconsize+offset))
        scroller = (scroll+scroller)/2

        for x in range(len(line)):
            windowSurfaceObj.blit(icon[x], (itt*x+offset+scroller, iconposition))
        for x in range(len(tools)):
            windowSurfaceObj.blit(tool[x], (toolcenter+(x*(toolsize+toolspace)), toolposition))

        if cursorrow == 0 and icode != pcode:
            pygame.draw.rect(windowSurfaceObj, (flash,flash,flash), (offset+(itt*cursorpoint)+scroller, iconposition, iconsize, iconsize), cursorsize)
        if cursorrow == 1 and icode != pcode:
            pygame.draw.rect(windowSurfaceObj, (flash,flash,flash), (toolcenter+(toolcursor*(toolsize+toolspace)), toolposition, toolsize, toolsize), cursorsize)
        if cursorrow == 0 and icode == pcode:
            pygame.draw.rect(windowSurfaceObj, (flash,0,0), (offset+(itt*cursorpoint)+scroller, iconposition, iconsize, iconsize), cursorsize)
        if cursorrow == 1 and icode == pcode:
            pygame.draw.rect(windowSurfaceObj, (flash,0,0), (toolcenter+(toolcursor*(toolsize+toolspace)), toolposition, toolsize, toolsize), cursorsize)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_h:
                hide = 1
            else:
                hide = 0
            if event.key == K_x and pcode == icode:
                os.system("rm ./.config/sidewalk/.misc/pauser.jpg")
                os.system("scrot -z ./.config/sidewalk/.misc/pauser.jpg")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/pauser.jpg")
                os.system("aterm -b 100 -tr -fn lucidasanstypewriter-bold-14 -bg black -fg white -tint gray -sh 50 -e byobu")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")
            if event.key == K_RETURN and cursorrow == 1:
                os.system("rm ./.config/sidewalk/.misc/pauser.jpg")
                os.system("scrot -z ./.config/sidewalk/.misc/pauser.jpg")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/pauser.jpg")
                os.system("aterm -b 100 -tr -fn lucidasanstypewriter-bold-14 -bg black -fg white -tint gray -sh 50 -e sh "+toolslist[toolcursor])
                os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")
            if event.key == K_RIGHT and cursorpoint < (len(line)-1) and cursorrow == 0:
                cursorpoint = cursorpoint + 1
            if event.key == K_LEFT and cursorpoint > 0 and cursorrow == 0:
                cursorpoint = cursorpoint - 1
            if event.key == K_RIGHT and toolcursor < (len(tools)-1) and cursorrow == 1:
                toolcursor = toolcursor + 1
            if event.key == K_LEFT and toolcursor > 0 and cursorrow == 1:
                toolcursor = toolcursor - 1
            if event.key == K_UP:
                cursorrow = 0
            if event.key == K_DOWN:
                cursorrow = 1
            if event.key == K_r and pcode == icode:
                os.system("echo pcode = 0 > ./.config/sidewalk/.misc/mason.py")
                exec(open("./.config/sidewalk/.misc/init.py").read())
            if event.key == K_u and pcode != icode:
                pygame.draw.rect(windowSurfaceObj, (255,255,255), pygame.Rect(0,0,w/2.5+5,h))
                pygame.draw.rect(windowSurfaceObj, (0,0,0), pygame.Rect(0,0,w/2.5,h))
                pygame.display.update()
                os.system("rm ./.config/sidewalk/.misc/pauser.jpg")
                os.system("scrot -z ./.config/sidewalk/.misc/pauser.jpg")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/pauser.jpg")
                os.system("aterm -b 100 -tr -fn lucidasanstypewriter-bold-14 -bg black -fg white -tint gray -sh 50 -e mason-lock")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")
                exec(open("./.config/sidewalk/.misc/mason.py").read())
                exec(open("./.config/sidewalk/.misc/init.py").read())
            if event.key == K_c and pcode == icode:
                copy = cursorpoint + 10
            if event.key == K_c and pcode != icode:
                os.system("killall mplayer")
            if event.key == K_p and pcode == icode and copy != paste:
                paste = cursorpoint + 10
                os.system("mv './.config/sidewalk/"+titles[copy-10]+"' './.config/sidewalk/"+str(paste)+titles[copy-10][2:]+"'")
                os.system("mv './.config/sidewalk/"+titles[paste-10]+"' './.config/sidewalk/"+str(copy)+titles[paste-10][2:]+"'")
                exec(open("./.config/sidewalk/.misc/init.py").read())
            if event.key == K_a and pcode == icode:
                pygame.draw.rect(windowSurfaceObj, (255,255,255), pygame.Rect(0,0,w/2.5+5,h))
                pygame.draw.rect(windowSurfaceObj, (0,0,0), pygame.Rect(0,0,w/2.5,h))
                pygame.display.update()
                os.system("echo "+str(cursorpoint+10)+" > shuforder")
                os.system("rm ./.config/sidewalk/.misc/pauser.jpg")
                os.system("scrot -z ./.config/sidewalk/.misc/pauser.jpg")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/pauser.jpg")
                os.system("aterm -b 100 -tr -fn lucidasanstypewriter-bold-14 -bg black -fg white -tint gray -sh 50 -e masonry-add")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")
                exec(open("./.config/sidewalk/.misc/init.py").read())
            if event.key == K_w and pcode == icode:
                pygame.draw.rect(windowSurfaceObj, (255,255,255), pygame.Rect(0,0,w/2.5+5,h))
                pygame.draw.rect(windowSurfaceObj, (0,0,0), pygame.Rect(0,0,w/2.5,h))
                pygame.display.update()
                os.system("rm ./.config/sidewalk/.misc/pauser.jpg")
                os.system("scrot -z ./.config/sidewalk/.misc/pauser.jpg")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/pauser.jpg")
                os.system("aterm -b 100 -tr -fn lucidasanstypewriter-bold-14 -bg black -fg white -tint gray -sh 50 -e masonry-wall")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")
                exec(open("./.config/sidewalk/.misc/init.py").read())
            if event.key == K_DELETE and pcode == icode:
                os.system("rm -r './.config/sidewalk/"+titles[cursorpoint]+"'")
                exec(open("./.config/sidewalk/.misc/init.py").read())
                if cursorpoint > 0:
                    cursorpoint = cursorpoint - 1
            elif event.key == K_RETURN and cursorrow == 0 and  (".lock" not in titles[cursorpoint] or icode == pcode):
                pygame.draw.rect(windowSurfaceObj, (255,255,255), pygame.Rect(0,0,w/1.8+5,h))
                pygame.draw.rect(windowSurfaceObj, (0,0,0), pygame.Rect(0,0,w/1.8,h))
                pygame.display.update()
                os.system("rm ./.config/sidewalk/.misc/pauser.jpg")
                os.system("scrot -z ./.config/sidewalk/.misc/pauser.jpg")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/pauser.jpg")
                os.system("aterm -b 100 -tr -fn lucidasanstypewriter-bold-14 -bg black -fg white -tint gray -sh 50 -e sh '"+playlist[cursorpoint]+"'")
                os.system("feh --bg-scale ./.config/sidewalk/.misc/backsplash.jpg")
                os.system("cat '"+launch[cursorpoint]+ "' > tmp")
                os.system("echo xrandr -s 1280x720 >> tmp")
                os.system("echo killall python >> tmp")
                os.system("echo killall nodm >> tmp")
                windowSurfaceObj.fill(blackColor)
                pygame.display.update()
                os.system("nohup sh tmp &")
                pygame.quit()

    pygame.display.update()
    fpsClock.tick(30) # pause to run the loop at 30 frames per second
