importemail
fromemailimportpolicy
fromgenericpathimportexists
importsys
importos
importre
fromtypingimportFinal
importcolorama
importextract_msg
fromcoloramaimportFore
colorama.init(autoreset=True)

global count

iflen(sys.argv) <2orlen(sys.argv) >2:
        exit
else:
        emailFName = sys.argv[1]
        emailFNameF = "Attachments"
        c_path = os.getcwd()
        exportedPath = os.path.join(c_path, emailFNameF)

        try:
            ifos.path.exists(exportedPath) isTrue:
                exit
            else:
                os.mkdir(exportedPath)
        except:
            print("Creating The Path: " + exportedPath)

deffileChecker():

    ifsys.argv[1].endswith('.msg'):
        msgGrabber(sys.argv[1])
    elifsys.argv[1].endswith('.eml'):
        baseGrabber()
    else:
        print(Fore.RED + "The file is in " + sys.argv[1].split(".")[-1] + " format: " + sys.argv[1])

defmsgGrabber(file):

    try:
        print(Fore.CYAN + "[+] ��������: " + file + "\n")
        withextract_msg.openMsg(file) asmessageFile:
            print(Fore.GREEN + "[+] ��: " + Fore.RESET + str(messageFile.sender))
            print(Fore.GREEN + "[+] �: " + Fore.RESET + str(messageFile.to))
            print(Fore.GREEN + "[+] �������: " + Fore.RESET  + str(messageFile.subject))
            print(Fore.GREEN + "[+] CC: " + Fore.RESET  + str(messageFile.cc))
            print(Fore.GREEN + "[+] BCC: " + Fore.RESET  + str(messageFile.bcc))
            print(Fore.GREEN + "[+] ���������������������: " + Fore.RESET  + str(messageFile.receivedTime))
            iflen(messageFile.attachments) >0:
                print(Fore.GREEN + "[+] ��������������� � ���������������������!\n\n")
                forattachmentinmessageFile.attachments:
                     attachmentName = attachment.getFilename()
                     print(Fore.CYAN + attachmentName + "\n")
                     attachment.save(customPath= exportedPath)
            else:
                print(Fore.GREEN + "[+] �������� �� �����������")
            messageBody = str(messageFile.body)
            trucatedBody = messageBody.replace('\r', ' ')
            print(Fore.GREEN + "[+] ����������������\n\n" + Fore.YELLOW + trucatedBody)
            msgIPGrabber(trucatedBody)
            msgEmailGrabber(trucatedBody)
            msgURLGrabber(trucatedBody)
            messageFile.close()
    except:
        print("���-�������������msgGrabber!")

defmsgIPGrabber(bodyWell):

        IP = [] 
        IP_COUNT = 0
        regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',bodyWell)
        
        try:
            ifregexisnotNone:
                formatchinregex:
                    ifmatchnotinIP:
                        IP.append(match)
                        IP_COUNT += 1
                        print("\n" + str(IP_COUNT) + Fore.Green + " - ���������: " + match)
        except:
            print("���-�� ����� �� ��� ��� ������� IP-������� MSG")

defmsgEmailGrabber(emailBody):
        
        EMAIL = [] 
        regex = re.findall(r'[\w\.-]+@[\w\.-]+', emailBody)
        
        try:
            ifregexisnotNone:
                print(Fore.GREEN + "[+] ����������� ������, ����������� � ���� ������\n")
                formatchinregex:
                    ifmatchnotinEMAIL:
                        EMAIL.append(match)
                        print(match)
            print("\n")
        except:
            print("���-�� ���� �� ��� ��� ������� ����������� ����� MSG")

defmsgURLGrabber(urlFile):

        try:
            print(Fore.GREEN + "[+] ����������� URL\n\n") 
            URL = [] 
            regex = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]',urlFile)
            ifregexisnotNone:
                formatchinregex:
                    urlFound = str(match)
                    urlFound = re.sub("[(\']", "", urlFound)
                    urlFound = re.sub(">", "", urlFound)
                    urlFound = re.sub("<", "", urlFound)
                    print(urlFound.strip())
        except:
            print("���-�� ���� �� ��� � URL-������ MSG")

