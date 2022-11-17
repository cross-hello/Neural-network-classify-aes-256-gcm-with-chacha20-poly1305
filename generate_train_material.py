import os
import random 
import encrypt as et

def memory_write(con, encryfun=None, name_tag='0'):
   if encryfun==None:
       return (con,name_tag)
   else:
       return (encryfun(con),name_tag)

def file_write(folder, name_tag='0',encryfun=None,con=''):
    f=open(os.path.join(folder, name_tag+'_'+str(random.randint(1,10000000))+'.data'),'wb')
    if encryfun!=None:
        f.write(encryfun(con))
    else:
        f.write(con)
    f.close()

def generate_random_bytes_memory(length_bytes):
    a=os.urandom(length_bytes)
    return a

def generate_random_bytes_file(file_name, length_bytes):
    a=os.urandom(length_bytes)
    #a=os.urandom(6048000)
    f=open(file_name,'wb')
    f.write(a)
    f.close()

def read_file(file_name):
    f=open(file_name,'rb')
    con=f.read()
    f.close()
    return con

def generate_memory(con, length=None):
    a=0
    aes=et.encrypt('AES-256-GCM')
    cha=et.encrypt('chacha20poly1305')
    aes128=et.encrypt('TLS-AES-128-CCM-8-SHA256')
    l=[]
    #name_flags={'0':None,'1':cha.encrypt,'2':aes.encrypt}
    name_flags={'0':cha.encrypt,'1':aes.encrypt,'2':aes128.encrypt}
    while a<len(con):
        if length==None:
            i=random.randint(48,168)
        else:
            i=length
        temcon=con[a:a+i]
        for aa in name_flags:
                l.append(memory_write(temcon,name_flags[aa],aa))
        a+=i
    return l

#def generate_file(con):
def generate_file(con, length=None):
    a=0
    aes=et.encrypt('AES-256-GCM')
    cha=et.encrypt('chacha20poly1305')
    aes128=et.encrypt('TLS-AES-128-CCM-8-SHA256')
    #name_flags={'0':None,'1':cha.encrypt,'2':aes.encrypt}
    name_flags={'0':cha.encrypt,'1':aes.encrypt,'2':aes128.encrypt}
    while a<len(con):
        if length==None:
            i=random.randint(48,168)
        else:
            i=length
        temcon=con[a:a+i]
        for aa in name_flags:
            file_write(dir,aa,name_flags[aa],temcon)
        a+=i



