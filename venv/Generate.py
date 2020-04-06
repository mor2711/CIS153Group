import random
def generate_cred(n):
    file1 =open(n,"r")
    for i in file1.readlines():
        lastname = i.split()[1]
        if len(lastname) > 5:
            part1 = str(lastname)[0:5]
        else:
            part1 = lastname
        initial = i[0]
        username = part1 + initial
        counter = 1
        file2 =open("ad","r")
        while username in file2.read():
            username = username + str(counter)
            counter = counter + 1
        file2.close()
        pool = "abcdefghijklmnopqrstuvwxyz"
        pool2 = pool + pool.upper()
        pool3 = pool2 + "1234567890!@#$%^&*()"
        randomcharacter = [random.choice(pool3) for i in range(8)]
        password = "".join(randomcharacter)
        output = "username {} password {}".format(username,password)
        print(output)
        file2 =open("ad","a")
        file2.writelines(output + "\n")
        file2.close()
    file1.close()
    return;
generate_cred("list1.txt")
generate_cred("list2.txt")
