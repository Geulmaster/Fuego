import configparser
#from pexpect import pxssh
from Overlord import ssh

class Connect():
    """
    Legacy
    """
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        print("Trying to login to {}, with the user {}".format(hostname, username))

    def connect_to_target(self):
        print("Credentials: hostname: {}, username: {}, password: {}".format(self.hostname, self.username, self.password))
        try:
            agent = pxssh.pxssh()
            agent.login(self.hostname, self.username, str(self.password))
        except:
            print("Failed to login to server, please check the inserted credentials of {}".format(self.hostname))

#connection = Connect('host', 'user', 'passwd')
#connection.connect_to_target()
def config_reader():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

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