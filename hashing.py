import hashlib
filename = "D:\Users\91848\hello\sampleFile.txt"
filelocation = open(filename, "w+")
filelocation.write("My Name is Sam")
filelocation.close()
filelocation = open("sampleFile.txt", "w+")
message = filelocation.read()
encoded = hashlib.sha256(message.encode())
filelocation.write(encoded.hexdigest())
filelocation.close()
