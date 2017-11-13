import hashlib

found = False
hashme = ''
f = open('crackme.txt', 'r')
hashedpass = f.read()
f.close()

def ComputeHash(srt):
    print(srt)
    hashme = hashlib.sha1(srt.encode())
    print(hashme.hexdigest())
    
    if hashme.hexdigest() == hashedpass:
        print("FOUND IT")   
        found = True
        return True


print(hashedpass + '\n\n')
with open('rockyou.txt') as a:
    for line in a:
              
        line = str(line)
        line = line.strip()
        
        found = ComputeHash(line)
        if found == True:
            break    
        else:
            continue          
        

#Add for loop for comparing
#add code to import rockyou.txt
