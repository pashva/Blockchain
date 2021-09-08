import hashlib
i=0
hash_operation=""
while True:
    hash_operation=hashlib.sha256(f"181080049_Pashva_{i}".encode()).hexdigest()
    if hash_operation[:10] == '0000000000':
        break
    i=i+1;    

print(i)
print(hash_operation)