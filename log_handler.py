import sys


def open_log_file(logname):
    old_stdout = sys.stdout
    log_file = open(f"{logname}.log","a")
    sys.stdout = log_file
    return old_stdout, log_file


def close_log_file(old_stdout, log_file):
    sys.stdout = old_stdout
    log_file.close()
    return
