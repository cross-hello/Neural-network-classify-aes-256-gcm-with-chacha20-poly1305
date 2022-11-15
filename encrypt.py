import os
from chacha20poly1305 import ChaCha20Poly1305 as cha
key=os.urandom(32)
nounce=os.urandom(12)
from Crypto.Cipher import AES
class encrypt:
    #def __init__(self, key=b'password'*4, nounce=nounce):
    #method must choose from "chacha20poly1305" between "AES-256-GCM"
    def __init__(self, method="chacha20poly1305", key=key, nounce=nounce):
        self.key=key
        self.nounce=nounce
        #if method=='cha_encrypt':
        if method=='chacha20poly1305':
            #self.instance=chacha(key)
            self.instance=cha(key)
            self.encrypt=self.cha_encrypt
        elif method=="AES-256-GCM":
            #self.instance=AES.new(key, AES.MODE_GCM)
            self.instance=AES.new(key, AES.MODE_GCM,self.nounce)
            self.encrypt=self.AES_256_GCM_encrypt
        else:
            print("method must choose from 'chacha20poly1305' between 'AES-256-GCM'")
            print("Create instance failed")


    def cha_encrypt(self, btext):
        return self.instance.encrypt(self.nounce,btext)

    def AES_256_GCM_encrypt(self, btext):
        #return self.instance.encryptpt_and_digest(btext)[0]
        #return self.instance.encrypt_and_digest(btext)[0]
        i=self.instance.encrypt_and_digest(btext)[0]
        self.instance=AES.new(self.key, AES.MODE_GCM,self.nounce)
        return i





        

