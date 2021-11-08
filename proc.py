import psutil
import datetime

def on_test_start(process):
    for proc in psutil.process_iter():
        if(proc.name() == process):
            # print(proc)
            time = proc.create_time()
            formated = datetime.datetime.fromtimestamp(
                time).strftime("%H:%M:%S")
            # print(formated)
            return (formated, proc.pid, proc.name)


def info():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)


def on_terminate(proc):
    #print("Process {} terminated".format(proc))
    ()
    


def get_pid(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            return proc.pid
    return -1
