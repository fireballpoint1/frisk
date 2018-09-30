import ftplib

server = ftplib.FTP()
server.connect('10.2.6.49', 8080)
server.login('user', 'user')

