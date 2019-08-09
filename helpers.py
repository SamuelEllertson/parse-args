def isFloat(string):
    try:
        float(string)
        return True
    except Exception:
        return False

def files(path):
    import os
    for entry in os.scandir(path):
        if entry.is_file():
            yield entry

def runAsThreads(inputList):
    """Takes a list of functions, or a list of tuples (function, args, kwargs) and runs them all in parallel with the threading module. Blocks until all functions have finished."""

    import threading

    #type validation
    if type(inputList) != list:
        raise TypeError(f"expected list, received {type(inputList)}")

    threads = []

    for val in inputList:
        #assume default values
        func = val
        args = tuple()
        kwargs = dict()

        #if tuple was provided, extract func, args, and kwargs if possible
        if type(val) == tuple:
            try:
                func = val[0]
                args = val[1]
                kwargs = val[2]
            except IndexError:
                pass

            #syntactic sugar: if provided args not a tuple, make it a tuple
            #this lets you pass in single arguments directly without having to wrap them yourself
            if type(args) != tuple:
                args = (args,)

        #create the thread
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        threads.append(thread)

    #start all the threads
    for thread in threads:
        thread.start()

    #wait for all threads to finish executing
    for thread in threads:
        thread.join()