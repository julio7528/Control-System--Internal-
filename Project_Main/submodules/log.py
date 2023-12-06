# Importing the libraries
from datetime import datetime
import psutil, os, traceback
from tkinter import messagebox

# Creating the class logFile
class logFile:

    """
    This class is used to log messages in a file.
    Attributes:
        now (datetime): The current date and time.
        message (str): The message to be logged.
        logfile (str): The path of the file where the logs will be stored.
    Methods:
        _log(): Records the log in the file using a message.
        _logStructure(): Log struct is only used in the beginning and the ending of the file.
        pubLog(): Calls _log() method to record the log in the file using a message.
        pubLogStructure(): Calls _logStructure() method to log struct in the beginning and the ending of the file.
    """

    def __init__(self, message):
        self.now = datetime.now()
        self.message = message
        self.logfile = './Logs/logStructure.txt'

    def _log(self): #Record the log in the file using a message
        now = self.now
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S:%f")
        with open(self.logfile,'a+') as f:
            f.write(f'Log:{dt_string} - {self.message}\n')
            f.write(f'{" " * 90}CPU%:{float(psutil.cpu_percent())}%-CPUGHZ:{str(psutil.cpu_freq().current)}-MEM:{float(psutil.virtual_memory().percent)}%\n')
        f.close()

    def _logStructure(self): #Log struct is only used in the beginning and the ending of the file
        with open(self.logfile,'a+') as f:
            f.write(f'{"-" * 90}\n')
        f.close()

    def pubLog(self):
        self._log()

    def pubLogStructure(self):
        self._logStructure()

def logmessage(message): #Public Function to Call in another Python File
    logFile(message).pubLog()
    
def logStruct(): #Public Function to Call in another Python file
    logFile('').pubLogStructure()

try:
    e = 0
except Exception as e:
    logmessage(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")
