#Accept directory name and delete duplicate files.
#Create one directory named 'Marvellous' maintain all log files fName : abc{datetime}.log
#Accept time interval to perform task
#Accept mail id and send log file as attachment
#Mail body should contain statstics about the operation of file removal
#Mail body should contain below things :
#Starting time of Scan
#Total number of files scanned
#Total number of duplicates found


# methods
# CreateLog
# sendMail
# FindDuplicate
# DeleteDuplicate
# GetCheckSum

# Added email regex for valid email input

import os 
import sys
import schedule
import time
import re
import hashlib
import smtplib
from email.message import EmailMessage
import mimetypes
import datetime

def CheckSum(fPath,BlockSize = 1024):
    fobj = open(fPath,"rb")                         #Opened in binary mode(because accepts all types files)

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirName):
    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    Duplicate = {}

    for FolderName , SubFolderNames, FileNames in os.walk(DirName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)   #abs Path for that particular file
            checksum = CheckSum(fname,1024)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate


def SendMail(fName,TotalDeleted,TotalScans, Start ,email):
    sender_email = "demoforpython5@gmail.com"
    reciever_email = email

    timeStamp = time.ctime()

    subject = "Log file"+timeStamp
    message = "Below is file attached,consists log data of Directory cleaning.\nThis is an attachment demo.\n"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = reciever_email
    msg.set_content(message+"\nStart time of scan : "+str(Start)+"\nTotal Scans : "+str(TotalScans)+"\nTotal files deleted : "+str(TotalDeleted)+"\n")

    fName = os.path.abspath(fName)
    mime_type, _ = mimetypes.guess_type(fName)
    mime_type, mime_subtype = mime_type.split('/')

    with open(fName, 'rb') as file:
        msg.add_attachment(file.read(),
                       maintype=mime_type,
                       subtype=mime_subtype,
                       filename=os.path.basename(fName))
        
    

    try : 
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,"mqvrzhbnqxpkmruc")
        server.send_message(msg)

        print("Mail sent to :",reciever_email)
    except Exception as e:
        print("Failed to send the mail : ",e)

def CreateLog(DeletedDuplicates,TotalDeleted,TotalScans,Start,email):

    Destination = "Marvellous"

    flag = os.path.isdir(Destination)
    timeStamp = time.ctime()

    Border = "-"*80

    if flag:
        logFile = "DeletedFiles_"+timeStamp+".log"
        logFilePath = os.path.join(Destination,logFile)

        log = open(logFilePath,"w")

        log.write(Border+"\n")
        log.write("\tThis log file contains data of periodically performed directory cleaning\n")
        log.write(Border+"\n")

        for file in DeletedDuplicates:
            log.write(file+"\n")
        
        log.write(Border+"\n")
        log.write("\tTotal Scans : "+str(TotalScans)+"\n")
        log.write("\tTotal deleted files : "+str(TotalDeleted)+"\n")
        log.write(Border+"\n")

        log.close()
        SendMail(logFilePath,TotalDeleted, TotalScans, Start, email)

    else:
        os.mkdir(Destination)
        CreateLog(DeletedDuplicates,TotalDeleted,TotalScans,Start,email)


def DeleteDuplicate(DirName,email):
    Start = datetime.datetime.now()
    Duplicates = FindDuplicate(DirName)

    Result = list(filter(lambda x : len(x) > 1, Duplicates.values()))

    OriginalCount = 0
    Cnt = 0
    tCnt = 0

    DeletedFiles = list()

    for value in Result:
        for subvalue in value:
            tCnt += 1
            OriginalCount += 1
            if(OriginalCount > 1):
                DeletedFiles.append(subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        OriginalCount = 0

    CreateLog(DeletedFiles,Cnt,tCnt,Start,email)


def main():
    Border = "-"*80
    print(Border)
    print("--------------------------Vrishabha's Automation Demo---------------------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script.\nSends updates via mail.")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory(Abs Path) timeinterval reciever_EmailId")
            print("Please provide valid absolute path")

    if(len(sys.argv) == 4):
        DirName = sys.argv[1]

        flag = os.path.isdir(DirName)

        if flag == False:
            print("Enter proper directory Name.")
            exit()
        
        try:
            duration = int(sys.argv[2])
        except ValueError as vobj:
            print("Enter values in proper sequence : \nFileName.py DirectoryName timeInterval(Integer) email_id")

        regex = r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        email = sys.argv[3]

        valid = re.match(regex,email)

        if valid == None:
            print("Enter Vaid email id.")
            exit()
            
        # DeleteDuplicate(DirName,email)
        print("Directory name :",DirName,"Duration :",duration,"Email id :",email)
        schedule.every(duration).minutes.do(DeleteDuplicate,DirName,email)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("File_Name.py --h : Used to display the help")
        print("File_Name.py --u : Used to display the usage") 


    print(Border)
    print("------------------------Thank you for using my Automation-----------------------")
    print(Border)

if __name__ == "__main__":
    main()