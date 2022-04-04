import shutil
import subprocess
import os
from os import system

filepath_md = 'modrinth_list.txt'

with open(filepath_md) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("packwiz modrinth install {}".format(line.strip()))
       subprocess.run("packwiz modrinth install {}".format(line.strip()) , shell=True)
       line = fp.readline()
       cnt += 1
       
filepath_cf = 'curseforge_list.txt'

with open(filepath_cf) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("packwiz curseforge install {}".format(line.strip()))
       subprocess.run("packwiz curseforge install {}".format(line.strip()) , shell=True)
       line = fp.readline()
       cnt += 1
