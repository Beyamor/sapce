LOG_CRITICAL = 1
LOG_ERROR = 2
LOG_WARNING = 3
LOG_INFO = 4
LOG_DEBUG = 5

log_level = LOG_DEBUG

def logmsg(msg, level=LOG_DEBUG):
	if level <= log_level:
		print msg
