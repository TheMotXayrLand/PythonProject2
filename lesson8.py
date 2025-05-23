import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="a",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
try:
    print(10/0)
except Exception:
    logging.exception("Exception")


def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
