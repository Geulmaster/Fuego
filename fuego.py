import questionary
import cmd
import Fuego.Infrastructure.methods as methods
from Fuego.Installer.servers_login import Connect
import re

hostname = "default"
username = "default"
password = "default"

def input_formatter(source, seperators):
    return re.split('[{0}]'.format(re.escape(seperators)), source)

class General(cmd.Cmd):

    def do_install(self):
        methods.install()

    def do_config(self, *args):
        inpt = args[0].replace(" ", ",")
        credentials = input_formatter(inpt, ',')
        hostname, username, password = credentials
        validate = input("The credentials are: hostname: {}, username: {}, password: {}. Please confirm y/n ".format(hostname, username, password))
        if validate == 'y' or validate == 'yes':
            connection = Connect(str(hostname), str(username), str(password))
            connection.connect_to_target()
        else:
            print("Operation aborted, please try again.")

    def do_exit(self):
        print("Bye!")
        exit()

run = General()

if __name__ == '__main__':
    General().cmdloop()