import sys
import queue
import threading


def read_stdin(q: queue.Queue):
    while True:
        in_str = ''
        while True:
            in_str += sys.stdin.read(1)

            if in_str[-1] == '\n':
                break

        q.put(in_str)


def write_stdout(q: queue.Queue):
    while True:
        out_str = q.get()
        print(out_str, end='\n', flush=True)


class Communicator:
    """
    Object which for communicates with Slay the Spire (using the CommunicationMod).
    """

    def __init__(self):
        self.in_queue = queue.Queue()
        self.input_thread = threading.Thread(target=read_stdin, args=[self.in_queue])
        self.input_thread.daemon = True
        self.input_thread.start()

        self.out_queue = queue.Queue()
        self.output_thread = threading.Thread(target=write_stdout, args=[self.out_queue])
        self.output_thread.daemon = True
        self.output_thread.start()
