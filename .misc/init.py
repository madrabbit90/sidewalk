
#startinit
toolcursor = 0


if grep != "":
    cursorpoint = 0

pcode = 0
walltic = 0
exec(open("./.config/sidewalk/.misc/icode.py").read())
exec(open("./.config/sidewalk/.misc/mason.py").read())

toolhide = ""
toolswap = "icon"
if icode == pcode:
    toolswap = "alticon"
    toolhide = "-A"

#if grep == "":
#    for x in range(len(titles)):
#        os.system("mv './.config/sidewalk/"+titles[x]+"' './.config/sidewalk/"+str(x+1000)+titles[x][4:]+"'")

os.system("echo wallframes = [  > sidetemp.py")
os.system("ls -d ./.config/sidewalk/.wallpaper/* | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo titles = [  >>  sidetemp.py")
os.system("ls ./.config/sidewalk"+folders[subfolder]+" | grep -i 'add media\|"+grep+"' | sed -e 's/^/\"/g' | sed -e 's/$/\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo tools = [  >>  sidetemp.py")
os.system("ls "+toolhide+" ./.config/sidewalk/.tools/ | sed -e 's/^/\".\/.config\/sidewalk\/.tools\//g' | sed -e 's/$/\/"+toolswap+"\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
os.system("echo toolslist = [  >> sidetemp.py")
os.system("ls "+toolhide+" ./.config/sidewalk/.tools/ | sed -e 's/^/\".\/.config\/sidewalk\/.tools\//g' | sed -e 's/$/\/launcher\",/g' >> sidetemp.py")
os.system("echo ] >> sidetemp.py")
exec(open("sidetemp.py").read())

if len(titles) > tilemax and grep == "":
    titles = titles[:tilemax]

icon = []
iconalph = []
if grep == "":
    wallpaper = []
tool=[]
toolalph=[]

if subfolder == 4:
    talltoggle = 1.00
else:
    talltoggle = 1.33
for x in range(len(titles)):
#    icon.append(pygame.image.load(line[x]))
    iconalph.append(lowalph)
    icon.append(pygame.image.load("./.config/sidewalk"+folders[subfolder]+"/"+titles[x]+"/icon").convert_alpha())
    icon[x] = pygame.transform.scale(icon[x], (iconsize, math.floor(iconsize*talltoggle)))
if grep == "":
    for x in range(len(wallframes)):
        wallpaper.append(pygame.image.load(wallframes[x]).convert_alpha())
        wallpaper[x] = pygame.transform.scale(wallpaper[x], (w, h))
        wallpaper[x].set_alpha(wallalph)
for x in range(len(tools)):
    toolalph.append(lowalph)
    tool.append(pygame.image.load(tools[x]).convert_alpha())
    tool[x] = pygame.transform.scale(tool[x], (toolsize, toolsize))

if immerse == 0:
    toolcenter = (w/2)-(((toolsize*len(tools))+(toolspace*(len(tools)-1)))/2)+toolspace
if immerse == 1:
    toolcenter = iconspace*4
if immerse == 2:
    toolcenter = (flipw/2)-(((toolsize*len(tools))+(toolspace*(len(tools)-1)))/2)+toolspace
