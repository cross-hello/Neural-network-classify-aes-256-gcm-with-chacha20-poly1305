import glob
import os
import re
import numpy as np
limit=188
num_dic={}
def get_digit(name):
    global num_dic
    #return re.findall('([0-9])_',name)[0]
    a=re.findall('([0-9])_',name)[0]
    return a

def get_file_label(file_name='labels'):
    f=open(file_name,'r')
    con=f.read().split('\n')
    f.close()
    con.remove('')
    return con

def digit2num(s):
    global num_dic
    if s in num_dic:
        num_dic[s]+=1
    else:
        num_dic[s]=1
    #num=len(get_label_list())
    num=len(get_file_label())
    #a=np.zeros((3,1))
    a=np.zeros((num,1))
    #a=np.zeros((2,1))
    a[int(s)]=1
    return a

def get_label_list(file_name='labels'):
    #f=open(file_name,'r')
    #con=f.read().split('\n')
    #f.close()
    con=get_file_label(file_name)
    ll=[]
    global num_dic
    for a in num_dic:
        ll.append((con[int(a)],num_dic[a]))
    #return con
    return ll

def get_memory(li):
    global limit, num_dic
    num_dic={}
    ll=[]
    for a in li:
        con=a[0]
        if len(con)<limit:
            #con+=(1024-len(con))*b'0'
            #con+=(limit-len(con))*b'0'
            con+=(limit-len(con))*b'\0'
        #fm=np.array(con
        #fm=np.frombuffer(con,dtype=np.uint8).reshape((1024,1))/255
        fm=np.frombuffer(con,dtype=np.uint8).reshape((limit,1))/255
        #an=digit2num(get_digit(a))
        #an=digit2num(get_digit(a[1]))
        an=digit2num(a[1])
        ll.append((fm,an))
    return ll


def get(dir='train'):
    global num_dic
    num_dic={}
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



