inputfile = "../file_name.txt"
outputfile = "../newfile_name.txt"

myfile = open(inputfile, mode='r', encoding='latin_1')
for line in myfile:
    print(myfile.read())
    # print(line.strip())

# вывести толко несколько строк, содержащих фамилию Ivanov
# myfile = open(inputfile, mode='r', encoding='latin_1')
# for num, line in enumerate(myfile, 1):
#     if "Ivanov" in line:
#         print("Line N:" + str(num) + " : " + line.strip())


# перезаписываем пароли в файл
inputfile = "../file_name.txt"
outputfile = "../newfile_name.txt"

password_tolookfor = "vasia"
#  берем из myfile1 и закидываем в myfile2
myfile1 = open(inputfile, mode='r', encoding='latin_1')
# инимение! режим w - перезаписывает, а для добавления mode='a'
myfile2 = open(inputfile, mode='w', encoding='latin_1')

for num, line in enumerate(myfile, 1):
    if password_tolookfor in line:
        print("Line N:" + str(num) + " : " + line.strip())
        myfile2.write("Found password" + line)

myfile1.close()
myfile2.close()