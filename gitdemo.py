#!/usr/bin/python3

import os,shutil
import glob,hashlib
from colorama import Fore
from sys import argv


flag=0



def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()


def handle_init():
    global flag
    flag=1
    path=os.getcwd()
    path1=path+"/git/object"
    path2=path+"/git/refs"
    path3=path+"/git/index"
    try:
        os.makedirs(path1,0o777,exist_ok=False)
        os.makedirs(path2,0o777,exist_ok=False)
        os.makedirs(path3,0o777,exist_ok=False)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


def handle_add_dot():
    global flag
    filelist=[]
    path=os.getcwd()
    dirs = os.listdir( path )
    for file in dirs:
        checkfile=path+"/"+file
        if(os.path.isfile(checkfile)):
            message = hash_file(file)
            checkpath=path+"/git/refs/"+message
            if(os.path.exists(checkpath)):
                continue
            else:
                try:
                    os.makedirs(checkpath,0o777,exist_ok=False)
                except OSError:
                    print ("Creation of the directory %s failed" % path)
                shutil.copy(file,checkpath)

def handle_add_file(file_name):
    global flag
    filelist=[]
    path=os.getcwd()
    # dirs = os.listdir( path )
    # for file in dirs:
    checkfile=path+"/"+file_name
    if(os.path.isfile(checkfile)):
        message = hash_file(file)
        checkpath=path+"/git/refs/"+message
        if(os.path.exists(checkpath)):
            pass
        else:
            try:
                os.makedirs(checkpath,0o777,exist_ok=False)
            except OSError:
                print ("Creation of the directory %s failed" % path)
            shutil.copy(file,checkpath)



def handle_status():
    path=os.getcwd()
        #print(path)
        #print(glob.glob(path))
    dirs = os.listdir( path )
    for file in dirs:
        checkfile=path+"/"+file
        if(os.path.isfile(checkfile)):
            message = hash_file(file)
            checkpath=path+"/git/refs/"+message
            if(os.path.exists(checkpath)):
                #print("yes")
                #message1 = hash_file(file)
               # message2 = hash_file(checkpath)
                #if(message1==message2):
               #     continue
               # else :
                print(Fore.GREEN +file)
                continue
            else:
                print(Fore.RED +file)



# while True:
    # command=input(Fore.WHITE + "Enter command ")
    # if(command=="git init" and flag==0):
    #     handle_init()
    # elif(command=="git status" and flag==1):
    #     handle_status()
    # elif(command=="git add ." and flag==1):
    #     handle_add_dot()
    # elif(command=="exit"):
    #     break



argc=len(argv)
# print(argc)
path=os.getcwd()
gitdir=path+"/"+"git"

if(argc==2):
    # print(argv[1])
    if(argv[1]=="init"):
        if(not os.path.isdir(gitdir)):
            handle_init()
        else:
            print("Already Created")

    if(argv[1]=="status"):
        if(os.path.isdir(gitdir)):
                handle_status()
        else:
            print("Not a git directory")
elif(argc==3):
    # print(argv[1],argv[2])
    if(os.path.isdir(gitdir)):
        if(argv[1]=="add" and argv[2]=="."):
            handle_add_dot()
        elif(argv[1]=="add"):
            handle_add_file(argv[1])
    else:
        print("Not a git directory")
else:
    print("Invalid")


