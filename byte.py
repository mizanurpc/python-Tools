import hashlib

s = "café"                       
b = s.encode("utf-8")            
print(len(s), len(b))           
print(b)                        


hash_val = hashlib.sha256(b"admin").hexdigest()
print("SHA256 Hash:", hash_val)
