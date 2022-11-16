import glob
import os
import re
import numpy as np
limit=188
def get_digit(name):
    return re.findall('([0-9])_',name)[0]

def digit2num(s):
    a=np.zeros((3,1))
    a[int(s)]=1
    return a

def get_memory(li):
    global limit
    ll=[]
    for a in li:
        con=a[0]
        if len(con)<limit:
            #con+=(1024-len(con))*b'0'
            con+=(limit-len(con))*b'0'
        #fm=np.array(con
        #fm=np.frombuffer(con,dtype=np.uint8).reshape((1024,1))/255
        fm=np.frombuffer(con,dtype=np.uint8).reshape((limit,1))/255
        #an=digit2num(get_digit(a))
        #an=digit2num(get_digit(a[1]))
        an=digit2num(a[1])
        ll.append((fm,an))
    return ll


def get(dir='train'):
    l=glob.glob(os.path.join(dir,'*.data'))
    ll=[]
    #limit=1044
    #limit=188
    global limit
    for a in l:
        f=open(a,'rb')
        con=f.read()
        f.close()
        #if len(con)<1024:
        if len(con)<limit:
            #con+=(1024-len(con))*b'0'
            con+=(limit-len(con))*b'0'
        #fm=np.array(con
        #fm=np.frombuffer(con,dtype=np.uint8).reshape((1024,1))/255
        fm=np.frombuffer(con,dtype=np.uint8).reshape((limit,1))/255
        an=digit2num(get_digit(a))
        ll.append((fm,an))
    return ll



