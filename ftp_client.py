import ftplib

server = ftplib.FTP()
server.connect('127.0.0.1', 44333)
server.login('user', 'user')

