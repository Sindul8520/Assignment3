from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"


    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM:<s@s.com>\r\n'
    clientSocket.send(mailfromCommand.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)


    rcpttoCommand = 'RCPT TO:<s@s.com>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    # print(dataCommand)
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)

    mailMessageEnd = '\r\n.\r\n'
    message = msg + mailMessageEnd
    clientSocket.send(message.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)

    quitCommand = 'QUIT\r\n'
    # print(quitCommand)
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024)
    clientSocket.close()
    # print(recv1)

if __name__ == '__main__':

