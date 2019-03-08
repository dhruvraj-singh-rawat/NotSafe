passwords = []
for i in range(1,98):
    filename = str(i) + ".txt"
    filepath = "./Data/" + filename
    with open(filepath) as f:
        for line in f:
            credentials = line.strip().split(':')
            i = 0
            for cred in credentials:
                if(i != 0):
                    passwords.append(cred)
                    i = 0 
                else:
                    i = 1

    with open('passwords.txt', 'a+') as f:    
        for password in passwords:
            try:
                f.write("%s\n" % password)
            except IndexError:
                print ("A line in the file doesn't have enough entries.")