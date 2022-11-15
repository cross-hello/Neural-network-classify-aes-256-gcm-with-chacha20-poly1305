import numpy as np
import random 
class nn:
    def __init__(self, layers):
        self.layers=layers
        self.layer_num=len(layers)
        self.baise=[np.random.randn(a,1) for a in layers[1:] ]
        self.weight=[np.random.randn(a,b)/np.sqrt(b) for a,b in zip(layers[1:], layers[:-1])]
        self.epoch_time=0
    
    def sigma(self, x):
        return 1/(1+np.exp(-x))
    def derivate_sigma(self,x):
        return self.sigma(x)*(1-self.sigma(x))

    def forward(self, x):
        for a,b in zip(self.weight, self.baise):
            #x=a*x+b
            x=np.dot(a,x)+b
            x=self.sigma(x)
        return x

    def backpropagate(self, x,y):
        ass=[x]
        zss=[]
        #cweight=[np.zeros(a.shape) for a in self.weight ]
        cweight=[0 for a in self.weight ]
        #cbaise=[np.zeros(a.shape) for a in self.baise]
        cbaise=[0 for a in self.baise]
        for a,b in zip(self.weight, self.baise):
            #x=x*a+b
            #x=x*(a.T)+b.T
            #print(x)
            #print('x.shape:',x.shape)
            #print(a)
            #print('a.shape:',a.shape)
            x=np.dot(a,x)+b
            #x=np.dot(x,a.T)+b.T
            zss.append(x)
            x=self.sigma(x)
            ass.append(x)
        delta=x-y
        #delta=y-x
        #cweight[-1]=delta*ass[-1]
        #cweight[-1]=delta*ass[-2]
        cweight[-1]=np.dot(delta,ass[-2].T)
        #cweight[-1]=np.dot(delta,ass[-2].T) // can't use matrix here
        cbaise[-1]=delta
        #for n in range(2, len(cweight)):
        for n in range(1, len(cweight)):
            #delta=delta*self.weight[1-n].T*self.derivate_sigma(zss[-n])
            #delta=np.dot(self.weight[1-n].T,delta)*self.derivate_sigma(zss[-n])
            #print('here')
            delta=np.dot(self.weight[-n].T,delta)*self.derivate_sigma(zss[-1-n])
            #cweight[-n]=delta*ass[-n-1]
            #cweight[-n]=np.dot(delta,ass[-n-1].T)
            cweight[-n-1]=np.dot(delta,ass[-n-2].T)
            cbaise[-n-1]=delta

    
        return (cweight,cbaise)

    #def THG(self, train_data_list, batch_num, learn_rate, rounds):
    #def THG(self, train_data_list, batch_num, learn_rate, epoches, validate_data_list=None):
    def THG(self, train_data_list,validate_data_list, batch_num, learn_rate, epoches):
        #while _ in range(rounds):

        #while n in range(epoches):
        #for n in range(epoches):
        for _ in range(epoches):
            #train_data_list=random.shuffle(train_data_list)
            random.shuffle(train_data_list)
            batch=[train_data_list[a:a+batch_num] for a in range(0,len(train_data_list),batch_num)]
            for aa in batch:
                #x=[a[0] for a in batch]
                #y=[a[1] for a in batch]
                x=[]
                y=[]
                #for a in batch:
                #    x.append(a[0])
                #    y.append(a[1])
                #for b in batch:
                for b in aa:
                    x.append(b[0])
                    y.append(b[1])
                #z=(x,y)
                #print('len(x):', len(x))
                #print('len(y):',len(y))
                x=self.batch_update(x,y)
                #print('len(aa):',len(aa))
                #print('len(x[0]): ',len(x[0]))
                #print('len(x[1]): ',len(x[1]))
                #return  z
                #self.weight=[a-b*learn_rate for a,b in zip(self.weight,x[0]) ]
                #self.weight=[a-b*learn_rate/len(x) for a,b in zip(self.weight,x[0]) ]
                #self.weight=[a-b*learn_rate/len(x[0]) for a,b in zip(self.weight,x[0]) ]
                self.weight=[a-b*learn_rate/len(aa) for a,b in zip(self.weight,x[0]) ]
                #self.baise=[a-b*learn_rate for a,b in zip(self.baise,x[1])  ]
                #self.baise=[a-b*learn_rate/len(y) for a,b in zip(self.baise,x[1])  ]
                #self.baise=[a-b*learn_rate/len(x[1]) for a,b in zip(self.baise,x[1])  ]
                self.baise=[a-b*learn_rate/len(aa) for a,b in zip(self.baise,x[1])  ]
            #print('epoch {} loss:{}%'.fomrat(n, self.validate(train_data_list)))
            print('epoch {}\n\t\t loss:{}%'.format(self.epoch_time, self.validate(validate_data_list)))
            self.epoch_time+=1
            #print('epoch {}\n\t\t loss:{}%'.format(n, self.validate(train_data_list)))
            #print('epoch {}\n\t\t loss:{}%'.format(n, self.validate(validate_data_list)))
            '''
            if validate_data_list==None:
                print('epoch {}\n\t\t loss:{}%'.format(self.epoch_time, self.validate(train_data_list)))
            else:
                print('epoch {}\n\t\t loss:{}%'.format(self.epoch_time, self.validate(validate_data_list)))
            '''
                 
    def batch_update(self, xl,yl):
        #x=[np.expand_dims(a,-1) for a in x1]
        #x=[np.expand_dims(a,-1) for a in xl]
        #y=[np.expand_dims(a,-1) for a in yl]
        #w,b=self.backpropagate(x,y)
        #x=np.array(xl) //for matrix 
        #y=np.array(yl)// for mtarix
        #w,b=self.backpropagate(xl,yl)// for mtarix
        #w=[a for a in w ]// for mtarix
        cweight=[np.zeros(a.shape) for a in  self.weight]
        cbaise=[np.zeros(a.shape) for a in self.baise ]
        for aa, bb in zip(xl,yl):
            x=self.backpropagate(aa,bb)
            #cweight+=x[0]
            cweight=[a+b  for a, b in zip (cweight,x[0])]
            #cbaise+=x[1]
            cbaise=[a+b for a, b in zip(cbaise, x[1])]
        #return (cweight/len(xl), cbaise/len(yl))
        return (cweight,cbaise)

    def validate(self, data):
        n=0
        for a in data:
            x=self.forward(a[0])
            if x.argmax()==a[1].argmax():
                n+=1
        #return n/(len(data)*100)
        #return n*100/len(data)
        return (1-n/len(data))*100
    def save_model(self, weight_array_name='weight.npy', baise_array_name='baise.npy'):
        #np.save(weight_array_name,self.weight)
        a=np.asanyarray(self.weight)
        np.save(weight_array_name,a)
        a=np.asanyarray(self.baise)
        #np.save(baise_array_name,self.baise)
        np.save(baise_array_name,a)

    def restore_model(self, weight_array_name='weight.npy', baise_array_name='baise.npy'):
        #np.load(weight_array_name, self.weight)
        self.weight=np.load(weight_array_name, allow_pickle=True )
        #np.load(baise_array_name, self.baise)
        self.baise=np.load(baise_array_name, allow_pickle=True)
        a=[b.shape[0] for b in self.baise]
        a=[self.weight[0].shape[1]]+a
        self.layers=a








        

    





    #def THG(self)
