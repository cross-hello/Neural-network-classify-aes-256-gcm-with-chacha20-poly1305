## Neural Network classify AES-256-GCM between chacha20poly1305

The experiment conculsion is the neural network model can't distinguish data from  AES-256-GCM or chacha20poly1305, and unmodified source.

After  some epoches, loss  rate wander around 63%. Total only three possibility.

![conclusion](conclusion.PNG)

### Steps replicate

```python

#generate three form data: unmodified data, AES-256-GCM 
#encryption data, chacha20poly1305 encryption data.
import generate_train_material as gl
#con=gl.read_file('xray.exe')
con=gl.generate_random_bytes_memory(3600*24*7)
rough_train_data=gl.generate_memory(con)
randoms=gl.generate_random_bytes_memory(3600*24*7)
rough_validate_data=gl.generate_memory(randoms)
#feed module
import  read_train_material as ra
#train_data=rs.get('train')
train_data=ra.get_memory(rough_train_data)
valida_data=ra.get_memory(rough_validate_data)
#valida_data=ra.get('validate')
import neural_network_cross_entropy as ne
A=ne.nn([188,30,3])
A.THG(train_data, valida_data, 20,1,30)
```
