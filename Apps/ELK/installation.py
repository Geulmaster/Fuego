#from pexpect import pxssh

from Fuego.Installer.servers_login import Connect
import Fuego.fuego as main

connector = Connect(main.hostname, main.username, main.password)

def install_elk():
    connector.connect_to_target()
    print("bla")