from datetime import datetime
from custom_logger import CustomLogger

def handle_exception(
    log=True,print_exception=True,stop_execution=False,log_exe_time=False,skip_args=False,
    log_file_name=datetime.now().strftime(f"%d-%m-%Y.log"),
    log_path="logs"
    ):
    """handeles exception and logs 

    Args:
        log (bool, optional): _description_. Defaults to True. set False if log is not necessary
        print_exception (bool, optional): _description_. Defaults to True.
        stop_execution (bool, optional): _description_. Defaults to False. Set true if functions needs to raise exception
        log_exe_time (bool, optional): _description_. Defaults to False. print the executing time of a function
        skip_args (bool, optional): _description_. Defaults to False. To not to include args in log file
        log_file_name (_type_, optional): _description_. Defaults to datetime.now().strftime(f"%d-%m-%Y.log").
        log_path (str, optional): _description_. Defaults to "logs".

    """
    c_logger=CustomLogger(log_file_name=log_file_name,log_path=log_path)
    def main_decorator(func):
        def wrapper_func(*args,**kwargs):
            try:
                if not log_exe_time:
                    return func(*args,**kwargs)
                else:
                    from helper_functions import get_execution_time
                    func_result,time_str= get_execution_time(func,*args,**kwargs)
                    c_logger.debug(time_str) 
                    return func_result        
            except Exception as e:
                if print_exception:
                    print(f"Exception->{func.__name__}->{e}")
                if log:
                    if skip_args:
                        c_logger.handle_exception_log(method_name=func.__name__,exception_str=str(e))
                    else:
                        c_logger.handle_exception_log(exception_str=str(e),method_name=func.__name__,args=args,kwargs=kwargs)
                if stop_execution:
                    raise e
        return wrapper_func
    return main_decorator


# example of how to use
if __name__=="__main__":
    @handle_exception(skip_args=False,log_file_name="test_name.log",log_exe_time=True)
    def test_decoretor(name,k="sdsd"):
        print("Testing main func")
    test_decoretor("Rifat",k="sdsd")