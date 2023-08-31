import sys
import socket
import time 
from datetime import datetime

def check_port(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Timeout for the connection attempt
    
    try:
        result = sock.connect_ex((hostname, port))
        if result == 0:
            print(f"{datetime.now()} - Port is open")
        else:
            print(f"{datetime.now()} - Port isn't open")
            
        sock.close()
        
    except Exception as e: 
         print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Invalid number of arguments')
        sys.exit()

    hostname = sys.argv[1]
    port     = int(sys.argv[2])
   
    while True:  
        check_port(hostname,port)
        time.sleep(1) # wait for a second before checking again.
