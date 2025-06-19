import psutil
import os
import time
import schedule
import sys
import smtplib
import mimetypes
from email.message import EmailMessage

def CreateLog(folderName,email):
    Data = ProcessScan()
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    
    timeStamp = time.ctime()
    timeStamp = timeStamp.replace(" ","")
    timeStamp = timeStamp.replace(":","-")
    timeStamp = timeStamp.replace("/","_")

    fileName = os.path.join(folderName,"Marvellous"+timeStamp+".log")
    fobj = open(fileName,"w")

    Border = "-"*80
    fobj.write(Border+"\n")
    fobj.write("\t\tMarvellous Infosystems Process log\n")
    fobj.write("\t\tLog file created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    for d in Data:
        fobj.write(str(d)+"\n\n")

    fobj.write(Border+"\n")
    fobj.close()
    SendMail(fileName,email)

def ProcessScan():
    
    listProcess = []
     
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listProcess

def SendMail(fName,email):
    sender_email = "demoforpython5@gmail.com"
    reciever_email = email

    timeStamp = time.ctime()
    subject = "Log file"+timeStamp
    message = "Below is file attached,consists log data of Directory cleaning.\n"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = reciever_email
    msg.set_content(message+"\nThis is an attachment demo.\n")

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

def main():

    size = len(sys.argv)

    if size == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use this script as : ");
            print("ScriptName.py dirName emailid");
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to create a log file of running process and send to your emailid.")
    elif size == 3:
        DirName = sys.argv[1]
        email = sys.argv[2]
        schedule.every(1).minutes.do(CreateLog,DirName,email)

        while True:
            schedule.run_pending()
            time.sleep(1)
        
    else:
        print("Invaid arguements.")
        print("Enter : \n1. ScriptName.py --u(For Usage).\n2. ScriptName.py --h(For Help)")

    

if __name__ == "__main__":
    main()