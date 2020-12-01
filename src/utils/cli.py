from src.sock import Sock
from src.utils.parser import Parser
from src.sender import Sender


class Cli:

    def __init__(self, sockint: Sock, parser: Parser, sender: Sender):
        self.sockint = sockint
        self.socket = sockint.get_socket()
        self.parser = parser
        self.sender = sender

    def welcome(self):
        print(
            f'\t\tWelcome!\n'
            f'":c" to establish connection\n'
            f'":m" to send message\n'
            f'":f" to send file\n'
            f'":s" to change settings\n'
            f'":q" to exit program\n'
            f'Your address is set to: {self.socket.getsockname()[0]}:{self.socket.getsockname()[1]}\n'
        )

    def stdin(self):
        self.welcome()

        while True:
            action = input('')

            if action == ':c':  # establish connection
                self.sender.send_syn()

            elif action == ':m':  # send message
                self.sender.input_data()

            elif action == ':f':  # send file
                self.sender.input_data(file=True)

            elif action == ':d':  # drop connection [do not send keep-alive]
                pass

            elif action == ':s':  # settings for changing dgram size
                self.parser.set_dgram_size()

            elif action == ':q':  # quit program
                self.sockint.close_socket_stop()
            else:
                print('$ Unknown action, please try again')
