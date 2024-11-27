from utils import install_pkg

import subprocess
import os
import time
import re

install_pkg('requests')

import requests


def download_file(url, fn):
    rp = requests.get(url)

    if rp.status_code == 200:
        with open(fn, 'wb') as dgf:
            dgf.write(rp.content)
        print('Success full downloaded the game')
    else:
        print('Failed to download file. Status code:', rp.status_code)

def is_file_downloaded(fn):
    return os.path.isfile(fn) and os.path.getsize(fn) > 0

def spy():
    print('Start extacting game-link ...')
    fn = input('File Name: ')
    with open(fn + '.html', "r") as f:
        data = f.read()
        uid = str(time.time() * 1000)
    
        start_delim = "scriptSrc = '"
        end_delim = "'"
    
        si = data.find(start_delim) + len(start_delim)
        if si == -1:
            raise ValueError("Start Delim not found string")
    
        ei = data.find(end_delim, si)
        if ei == -1:
            raise ValueError("End Delim not found string")
    
        gl = data[si:ei]
    
        print('Found game link:', gl)
        print('Start downloading the game ...')
    
        dgl = '___spygame_downloaded__' + uid
    
        pattern = r'(https?://[^\s]+)'
    
        download_file(gl, dgl)
    
        if is_file_downloaded(dgl):
            with open(dgl, "r") as f:
                dgdt = f.read()
    
            game = dgdt.replace('al_renderHtml({"html":', '', 1).strip()
            index = game.rfind("});")
            if index != -1:
                fng = game[:index]
            else:
                fng = game
    
            matches = re.findall(r'(https?://[^\s]+)', fng)
    
            print("\n------------------------------")
    
            for match in matches:
                print("Found game store link:", match)
    
            jsg = 'const x = ' + fng + '\n' + 'var fs = require("fs")\nfs.writeFile("' + fn + '_pts_spy_game' + uid + '.html", x, (err) => { if(err) { console.error(err); return; } console.log("SUCCESS") })'
    
            print("------------------------------\n")
            gfn = '___spygame___' + uid + '.js'
            with open(gfn, 'w') as gf:
                gf.write(jsg)
    
            subprocess.run(["node", gfn])
    
            if os.path.exists(gfn):
                os.remove(gfn)
            if os.path.exists(dgl):
                os.remove(dgl)
