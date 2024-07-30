import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:\\Users\\T-GAMER\\Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path}  foi criado!")

    def on_deleted(self,event):
        print(f"Opa! Alguem excluiu {event.src_path} !")

    def on_modified(self,event):
        print(f"Olá!, {event.src_path} foi modificado !")

    def on_moved(self,event):
        print(f"Alguem moveu {event.src_path} para{event.dest_path} !")

        


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt
try:
    while True:
      time.sleep(2)
      print("executando...")
except KeyboardInterrupt:
    print("interrompido! ")
    observer.stop()






