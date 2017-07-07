import gzip 
with  gzip.open('smaple.gz','wb') as f:
    f.write(b'bin data')

with  gzip.open('smaple.gz','rb') as f2:
    print( f2.read() ) 


f3 = open('smaple.gz', 'rb')
with gzip.open(f3, 'rt') as g:
    print( g.read() )