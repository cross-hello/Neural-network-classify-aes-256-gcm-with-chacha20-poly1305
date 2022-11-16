import generate_train_material as gl
#for generated material stored in file
gl.generate('train','xray.exe', return_mode='file')
#l=gl.generate('train','xray.exe', return_mode='memory')
gl.generate_random_bytes_file('validate_random_data',3600*24*7)
gl.generate('validate','validate_random_data')

