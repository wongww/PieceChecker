import hashlib
#How to Use
#Tecnicalities of this program anf specifics 
# Get the file and a return a list of strings
def getFile():
	# Get the name of the torrent file and return a list of hex values e.g['32','FF','A4']
	try:
		with open(input("What is the .torrent file called?: "), 'rb') as f:
   			hexdata = f.read().hex()
   			return [hexdata[i:i+2] for i in range(0, len(hexdata), 2)]
	except FileNotFoundError:
		print("The program could not find the file. The program will now terminate.")
# Take a hex string and convert to ascii
def convertToASCII(hexChar):
	bytes_object = bytes.fromhex(hexChar) 
	return bytes_object.decode("ASCII")
#Check file signature of .torrent file
def signatureCheck():
	sig = ''
	for x in range(11):
		sig+=convertToASCII(hexList[x])
	if(sig == 'd8:announce'):
		print('The hex signautre matches that of a .torrent file')
	else:
		print('There is a signature mismatch')
# Returns the length of each piece is
def getPieceLength():
	if hexConcatenated.find('7069656365206c656e677468')==-1:
		print("Piece Length not found in torrent file")
		return
	else:
		parse(int(hexConcatenated.find('7069656365206c656e677468')/2)+13,'65')
# Returns all the pieces concatenated as a string
def getPiece():
	start = int(hexConcatenated.find('706965636573')/2)+6
	# How long the string of concatenated SHA1 hashes will be
	# Has to be a multiple of 20
	lengthOfHashses = parse(start, '3a')
	if lengthOfHashses%20!=0:
		print('This torrent file is not valid. The length of the concatenated hashes is not a multiple of 20')
		return 
	start = start + len(decimal_value) + 1
	end = start + int(decimal_value)
	hashes = ''
	for x in range(start, end):
		hashes+=hexList[x]
	return hashes
# Parse BEncode for certain numbers
def parse(index, delimeter):
	hex_value=''
	dec_value=''
	while hexList[index]!=delimeter:
		hex_value+=hexList[index]
		index = index+1
	for x in range(0,len(hex_value),2):
		dec_value+=convertToASCII(hex_value[x:x+2])
	return dec_value
def singleFileCheck():
	with open(input("What is the content filename?: "), 'rb') as file:
		buf = file.read(int(getPieceLength))
		hasher = hashlib.sha1()
		hasher.update(buf)
		hash_value =hasher.hexdigest()
		hashes = getPiece()
		if hashes.find(hash_value) != -1:
			print('This file is torrented using this torrent')
		else:
			print('This file is not associate with this torrent')
def fileMode():
	if hexList.concatenated.find('66696c6573') != -1:
		return 1
	else:
		return 0
def getFiles():
	indexesOfLengths = [i for i in range(len(hexConcatenated)) if hexConcatenated.startswith('64363a6c656e67746869', i)]
	indexesOfPaths = [i for i in range(len(hexConcatenated)) if hexConcatenated.startswith('343a706174686c', i)]
	listOfFiles = []
	for x in range(0,len(indexesOfPaths)):
		filepath = ''
		index_start = int(indexesOfPaths[x]/2)+7
		decimal_start = parse(index_start, '3a')
		while hexList[index_start:index_start+2] != ['65','65']:
			for y in range (index_start+1+len(str(decimal_start)), index_start+1+int(decimal_start)+len(str(decimal_start))):
				hex_value = hexList[y]
				filepath+=convertToASCII(hex_value[0:2])
			index_start = index_start + int(decimal_start) + 1 + len(str(decimal_start))
			decimal_start = parse(index_start, '3a')
			if hexList[index_start:index_start+2] != ['65','65']:
				filepath+='/'
		listOfFiles.append(filepath)
	return listOfFiles

		
def pieceVerify():
	filename = input("What is the file of the name you are trying to verify?: ")
	if fileMode():
		startingByte = 0
		indexOfFile = 0
		for i in range(0,len(listOfFiles)):
			if listOfFiles[i].find(filename) !=-1:
				indexOfFile = i

print("""
Welcome to BitTorrent Piece Analyzer!

To conitnue please enter the .torrent you wish to analyze to continue.
""")
hexList = getFile()
if !fileMode():
	print("The torrent file specified is a single file torrent.")
	singleFileCheck()
else:
	print("The torrent file specified is a multi file torrent")
# hexConcatenated = ''.join(hexList)
# listOfFiles = getFiles()




