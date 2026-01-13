import sys 
from networksequrity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details) -> None:
        super().__init__(error_message)
        self.error_message = error_message
        _,_, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self) -> str:
        return f"Error occurred in script: {self.file_name} at line number: {self.lineno} with message: {self.error_message}"
        return self.file_name,self.lineno,str(self.error_message)

if __name__ == "__main__":
    try:
        logger.logging.INFO("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
