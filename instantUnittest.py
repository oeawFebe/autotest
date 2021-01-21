# This script will detect any change in scripts in the same directory or sub-directories and run unittest automatically.
# Using python3.9.0
import time
from fabric.api import local
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler
  
def on_created_or_modified(event):
    """run unittest by using fabric3"""
    try:
        # There is a unittest script named 'test.py' in the same directory.
        local('python test.py')
    except:
        # Let the user know that unittest failed or encountered an error but keep running this script.
        print("Detected failure or an error.")

if __name__ == "__main__":
    my_event_handler = FileSystemEventHandler()
    my_event_handler.on_created  = on_created_or_modified
    my_event_handler.on_modified = on_created_or_modified

    my_observer = Observer()
    my_observer.schedule(my_event_handler, path='.', recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(5)
    except Exception:
        my_observer.stop()
    my_observer.join()

