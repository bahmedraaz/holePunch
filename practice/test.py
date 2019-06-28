while True:

    userCredential = input("Enter <username> <password> <port>\n")
    userCredentialList = userCredential.split()

    print("You entered: ", userCredential)
    print("Splited input: ", userCredentialList)
    print("\n")

    fileObj = open("test.txt", "r")


    try:
        port = float(userCredentialList[2])
        print("Port cannot be float")
        continue

    except Exception as e:
        pass

    try:
        port = int(userCredentialList[2])
    except Exception as e:
        print("Port should be integer")
        continue




# for line in fileObj:
#     print("username: ", userInputList[0])
#     print("port: ", userInputList[2])
#     print("splitted Line: ",line.split())

    # if userInputList[0] in line.split():
    #     print("username in use")
