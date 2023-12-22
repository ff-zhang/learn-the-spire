import sys

from comms import communicator

if __name__ == '__main__':
    com = communicator.Communicator()

    print("Hello World!", file=sys.stderr)
