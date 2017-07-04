
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

num = int.from_bytes(data,'little')
print(num)

data2 = num.to_bytes(16,'little')
print(data2)


