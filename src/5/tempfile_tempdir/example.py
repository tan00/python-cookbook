from tempfile import TemporaryFile 
#匿名临时文件
with TemporaryFile('w+t') as tmpf:
    tmpf.write('Hello World\n')
    tmpf.write('Testing\n')
    tmpf.seek(0)
    data = tmpf.read()

print(data)    

#命名临时文件
from tempfile import NamedTemporaryFile
with NamedTemporaryFile('w+t',prefix='mytmpfile') as name_tmpf:
    name_tmpf.write('lin123')
    print(name_tmpf.name)
    #out C:\Users\LN\AppData\Local\Temp\tmptvu34wpr

#创建临时目录
from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)


import serial
ser = serial.Serial('/dev/tty.usbmodem641', # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)
