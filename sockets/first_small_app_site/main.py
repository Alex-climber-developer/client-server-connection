import socket
from views import *


URLS = {
  '/': index,
  '/first': blog
}


def parse_reqest(reqest):
  parsed= reqest.split(' ')
  method=parsed[0]
  url=parsed[1]
  return (method, url)


def generate_headers(method, url):
  if not method == "GET":
    return ('HTTP/1.1 405 Method not allowed\n\n', 405)

  if not url in URLS:
    return ('HTTP/1.1 404 Not found\n\n', 404)

  return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(code, url):
  if code== 404:
    return '<h1> ERROR 404\n URL Not found </h1> '
  if code== 405:
    return '<h1> ERROR 405\nMethod didnt allowed </h1> '
  if code== 200:
    return URLS[url]()


def generate_responce(reqest):
  method, url = parse_reqest(reqest)
  headers, code = generate_headers(method, url)
  body = generate_content(code, url)
  
  return (headers+body).encode()


x = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
x.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
x.bind(('localhost', 5000 ))
x.listen()


while True:
  y, adress = x.accept()#блокирующая операция ,тк пока не полуит подключение к сервер. сокету(от браузера или метод "nc адрес порт" в терминале)
  reqest = y.recv(1024)
  print(reqest)
  


  responce =  generate_responce(reqest.decode('utf-8'))
  y.sendall(responce)#блокирующая операция
  y.close()
