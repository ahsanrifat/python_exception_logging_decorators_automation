import os
import logging
from datetime import datetime

class CustomLogger:
    
    def __init__(self,log_file_name=datetime.now().strftime(f"%d-%m-%Y.log"),log_path="logs"):
        print("Init Log")
        self.logger = None
        self.log_file_name=log_file_name
        self.log_path=log_path
         
    def get_log_file_full_path(self):
        # if log folder is not there then create one
        if os.path.isdir(self.log_path) == False:
            os.makedirs(self.log_path)
        return rf"{self.log_path}/{self.log_file_name}"

    def initiate_log(self):
        try:
            # initiate logger if self.logger in nones
            if not self.logger:
                
                LOG_FILENAME = self.get_log_file_full_path()
                logging.basicConfig(
                    level=logging.ERROR,
                    filename=LOG_FILENAME,
                    format="========(START)--Date: %(asctime)s Level: %(levelname)s==========>\n%(message)s<===========(END)==========>\n",
                )
                if os.path.isfile(LOG_FILENAME) != True:
                    logging.FileHandler(LOG_FILENAME, encoding=None, delay=False)
                self.logger = logging.getLogger()
        except Exception as e:
            print(f"Exception-(initiate_log)->{e}")

    def handle_exception_log(self, exception_str: str, method_name: str, *args,**kwargs):
        try:
            if not self.logger:
                self.initiate_log()
            
            message = (
                f"Method Name: {method_name}\nException Message: {exception_str}\n"
            )
            if kwargs:
                message = message+"parameters=\n"
                for key in kwargs:
                    message = message + f"{key}: {kwargs[key]}\n"
            if args:
                message = message+"args=\n"
                for key in args:
                    message = message + f"{key}\n"
            self.logger.error(message)
        except Exception as e:
            print(f"Exception-(handle_exception_log)->{e}")

    def error(self, *args,**kwargs):
        try:
            if not self.logger:
                self.initiate_log()
            msz=str(args)+"\n"+str(kwargs)
            self.logger.error(msz)
        except Exception as e:
            print(f"Exception-(error)->{e}")
