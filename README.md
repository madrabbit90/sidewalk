"A Butterfly is a very visual person and likes to see 
all her belongings for fear of “Out of Sight, Out of Mind”.

--Cassandra Aarssen

![logo](https://github.com/madrabbit90/sidewalk/blob/main/.misc%2Flogo)

<center>Your media. Up front. Period.</center>

--cheat sheet--

<LEFT-RIGHT> - scroll through tools and tiles
<UP-DOWN> - toggle between toolbar and tilebar
<ENTER> - select
<keyboard> - search
<spacebar> - fetch poster/cover art
<,-.> - scroll through folders

--getting started--

Welcome to Sidewalk, a simple, pretty media frontend designed
for TVs and handhelds that allows you to flip through your
frequently used games and media and rotate them regularly with ease,
while still being able to access the Linux OS under the hood.

To make changes to your Sidewalk tiles, access the terminal, fetch
cover art or view parental restricted content, unlock your session by
clicking the lock icon in the toolbar and entering your PIN 
("12345" by default). You can lock the session at any time by clicking 
the lock icon again.

--add tiles--

Find (or search for) the "Add Media" tile and launch it. Click "Add" and
the media installer tool will prompt you to pick your file/folder from a
list, then give it a title.

Once created, you can access your new media from a launcher tile bearing
the sidewalk logo. If connected to the internet, pressing the spacebar will
download poster art for your media. If you don't find the fetched art
satisfactory, press the spacebar again to rotate through more options. 

Linux apps: /usr/bin/<filename> or $HOME/ directory
Movies: ./Videos/<filename>
DVD/Blu-Ray dumps and Video playlists: ./Videos/<foldername>
Emulated ROMs: ./Games/<foldername>
Photo album: ./Photos/<foldername>
Music: ./Musiv/<foldername>

--delete tiles--

Find (or search for) the "Add Media" tile and launch it. Click "Remove" and
the media installer tool will prompt you to pick your file/folder from a
list of installed media.

--Pre-installed tools--
Sidewalk does not come with media, but comes with prerequisites and tools
that allow you to play optical media, rip DVDs, CDs and Blu-Ray, screen mirror
an Android device, and download and manage a Steam or ROM library with
relative ease. No need to memorize commands or setings.

--change wallpaper--

Click the picture icon in the toolbar while unlocked. Any amimated GIF
files in the ./Pictures directory with the .gif extension will be selectable.
Selecting a corrupt GIF or none at all will result in a solid black
background.

--music tool--

Sidewalk can play music while the screen is off through your media PC's built-in
speakers. Pressing buttons (1-8) will play a preset playlist. Presing (9) will
play an inserted audio CD. (0) stops all playback and returns sound to the main
speakers. You can asign folders in the ./Music directory to presets using the CD
audio tool in Misc.

--backend info--

Being a frontend, Sidewalk depends on several open source Linux
applications on the "backend" to work properly.

python/pygame - interface
mplayer - runs videos, music and DVD playback
mednafen/mupen64/dolphin - runs retro game roms
feh - views photos
alsamixer - volume control tool
matchbox - window management

I have no aspirations to support a wider range of media players
or emulator cores. Sidewalk is not meant to compete with the likes
of SteamOS and Kodi, but rather written to serve the niche
needs of my wife and kids and anyone else with similar needs. The
software I have chosen integrates well, is good enough, and "just works".

Thanks for reading, and hope you enjoy your Sidewalk experience.
