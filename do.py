import time

def hello():
    d = 0
    while True:
          if d > 10:
             break
          yield d
          d+=1


for x in hello():
    print(x)
    time.sleep(1)
