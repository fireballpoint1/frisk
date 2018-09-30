from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json

from vt_api import VtAPI

vt = VtAPI('5e4647cbad54f75398c8904e409de95fba7bda5e30a8938051ff07ad3cf6429f')

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        msg = json.loads(post_data.decode('utf-8'))
        file_name = msg['fname']
        file_address = 'test_user/' + msg['fname']
        us_response = vt.uploadScan(file_name, file_address)
        # print(type(response), response)

        gsr_response = vt.getScanReport(us_response['resource'])
        self._set_response()
        self.wfile.write(json.dumps(gsr_response).encode('utf-8'))

        # gbr_response = vt.getBehaviourReport(us_response['sha256'])
        # self._set_response()
        # self.wfile.write(str([json.dumps(gsr_response), json.dumps(gbr_reponse)]).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8081):
    logging.basicConfig(level=logging.INFO)
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()