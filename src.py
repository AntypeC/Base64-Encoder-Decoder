import base64
import argparse

ap = argparse.ArgumentParser()

input_msg = input("Enter encoded or decoded message: ")

def isBase64(msg):
    try:
        if base64.b64encode(base64.b64decode(msg)) == msg:
            return False
        else:
            return True
    except Exception:
        return False

if isBase64(input_msg) == False:
    msg_bytes = input_msg.encode('ascii')
    base64_bytes = base64.b64encode(msg_bytes)
    base64_msg = base64_bytes.decode('ascii')
    print(base64_msg)
else:
    base64_bytes = input_msg.encode('ascii')
    msg_bytes = base64.b64decode(base64_bytes)
    msg = msg_bytes.decode('ascii')
    print(msg)