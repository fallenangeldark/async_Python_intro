import socket

# domain:5001


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (IPV4, STREAM-TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 0 - socket level, so_reuse - переиспользование адреса в true ,1
server_socket.bind(('localhost', 5001)) # привязка к домену и порту, пишем в кортеже
server_socket.listen() # слушаем буфер для входящих подключений

while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept() # принимаем подключение кортеж с сокетом и адресом
    print('Connection from', addr, 'cl_socket: ', client_socket)

    while True:
        print('Before .recv()')
        request = client_socket.recv(4096) # получение сообщения на сервер от клиента размером буфера 4096 байт

        if not request:
            break
        else:
            response = 'Hello dumn\n'.encode() # default encode to bytes
            client_socket.send(response)
