import base64

def encrypt(string):
	return str(base64.b64encode(bytes(string.encode('utf-8'))))

def decrypt(string):
	return str(base64.b64decode((string.lstrip('b')).encode('utf-8'))).lstrip('b').strip("\'")
	