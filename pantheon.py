# REQUIREMENTS

from pyfade import Fade, Colors
from pycenter import center
from requests import get

from os import system, mkdir, name
from os.path import isdir
from base64 import b64decode as bd


def clear():
    system("cls" if name == 'nt' else "clear")


clear()

if name == 'nt':
    system("title Pantheon")
    system("mode 160, 50")

class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "orange" : "\033[38;2;255;100;0m", 
              "yellow" : "\033[38;2;255;255;0m",
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    orange = colors['orange']

    yellow = colors['yellow']
    
    white = colors['white']


pantheon = """

                          L.                                           ,;     t#,     L.
 t                        EW:        ,ft           .    .            f#i     ;##W.    EW:        ,ft
 ED.                   .. E##;       t#E GEEEEEEEL Di   Dt         .E#t     :#L:WE    E##;       t#E
 E#K:                 ;W, E###t      t#E ,;;L#K;;. E#i  E#i       i#W,     .KG  ,#D   E###t      t#E
 E##W;               j##, E#fE#f     t#E    t#E    E#t  E#t      L#D.      EE    ;#f  E#fE#f     t#E
 E#E##t             G###, E#t D#G    t#E    t#E    E#t  E#t    :K#Wfff;   f#.     t#i E#t D#G    t#E
 E#ti##f          :E####, E#t  f#E.  t#E    t#E    E########f. i##WLLLLt  :#G     GK  E#t  f#E.  t#E
 E#t ;##D.       ;W#DG##, E#t   t#K: t#E    t#E    E#j..K#j...  .E#L       ;#L   LW.  E#t   t#K: t#E
 E#ELLE##K:     j###DW##, E#t    ;#W,t#E    t#E    E#t  E#t       f#E:      t#f f#:   E#t    ;#W,t#E
 E#L;;;;;;,    G##i,,G##, E#t     :K#D#E    t#E    E#t  E#t        ,WW;      f#D#;    E#t     :K#D#E
 E#t         :K#K:   L##, E#t      .E##E    t#E    f#t  f#t         .D#;      G#t     E#t      .E##E
 E#t        ;##D.    L##, ..         G#E     fE     ii   ii           tt       t      ..         G#E
            ,,,      .,,              fE      :                                                   fE

"""

author = "   - - - {} - - -".format(bd("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))

print(Fade.Vertical(Colors.red_to_yellow, center(pantheon)))
print(Fade.Horizontal(Colors.yellow_to_red, center(author)))


print()

print(Col.orange+center("   Pantheon - The fastest YouTube video downloader.")+Col.white)

print("\n\n")

video_url = input(Col.yellow+"Video url > "+Col.white)
video_id = video_url.split("watch?v=")[-1]
video_id = video_id.split("&")[0]

print()

def get_title(id) -> str:
    verify_url = "https://www.youtube.com/oembed?format=json&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D" + id
    response = get(verify_url)
    if response.status_code == 400:
        return False
    json = response.json()
    return json["title"]


video_title = get_title(video_id)

if not video_title:
    input(Col.red+"Invalid URL!"+Col.white)
    exit()

else:
    print(Col.orange+"Video title: "+Col.white+video_title)

print()

mode = input(Col.yellow+"1: MP3 - 2: MP4 > "+Col.white)

print()

if mode == '1':
    download_url = "https://www.yt-download.org/api/button/mp3/"
elif mode == '2':
    download_url = "https://www.yt-download.org/api/button/videos/"
else:
    input(Col.red+"Invalid mode!"+Col.white)
    exit()


download_url += video_id

print(Col.orange+"Getting download link...\n"+Col.white)

response = get(download_url).text
response = response.split('"')
textures = list(reversed([link for link in response if video_id in link]))

if mode == '1':
    quality = input(Col.yellow+"1: 128kbps - 2: 192kbps - 3: 256kbps - 4: 320kbps > "+Col.white)
elif mode == '2':
    if len(textures) == 1:
        quality = input(Col.yellow+"1: 360p > "+Col.white)
    else:
        quality = input(Col.yellow+"1: 360p - 2: 720p > "+Col.white)

print()

try:
    quality = int(quality)
except ValueError:
    input(Col.red+"Please enter an integer!"+Col.white)
    exit()


if quality > len(textures):
    input(Col.red+"Invalid choice!"+Col.white)
    exit()


download_url = textures[quality-1]

print(Col.orange+"Downloading...\n\n"+Col.white)

content = get(download_url).content



if not isdir("Downloads"):
    mkdir("Downloads")


if mode == '1':
    file = ".mp3"
elif mode == '2':
    file = ".mp4"


for char in ('\\', '/', ':', '*', '?', '"', '<', '>', '|'):
    video_title = video_title.replace(char, '')

path = "Downloads/" + video_title + file

with open(path, 'wb') as f:
    f.write(content)


input(Col.red+"Downloaded!"+Col.white)
