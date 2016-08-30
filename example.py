import glog as log

# Should print all logs.
log.setLevel(log.DEBUG)
log.info("It works.")
log.warn("Something not ideal")
log.error("Something went wrong")
log.fatal("AAAAAAAAAAAAAAA!")

# Should only print ERROR and FATAL level logs.
log.setLevel(log.ERROR)
log.info("It works.")
log.warn("Something not ideal")
log.error("Something went wrong")
log.fatal("AAAAAAAAAAAAAAA!")

log.check(False)
