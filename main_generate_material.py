import generate_train_material as gl
gl.generate('train','xray.exe')
gl.generate_random_bytes_file('validate_random_data',3600*24*7)
gl.generate('validate','validate_random_data')

