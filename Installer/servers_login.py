from configparser import ConfigParser
from pathlib import Path
from Overlord import ssh

def config_reader():
    config_file = Path(__file__).parent / 'config.ini'
    parser = ConfigParser()
    parser.read(config_file)
    return parser

configuration = config_reader()
server = configuration['CREDENTIALS']

class Connection():
    def __init__(self):
        self.hostname = server['Hostname']
        self.username = server['Username']
        self.password = server['Password']
        print("Trying to login to {}, with the user {}".format(hostname, username))

    def connect(self):
        connection = ssh.Host(self.hostname, self.username, self.password)
        connection.connect()