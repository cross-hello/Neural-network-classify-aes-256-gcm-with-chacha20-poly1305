import os
#from chacha20poly1305 import ChaCha20Poly1305 as cha
from Crypto.Cipher import ChaCha20_Poly1305 as cha
key=os.urandom(32)
#nonce=os.urandom(12)
from Crypto.Cipher import AES
class encrypt:
    #def __init__(self, key=b'password'*4, nonce=nonce):
    #method must choose from "chacha20poly1305" between "AES-256-GCM"
    #def __init__(self, method="chacha20poly1305", key=key, nonce=nonce):
    #def __init__(self, method="chacha20poly1305", key=key, nonce=nonce):
    def __init__(self, method="chacha20poly1305", key=key):
        self.key=key
        #self.nonce=nonce
        #if method=='cha_encrypt':
        if method=='chacha20poly1305':
            #self.instance=chacha(key)
            #self.instance=cha(key,mac_len=16)
            #self.instance=cha(key)
            #self.instance=cha.new(key)
            #self.instance=cha.new(key=key)
            #self.instance=cha.new(key=key,nonce=nonce)
            #self.instance=cha.new(key=key,nonce=nonce)
            self.instance=cha.new(key=key)
            self.encrypt=self.cha_encrypt
        elif method=="AES-256-GCM":
            #self.instance=AES.new(key, AES.MODE_GCM)
            #self.instance=AES.new(key, AES.MODE_GCM,self.nonce)
            #self.instance=AES.new(key, AES.MODE_GCM,self.nonce. mac_len=16)
            #self.instance=AES.new(key, AES.MODE_GCM,self.nonce,mac_len=16)
            self.instance=AES.new(key, AES.MODE_GCM,mac_len=16)
            self.encrypt=self.AES_256_GCM_encrypt
        elif method=='TLS-AES-128-CCM-8-SHA256':
            if len(key)!=16:
                print('Initialize TLS-AES-128-CCM-8-SHA256 with key size {}!=16'.
                        format(len(key)))
                print('allocate a new key')
                #key=os.urandom(16)
                self.key=os.urandom(16)
            #self.instance=AES.new(key, AES.MODE_CCM,mac_len=8)
            self.instance=AES.new(self.key, AES.MODE_CCM,mac_len=8)
            self.encrypt=self.tls_aes_128_ccm_encrypt
        else:
            print("method must choose from 'chacha20poly1305' between 'AES-256-GCM', 'TLS-AES-128-CCM-8-SHA256'")
            print("Create instance failed")


    def cha_encrypt(self, btext):
        #return self.instance.encrypt(self.nonce,btext)
        #i=self.instance.encrypt_and_digest(self.nonce,btext)
        i=self.instance.encrypt_and_digest(btext)
        i=i[0]+i[1]
        #self.instance=cha.new(key=key,nonce=nonce)
        self.instance=cha.new(key=key)
        return i

    def AES_256_GCM_encrypt(self, btext):
        #return self.instance.encryptpt_and_digest(btext)[0]
        #return self.instance.encrypt_and_digest(btext)[0]
        #i=self.instance.encrypt_and_digest(btext)[0]
        i=self.instance.encrypt_and_digest(btext)
        i=i[0]+i[1]
        #self.instance=AES.new(self.key, AES.MODE_GCM,self.nonce)
        #self.instance=AES.new(self.key, AES.MODE_GCM,nonce=self.nonce,mac_len=16)
        self.instance=AES.new(self.key, AES.MODE_GCM,mac_len=16)
        return i

    def tls_aes_128_ccm_encrypt(self,btext):
        i=self.instance.encrypt_and_digest(btext)
        i=i[0]+i[1]
        #self.instance=AES.new(key, AES.MODE_CCM,mac_len=8)
        self.instance=AES.new(self.key, AES.MODE_CCM,mac_len=8)
        return i

        





        

