def log_for(logfile, date_str):
    with (
        open(logfile, 'rt', encoding='utf-8') as all_logs,
        open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as date_log
    ):
        for line in all_logs:
            if line.startswith(date_str):
                date_log.write(line.lstrip(date_str + ' '))
        