defbaseGrabber():

  try: 
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "����� ��� ������ �������� ����� �������������, � ������� ��� ������� ������������!")
        print(Fore.BLUE + "-"*50 + "\n")
        count = 0
        withopen(sys.argv[1], "r", encoding="utf-8") assample:
            forlineinsample:
                ifline.startswith("��: "):
                    print(Fore.RED + line)
                ifline.startswith("�: "):
                    print(Fore.YELLOW + line)   
                ifline.startswith("�������: "):
                    print(Fore.GREEN + line)
                ifline.startswith("����: "):
                    print(Fore.RED + line) 
                ifline.startswith("����������������������: "):
          print(Fore.GREEN + line)
                ifline.startswith("������������:"):
                    print(Fore.YELLOW + line)
                ifline.startswith("����������:"):
                    print(Fore.GREEN + line)
                ifline.startswith("List-Unsubscribe:"):
                    print(Fore.YELLOW + line)
                ifline.startswith("Message Body: "):
                    print(Fore.GREEN + line)
                ifline.startswith("Received: "):
                    count += 1

        print("+>����������������������: " + str(count) + "\n")
    
  exceptException:
        print("���-�� ����� �� ��� � Base Grabber!")
        exit

    finally:
        emailGrabber()

defemailGrabber():
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "������������������������!")
  print(Fore.BLUE + "-"*50)

    try:
        fileOpen = open(sys.argv[1],'r', encoding='utf-8')
        readText = fileOpen.read()
        EMAIL = [] 
        regex = re.findall(r'[\w\.-]+@[\w\.-]+', readText)
        ifregexisnotNone:
            formatchinregex:
                ifmatchnotinEMAIL:
                    EMAIL.append(match)
                    print(Fore.YELLOW + match + "\n")

        
    except:
        print("���-�� ����� �� ��� � EmailGrabber!")
        exit

    finally:
        ipGrabber()

defipGrabber():
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "����������������������IP-�������!")
  print(Fore.BLUE + "-"*50)
    
    try:
        fileOpen = open(sys.argv[1],'r', encoding='utf-8')
        readText = fileOpen.read()
        IP = [] 
        IP_COUNT = 0
        regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',readText)
        ifregexisnotNone:
            formatchinregex:
                ifmatchnotinIP:
                    IP.append(match)
                    IP_COUNT += 1
                    print("\n" + str(IP_COUNT) + Fore.YELLOW + " - ���������: " + match)
    
    except:
        print("���-�� ����� �� ��� IP Grabber!")
        exit
    
    finally:
        urlGrabber()

defurlGrabber():
    print("\n")
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "������������ URL!")
    print(Fore.BLUE + "-"*50 + "\n")
    
    # try:
    fileOpen = open(sys.argv[1],'r', encoding='utf-8')
    readText = fileOpen.read()
    print(re.search("(?P<url>https?://[^\s]+)", readText).group("url"))  
    URL = [] 

    regex = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]',readText)
    
    try:
        ifregexisnotNone:
                formatchinregex:
                    ifmatchnotinURL:
                        print(match)
                        URL.append(match)
        ifnotURL:
            print(Fore.GREEN + "URL-���������������!")
  except:
        print("���-�� ����� �� ��� � URL Grabber")
    
    finally:
        xHunter()
    
defxHunter():
    print("\n")
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "������ ���� ����������, ������� ���� ��������� �� ����� �������� ����������� �����")
  print(Fore.BLUE + "-"*50 + "\n")

    try:
        withopen(sys.argv[1],'r', encoding='utf-8') assample:
                forlineinsample:
                    ifline.startswith("X-"):
                        print(Fore.YELLOW + line)
    except:
        print("���������� X �� �����������")
    
    finally:
        embedAttachments()
        
defembedAttachments():
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "�������� ������� �����-���� ��������")
    print(Fore.BLUE + "-"*50)

    try:
        withopen(sys.argv[1], "r") asf:
            attachFile = email.message_from_file(f, policy=policy.default)
            forattachmentinattachFile.iter_attachments():
                    attName = attachment.get_filename()
                    print(Fore.GREEN + "\n[+] �����������������������������: " + Fore.RESET + attName)
                    withopen(os.path.join(exportedPath, attName), "wb") asfileWrite:
                            fileWrite.write(attachment.get_payload(decode=True))

    except:
        print("���-�� ����� �� ��� �� ���������� ���������")

defbanner():

    banner = """
ANTI PHISHINGGGGGGG 
    """

    print(Fore.GREEN + banner + "\n")

defmain():

    banner()

    iflen(sys.argv) <2orlen(sys.argv) >2:
        print(Fore.YELLOW + "������� �������� ���������� ����������!")
    else:
        fileChecker()

if__name__ == "__main__":
    main()
