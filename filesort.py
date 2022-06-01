
# Scrip used to sort downloads folder into sub-fodlers by namefile extension

import shutil
import os
from sys import platform
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

if platform == "linux" or platform == "linux2":
    slash = "/"
    downloadsdir = "/mnt/d/DESCARGAS"
    imgdir = "/mnt/d/DESCARGAS/images"
    viddir = "/mnt/d/DESCARGAS/videos"
    audiodir = "/mnt/d/DESCARGAS/audios"
    zipdir = "/mnt/d/DESCARGAS/zip"
    installdir = "/mnt/d/DESCARGAS/installers"
    pdfdir = "/mnt/d/DESCARGAS/pdf"
    restdir = "/mnt/d/DESCARGAS/rest"
    samplesdir = "/mnt/e/otros/PROYECTOS/Musica/ALL MY SOUNDS/DRUM KITS/SAMPLES"
elif platform == "win32":
    slash = "\\"
    downloadsdir = r"D:\DESCARGAS"
    imgdir = r"D:\DESCARGAS\images"
    viddir = r"D:\DESCARGAS\videos"
    audiodir = r"D:\DESCARGAS\audios"
    zipdir = r"D:\DESCARGAS\zip"
    installdir = r"D:\DESCARGAS\installers"
    pdfdir = r"D:\DESCARGAS\pdf"
    restdir = r"D:\DESCARGAS\rest"
    samplesdir = r"E:\otros\PROYECTOS\Musica\ALL MY SOUNDS\DRUM KITS\SAMPLES"
def move(file,dest,name):
    if os.path.exists(dest + slash + name):
        os.remove(dest + slash + name)
    shutil.move(file, dest)

class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(downloadsdir) as downloads:
            for file in downloads:
                if os.path.isfile(downloadsdir + slash + file.name):
                    name = file.name
                    destination = downloadsdir
                    if name.endswith(("crdownload", "part","tmp")):
                        pass
                    if name.endswith((".mp3",".wav",".mpeg")):
                        if name.startswith("looperman"):
                            destination = samplesdir
                            move(file,destination,name)
                        else:
                            destination = audiodir
                            move(file,destination,name)
                    elif name.endswith(".pdf"):
                        destination = pdfdir
                        move(file,destination,name)
                    elif name.endswith((".zip",".rar")):
                        destination = zipdir
                        move(file,destination,name)
                    elif name.endswith((".mp4",".mov")):
                        destination = viddir
                        move(file,destination,name)
                    elif name.endswith((".exe",".msi")):
                        destination = installdir
                        move(file,destination,name)
                    elif name.endswith(("png","jpg","jpeg","webp")):
                        destination = imgdir
                        move(file,destination,name)
    
if __name__ == "__main__":
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path=downloadsdir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
