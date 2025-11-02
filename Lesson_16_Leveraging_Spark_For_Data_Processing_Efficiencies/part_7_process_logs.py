def process_log(line):
    try:
        return line.split()[8], line.split()[6]
    except IndexError:
        return None

processed_logs = log_rdd.map(process_log).filter(lambda x: x is not None)
