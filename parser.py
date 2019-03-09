passwords = []
for i in range(1):
    filename = str(i) + ".txt"
    filepath = "./Dataset/Password List/" + filename
    with open(filepath) as f:
        start = 0
        for line in f:
            credentials = line.strip().split(':')
            j = 0
            for cred in credentials:
                if(j!= 0):
                    passwords.append(cred)
                    j = 0 
                else:
                    j = 1

with open('passwords.txt', 'a+') as f:    
    for password in passwords:
        try:
            f.write("%s\n" % password)
        except IndexError:
            print ("A line in the file doesn't have enough entries.")