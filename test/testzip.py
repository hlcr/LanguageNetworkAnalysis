import os,zipfile   
def Zip(target_dir):   
    target_file=os.path.basename(os.getcwd())+'.zip'  
    zip_opt=input("Will you zip all the files in this dir?(Choose 'n' you should add files by hand)y/n: ")   
    while True:   
        if zip_opt=='y':       #compress all the files in this dir   
            filenames=os.listdir(os.getcwd())    #get the file-list of this dir   
            zipfiles=zipfile.ZipFile(os.path.join(target_dir,target_file),'w',compression=zipfile.ZIP_DEFLATED)   
            for files in filenames:   
                zipfiles.write(files)   
            zipfiles.close()   
            print("Zip finished!")   
            break  
        elif zip_opt=='n':     #compress part of files of this dir   
            filenames=list(input("Please input the files' name you wanna zip:"))   
            zipfiles=zipfile.ZipFile(os.path.join(target_dir,target_file),'w',compression=zipfile.ZIP_DEFLATED)   
            for files in filenames:   
                zipfiles.write(files)   
            zipfiles.close()   
            print("Zip finished!")   
            break  
        else:   
            print("Please in put the character 'y' or 'n'")   
            zip_opt=input("Will you zip all the files in this dir?(Choose 'n' you should add files by hand)y/n: ")   


def Unzip(target_dir,target_name):
    zipfiles=zipfile.ZipFile(target_name,'r')   
    zipfiles.extractall(os.path.join(target_dir,os.path.splitext(target_name)[0]))   
    zipfiles.close()   
    print("Unzip finished!")   


Unzip('D://semantic analysis//','D://semantic analysis//testzip.rar')

# with open('D://semantic analysis//3次采集//所有目录.txt','r') as file:
#     dir_list = file.readlines();
#
# for dd in dir_list:
#     dd = dd[:-1]
#     print(dd)
#     Unzip(dir_list,dir_list+'//')