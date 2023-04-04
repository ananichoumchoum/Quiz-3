#Quiz 3 lab2
#Anne-Marie SMith
#os.path.getctime(path) to return last metadata change
import os
filename = []
#get the files in the directory requested
def getloginfo(directory):
    file_dict = {}
    for path, folder, files in os.walk(directory):
        for afile in files:
            #only select the files that are logs (end with .log)
            if os.path.splitext(afile)[1] == '.log':
                filename.append(os.path.join(path, afile))
                file_dict.setdefault(afile, [])
                answer = path + '_' + str(os.path.getmtime(path + '/' + afile))
                file_dict[afile].append(answer)
    return file_dict
#ask for which directory we want to find log files 
directory = input("please write the path of the directory you want to investigate(ex: /var/log): " )
dictionary = getloginfo(directory)

#print the login info
for x in filename:
    f = open(x, "r")
    
    print(x)
f.close()
