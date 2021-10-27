import time, json, sys

identifier = "python-%s-%s" % (sys.version[:3], sys.platform)
timestamp = time.strftime("%Y-%m-%d T%H%M%SZ", time.gmtime(time.time()))


def lambda_handler(event, context):
    return (
        f"Hello World from Lambda @ Python Version {identifier} executed @ {timestamp}"
