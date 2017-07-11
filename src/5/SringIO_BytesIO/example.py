import io 

stringf = io.StringIO()
stringf.writelines('hello world\n')
stringf.writelines('hello lin')

stringf.seek(0)
print( stringf.readlines() )

bytef = io.BytesIO()
bytef.write(b'binary data')
print( bytef.getvalue() )
