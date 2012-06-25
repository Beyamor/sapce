LOG_CRITICAL = 1
LOG_ERROR = 2
LOG_WARNING = 3
LOG_INFO = 4
LOG_DEBUG = 5

log_prefixes = {
		LOG_CRITICAL: "CRITICAL",
		LOG_ERROR: "ERROR",
		LOG_WARNING: "WARNING",
		LOG_INFO: "DEBUG INFO",
		LOG_DEBUG: "DEBUG"
		}


log_level = LOG_DEBUG

def logmsg(msg, level=LOG_DEBUG):
	msg = str(msg)
	if level <= log_level:
		print log_prefixes[level] + ": " + msg
