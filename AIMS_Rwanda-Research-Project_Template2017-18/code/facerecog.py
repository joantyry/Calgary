#This code is written in python3

import dlib
import face_recognition
from Crypto.PublicKey import RSA
from Crypto import Random
#This is a face recognition model.

#Key generation.
rand = Random.new().read 
private_key = RSA.generate(1280, rand)
public_key = private_key.publickey()

def face():
	
	#The inputFace is compared with the target face to see whether 
	#they images represent same or different persons.
	
	targetFace = face_recognition.load_image_file
			('/home/joan/joan/pythoncode/jj.jpg')

	encodedFace = face_recognition.face_encodings(targetFace)[0]

	inputFace = face_recognition.load_image_file
			("/home/joan/joan/pythoncode/DigitalPhoto.jpg")

	encodedInputFace = face_recognition.face_encodings(inputFace)[0]

	outPut = face_recognition.compare_faces([encodedFace ], encodedInputFace)
	
	u = "The face matches!"
	l = "No match!"

	if outPut [0] == True:
		a = u
	else:
		a = l
	return a

def encrypt():
	
	#Here the message encryption is performed based on the results of face()
	
	a = face()
	k = public_key.encrypt('Intruder detected'.encode('utf-8'),10)
	p = public_key.encrypt('Correct authentication'.encode('utf-8'),10)
	
	if a == "The face matches":
		
		enc_data = k
		
	else:
		enc_data = p	

	return enc_data	
		
		
def decrypt():
	
	#Decryption of the results from encrypt() are done.
	
	b = encrypt()
	privateKey = int(input('Please enter your password and press enter'))
	attempts = 1
	chances = 3

	if privateKey == 3045:

		raw_text = private_key.decrypt(b)
		print (raw_text)
	else:

		print('Wrong password')
			
		while attempts < 3 :
			chances -=1
			attempts +=1
			att = int(input('Attempt %d, you have %d chances left : ' 
							%(attempts, chances)))
			if att == 3045:

				raw_text = private_key.decrypt(b)
				print (raw_text)
			else :
				print ('Wrong password')
			
		print ('You have been blocked from the system!')
		
if __name__ == '__main__':

	print('Recognizing face .......')
	print (face())
	
	print('Encrypting ..........')
	print(encrypt())

	print('Decrypting ..........')
	print(decrypt())
