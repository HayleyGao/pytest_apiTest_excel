import  logging

#定义日志级别的映射
log_lev={
    "info": logging.INFO,
    "debug":logging.DEBUG,
    "warn":logging.WARNING,
    "error":logging.ERROR
}

class logger:
    #输出文件名称，loggername,日志级别
    def __init__(self,log_file,log_name,log_level):
        self.log_file=log_file
        self.log_name=log_name
        self.log_level=log_level

        self.logger=logging.getLogger(self.log_name)
        self.logger.setLevel(log_lev[log_level]) #logging.INFO



        