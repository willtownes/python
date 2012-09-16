import logging,types
def makelogger(filename='log.txt'):
    '''returns a logger object that will write to specified file.
    Remember to call logging.shutdown() or log.removeHandler() to
    remove the lock on the log file at the end of logging.'''
    log = logging.getLogger('log')
    log.setLevel(logging.INFO)
    fh = logging.FileHandler(filename)
    logfrmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(logfrmt)
    log.addHandler(fh)
    log.info("Starting the log...")
    return log

if __name__ == "__main__":
    log = makelogger()
    try:
        log.info("Informational message")
        log.warning("Warning message")
        log.info("final log message")
        raise Exception
    except Exception as e:
        log.exception(e)
    finally:
        logging.shutdown()
