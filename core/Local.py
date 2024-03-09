'''
Name : Local.py
Description : Local functions to checks and initiate application files
'''
import csv
from datetime import datetime
from pathlib import Path
import os

def WriteAppLog(action, result = "success"):
    log_file = "./local/App_Log.csv"
    f = open(log_file,"a")

    fields = ["date_time", "action","result"]
    log_input = {"date_time": str(datetime.today()), "action":action, "result":result}

    write_log = csv.DictWriter(f, fieldnames= fields)
    write_log.writerow(log_input)

    return True
    
def ReadAppLogger():
    log_file = "./local/App_Log.csv"
    f = open(log_file,"r")
    return csv.DictReader(f)

def ReadTraceLog():
    log_file = "./Trace_Log.csv"
    f = open(log_file,"r")
    return csv.DictReader(f)

def InitializationCheck():
    # Check for local folder
    if Path("./local").exists():
        pass
    else:
        os.makedirs("./local")

    # Check for application log file
    if Path("./local/App_Log.csv").exists():
        pass
    else:
        log_file = "./local/App_Log.csv"
        f = open(log_file,"a")

        fields = ["date_time", "action","result"]
        log_input = {"date_time": "date_time", "action":"action", "result":"result"}

        write_log = csv.DictWriter(f, fieldnames= fields)
        write_log.writerow(log_input)
        print("Application log file created")

    # Check for trace log file
    if Path("./local/Trace_Log.csv").exists():
        pass
    else:
        log_file = "./local/Trace_Log.csv"
        f = open(log_file,"a")

        fields = ["date_time", "technique", "tactic","attack_surface","result"]
        log_input = {"date_time":"date_time", "technique":"technique", "tactic":"tactic","attack_surface":"attack_surface", "result":"result"}

        write_log = csv.DictWriter(f, fieldnames= fields)
        write_log.writerow(log_input)
        print("Trace log file created")