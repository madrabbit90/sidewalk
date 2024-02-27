#startinit
pcode = 0
walltic = 0
exec(open("./.config/sidewalk/.misc/icode.py").read())
exec(open("./.config/sidewalk/.misc/mason.py").read())
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
exec(open("sidetemp.py").read())


icon = []
wallpaper = []

for x in range(len(line)):
    icon.append(pygame.image.load(line[x]))
    icon[x] = pygame.transform.scale(icon[x], (iconsize, iconsize))
for x in range(len(wallframes)):
    wallpaper.append(pygame.image.load(wallframes[x]))
    wallpaper[x] = pygame.transform.scale(wallpaper[x], (w, h))
