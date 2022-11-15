import os
import random 
import encrypt as et

def file_write(folder, name_tag='0',encryfun=None,con=''):
    f=open(os.path.join(folder, name_tag+'_'+str(random.randint(1,10000000))+'.data'),'wb')
    #f.write(cha.encrypt(con[a:a+i]))
    if encryfun!=None:
        f.write(encryfun(con))
    else:
        f.write(con)
    f.close()

def generate_random_bytes_file(file_name, length_bytes):
    #a=os.urandom(6048000)
    a=os.urandom(length_bytes)
    f=open(file_name,'wb')
    f.write(a)
    f.close()

def generate(dir='train', data_source_file='xray.exe'):
    #if os.path.exists('train'):
    if os.path.exists(dir):
        print('folder {} had existed, please remove before generate '.format(dir))
        return 
    else:
        #os.mkdir('train')
        os.mkdir(dir)
    #f=read('xray.exe','rb')
    #f=read(data_source_file,'rb')
    f=open(data_source_file,'rb')
    con=f.read()
    f.close()
    a=0
    #aes=et.encrypt('chacha20poly1305')
    aes=et.encrypt('AES-256-GCM')
    cha=et.encrypt('chacha20poly1305')
    while a<len(con):
        #i=random.randint(100,1024)
        i=random.randint(48,168)
        #l.append(
        file_write(dir,'0',None, con[a:a+i])
        #f=open(os.path.join('train','0_'+str(random.randint(1,10000000))+'.data'),'wb')
        #f=open(os.path.join('train','0_'+str(random.randint(1,10000000))+'.data'),'wb')
        #f.write(con[a:a+i])
        #f.close()
        #file_write(dir,'1',cha.encrypt,con[a;a+i])
        file_write(dir,'1',cha.encrypt,con[a:a+i])
        #f=open(os.path.join('train','1_'+str(random.randint(1,10000000))+'.data'),'wb')
        #f.write(cha.encrypt(con[a:a+i]))
        #f.close()
        file_write(dir,'2',aes.encrypt,con[a:a+i])
        #f=open(os.path.join('train','2_'+str(random.randint(1,10000000))+'.data'),'wb')
        #f.write(aes.encrypt(con[a:a+i]))
        #f.close()
        a+=i




#import 

