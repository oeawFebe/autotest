import time,os
import time
from fabric.api import local
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import PatternMatchingEventHandler
  
def on_created(event): 
    runTest()
def on_modified(event):
    runTest()

def runTest():
    print('\n\n')
    try:
        local('py test.py')
    except:
        print("Detected Error. Continuing Monitoring.\n\n\n")
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_modified = on_modified

    path_ = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path_, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(5)
    except (Exception):
        my_observer.stop()
    my_observer.join()

