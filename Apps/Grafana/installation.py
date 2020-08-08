#from pexpect import pxssh

from Fuego.Installer.servers_login import Connection
import Fuego.fuego as main

connector = Connection(main.hostname, main.username, main.password)

def install_grafana():
    connector.connect_to_target()
    print("bla")