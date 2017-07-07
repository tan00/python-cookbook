import functools 
import io

BLOCKSIZE = 4

bytef = io.BytesIO()
bytef.write(b'binary data')
bytef.seek(0)

records = iter( functools.partial(bytef.read,BLOCKSIZE)  , b'' )
print (  [ r for r in records ] )
#out  [b'bina', b'ry d', b'ata']



