import socket
import random
import time


HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando por conexões...')
conn, addr = s.accept()

print('Conexão estabelecida por', addr)


while True:
    # Dados de simulação, esses dados serão recebidos por meio dos sensores
    heading = random.randint(0, 360)
    speed = random.randint(0, 10)
    depth = random.uniform(0, 50)
    temperature = random.uniform(-10, 30)
    #####################################
    
    if heading < 180:
        conn.send('direita'.encode())
    else:
        conn.send('esquerda'.encode())
        
    if speed < 5:
        conn.send('frente'.encode())
    else:
        conn.send('costa'.encode())
        
    if depth < 10:
        conn.send('subir'.encode())
    else:
        conn.send('descer'.encode())
        
    if temperature < 0:
        conn.send('aumentar'.encode())
    elif temperature > 20:
        conn.send('diminuir'.encode())   
    
    time.sleep(5)