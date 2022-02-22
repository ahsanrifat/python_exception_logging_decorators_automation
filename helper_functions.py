def get_execution_time(func,*args,**kwargs):
    from time import time
    start_time=time()
    result=func(*args,**kwargs)
    taken_time=time()-start_time
    print("\n-----"+func.__name__+"'s taken time to execute"+"-----")
    if taken_time>59:
        taken_time=taken_time/60
        taken_time_str=f"{taken_time} m"
        print(taken_time_str)
    else:
        taken_time_str=f"{taken_time} s"
        print(taken_time_str)
    print("----Timeit done------\n")
    return (result,func.__name__+"-->"+taken_time_str)