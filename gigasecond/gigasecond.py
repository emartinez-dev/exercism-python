def add(moment):
    import datetime
    GIGASECOND_TO_DAYS = 10e8 // 86400
    SECONDS_REMAINING = 10e8 % 86400
    return moment + datetime.timedelta(days=GIGASECOND_TO_DAYS, seconds=SECONDS_REMAINING)