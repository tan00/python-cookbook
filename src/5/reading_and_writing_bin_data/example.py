with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')


