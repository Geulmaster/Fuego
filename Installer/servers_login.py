from pexpect import pxssh

class Connect():
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

connection = Connect('host', 'user', 'passwd')
connection.connect_to_target()