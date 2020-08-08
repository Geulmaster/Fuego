import questionary
import cmd
import Fuego.Infrastructure.methods as methods
from Fuego.Installer.servers_login import Connection
from Kingfish.Core import logger
import re

hostname = "default"
username = "default"
password = "default"

def input_formatter(source, seperators):
    return re.split('[{0}]'.format(re.escape(seperators)), source)

class General(cmd.Cmd):

    def do_install(self, arg):
        methods.install()

    def do_config(self, *args):
        try:
            inpt = args[0].replace(" ", ",")
            credentials = input_formatter(inpt, ',')
            hostname, username, password = credentials
            validate = input("The credentials are: hostname: {}, username: {}, password: {}. Please confirm y/n ".format(hostname, username, password))
            if validate == 'y' or validate == 'yes':
                connection = Connection(str(hostname), str(username), str(password))
                connection.connect_to_target()
            else:
                logger.fatal("Operation aborted, please try again.")
        except ValueError:
            logger.fatal("You should insert credentials after the 'config' command")

    def do_exit(self, arg):
        logger.info("Bye!")
        exit()

run = General()

if __name__ == '__main__':
    General().cmdloop()