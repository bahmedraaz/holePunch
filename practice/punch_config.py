import os
import hashlib
from stat import *


#tcheck uniqueness of the username and return true if the username is unique, otherwise return false
def isUsernameUnique(userCredential):
	count = 0
	userCredentialList = userCredential.split()
#	print("username: ", userCredentialList[0])
#	print("Port: ", userCredentialList[2])
	#check whether the file you want to store the username is empty
	if os.stat(home+"/.hole_punch/users").st_size == 0:
		return True

	# read the every lines of the file, if a match is found return false otherwise return true
	fileObj = open(home+"/.hole_punch/users", "r")
	for line in fileObj:
		if userCredentialList[0] in line.split():
			count+=1
	if count > 0:
		return False
	else:
		return True

#check uniqueness of the port number, return true if it is unique, otherwise return false
def isPortUnique(userCredential):
	count = 0
	userCredentialList = userCredential.split()
#	print("username: ", userCredentialList[0])
#	print("Port: ", userCredentialList[2])
	#check whether the file you want to store the username is empty
	if os.stat(home+"/.hole_punch/users").st_size == 0:
		return True

	# read the every lines of the file, if a match is found return false otherwise return true
	fileObj = open(home+"/.hole_punch/users", "r")
	for line in fileObj:
		if userCredentialList[2] in line.split():
			count+=1
	if count > 0:
		return False
	else:
		return True

def checkPermission(fileName):
	if oct(os.stat(fileName)[ST_MODE])[-3:] == "700":
		return True
	else:
		return False


while True:
		userCredential = input("Please Enter <username> <password> <port>\n")
		userCredentialList = userCredential.split()

		home = os.environ["HOME"]

		dirPermission = checkPermission(home+"/.hole_punch")
		filePermission = checkPermission(home+"/.hole_punch/users")

		if not dirPermission or not filePermission:
			print("\nProblem with permission")
			print(home+"/.hole_punch"+" and "+home+"/.home_punch/users "+"both should have permission 700")
			break

		#check if the user enters exactly three parameters
		if len(userCredentialList) != 3: #restric user from entering more than three parameters (username, password and port)
			print("Please enter exactly three parameters: <username> <password> <port>")
			continue
		try: #check if the user enters integer number for port
			port = int(userCredentialList[2])
			pass
		except Exception as valueError:
			print("Port number must be integer")
			continue

		#if the program counter comes to this point, that means user enters an integer for port number
		if len(str(userCredentialList[2])) > 4: #check if the number of digit in port number is more than 4
			print("Port number cannot hold more than 4 digit")
			continue
		if int(userCredentialList[2]) < 0: #check if the port number is negative
			print("Port number cannot be negative")
			continue

		#check the uniqueness of the username and port
		if not isUsernameUnique(userCredential) and not isPortUnique(userCredential):
			print("Try different username and port number")
			continue
		elif not isUsernameUnique(userCredential) and isPortUnique(userCredential):
			print("Try different username")
			continue
		elif isUsernameUnique(userCredential) and not isPortUnique(userCredential):
			print("Try different port number")
			continue

		#hash the password using md5 hash function
		hashObj = hashlib.md5(userCredentialList[1].encode())
		#get the hashed password
		hashedPawword = hashObj.hexdigest()

		#prepare the usercredentials with unique username and port, and hashed password
		updatedUserCredentials = userCredentialList[0]+" "+hashedPawword+" "+userCredentialList[2]

		#if program counter comes to this point, that means we passed all the checking of corner cases. Now its time to store in the file
		with open(home+"/.hole_punch/users", "a") as writeCredential:
			writeCredential.write(updatedUserCredentials+"\n")
			print("Congratulations !!!! You are registered")
			break
