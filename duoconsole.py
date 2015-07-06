"""
RamondettiDavide Spa
====================
DuoConsole Python 20

DuoConsole is a free open source console in python and it execute some commands
"""
import sys

print("************************");
print("* RamondettiDavide Spa *");
print("* DuoConsole Python 20 *");
print("************************");
def CommandLine() :
  command = input("DuoConsole:~ root$ ");
  if (command == null) :
    print("DuoConsole Cannot Execute This Code");
  else :
    if (command == "print") :
      wr = input("DuoConsole:~ root$ print ");
      print(wr);
    if (command == "echo") :
      print("To execute the command ECHO you must buy DuoConsole Platinum!");
    if (command == "whois") :
      whois = input("DuoConsole:~ root$ whois ");
      open("http://who.is/whois/",whois);
    else :
      print("Buy the PRO to Use Some Codes.");
CommandLine();
