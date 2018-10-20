import sys
import argparse
from .classes import Parser, Copypaste, Server

def main():
    #args = sys.argv[1:]

    if len(sys.argv) == 1:
        print('Error: Please supply arguments.', file=sys.stderr)
        return

    parser = Parser()
    args = parser.run()

    if args.func == 'set':
        cpypst = Copypaste()
        cpypst.set(args.server_ip[0])
    elif args.func == 'copy':
        cpypst = Copypaste()
        cpypst.copy(args.string[0])
    elif args.func == 'paste':
        cpypst = Copypaste()
        cpypst.paste()
    elif args.func == 'run':
        server = Server()
        server.run()

    #print('Invalid', file=sys.stderr)
        

if __name__ ==  '__main__':
    main()