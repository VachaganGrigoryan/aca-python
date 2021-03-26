import time
import logging

logging.basicConfig(format="Datetime :: %(asctime)s %(message)s!")


def retry(exceptions: tuple, tries: int, delay: int, backoff: int, logger: logging.Logger):
    """
    Decorator should have following arguments:
    :param exceptions: tuple of exception in which cases function should be retried
    :param tries: how many times should function be retried
    :param delay: seconds interval between retries
    :param backoff: multiplier e.g. value of 2 will double the delay each retry
    :param logger: logger to log retries if you don't use logger just print following strings --> "Datetime :: Retrying <function_name> xth time!"
    :return:
    """

    def decorator(func):
        def inner_retry(*args, **kwargs):
            mtries = 1
            while mtries < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    msg = f"Retrying <{func.__name__}> {mtries}th time"
                    mtries += 1
                if logger is None:
                    logging.exception(msg)
                else:
                    logger.exception(msg)
                mdelay = delay * backoff
                time.sleep(mdelay)
            return func(*args, **kwargs)
        return inner_retry
    return decorator
