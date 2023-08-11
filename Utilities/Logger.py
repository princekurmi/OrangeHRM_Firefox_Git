import inspect
import logging


class LogGenerator:

    @staticmethod
    def log_gen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:/Software Testing/TK OrangeHRM/Logs/OrangeHRM_Automation.log")
        formatt = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d :%(message)s")
        logfile.setFormatter(formatt)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


"""
get log --> logging.getLogger()         made object of logging.getLogger()
log file --> path and name              Gave path and name to file location
Define Log format --> logs format       Defined Log Format
setFormatter --> link file to format    Link the File and format
addHandler --> maintain log file        Maintain the logfile according to the log
"""
