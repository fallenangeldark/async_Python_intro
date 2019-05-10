"""Событийный цикл"""
import socket
from select import select # нужна для мониторинга состояния файловых объектов и сокетов работает с любым объектом у которого есть метод .fileno() (возвращает файловый дескриптор - номер файла ассоциированный с файлом в системе)


to_monitor = []

# domain:5001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (IPV4, STREAM-TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 0 - socket level, so_reuse - переиспользование адреса в true ,1
server_socket.bind(('localhost', 5001)) # привязка к домену и порту, пишем в кортеже
server_socket.listen() # слушаем буфер для входящих подключений


def accept_connection(server_socket):
    print('Before .accept()')
    client_socket, addr = server_socket.accept() # принимаем подключение кортеж с сокетом и адресом
    # print('Connection from', addr, 'cl_socket: ', client_socket)
    #было send_message(client_socket)

    to_monitor.append(client_socket)

def send_message(client_socket):
    # print('Before .recv()')
    request = client_socket.recv(4096) # получение сообщения на сервер от клиента размером буфера 4096 байт

    if request:
        response = 'Hello dumn\n'.encode() # default encode to bytes
        client_socket.send(response)
    else:
        client_socket.close()




def event_loop():
    while True:
        print('THIS IS AAAAAAAAAA: ',to_monitor)
        ready_to_read, wlist, xlist = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    # accept_connection(server_socket) #было
    event_loop()
