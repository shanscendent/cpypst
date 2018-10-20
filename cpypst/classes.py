import argparse
import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client, urllib.parse
import http

string = 'placeholder'

class Parser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Copy paste between machines')
        #self.parser.add_argument('copy', type=str, help='String to copy')
        subparsers = self.parser.add_subparsers()

        # 'copy' command parser
        self.parser_copy = subparsers.add_parser('copy', help='Copy string to server')
        self.parser_copy.set_defaults(func='copy')
        self.parser_copy.add_argument('string', type=str, nargs=1, help='String to be copied')

        # 'paste' command parser
        self.parser_paste = subparsers.add_parser('paste', help='Paste string to stdout')
        self.parser_paste.set_defaults(func='paste')
        
        # 'set' command parser
        self.parser_set = subparsers.add_parser('set', help='Set cpypst server IP address')
        self.parser_set.set_defaults(func='set')
        self.parser_set.add_argument('server_ip', type=str, nargs=1, help='Server IP address')

        # 'run' command parser
        self.parser_run = subparsers.add_parser('run', help='Spawn cpypst server')
        self.parser_run.set_defaults(func='run')

    def run(self):
        self.args = self.parser.parse_args()
        return self.args
    

class Copypaste():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('cpypst.conf')
        self.server_ip = self.config['cpypst']['server_ip']

    def set(self, server_ip):
        self.config['cpypst'] = {'server_ip': server_ip}
        with open('cpypst.conf', 'w') as configfile:
            self.config.write(configfile)
        pass
    
    def copy(self, string):
        conn = http.client.HTTPConnection(self.server_ip+':8080')
        bytestring = string.encode()
        #print(bytestring)
        params = bytestring
        conn.request('POST', '', params)
        # PROBLEM - does not check for response
        #response = conn.getresponse()
        #print(response.status, response.reason)
        conn.close()
        print(f'Copied {string} to: ')
        print(self.config['cpypst']['server_ip'])

    def paste(self):
        conn = http.client.HTTPConnection(self.server_ip+':8080')
        conn.request('GET', '/')
        r1 = conn.getresponse()
        #print(r1.status, r1.reason)
        data = r1.read().decode('utf-8')
        print(data)

class ServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global string
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        #string = 'Hello World!'
        print(f'User requests \'{string}\' to paste')
        # Write content as UTF-8
        self.wfile.write(bytes(string, 'utf-8'))
        return
    
    def do_POST(self):
        global string
        self.message = self.rfile.read()
        string = self.message.decode('utf-8')
        print(f'User updates string with \'{string}\'')
        self.send_response(201)
        #self.wfile.write(bytes(string, 'utf-8'))
        
        
        

class Server():
    def __init__(self):
        # read from server section in config file. Example: ports

        server_address = ('0.0.0.0', 8080)
        self.httpd = HTTPServer(server_address, ServerRequestHandler)

        pass

    def run(self):
        print('Server started.')
        self.httpd.serve_forever()
        pass