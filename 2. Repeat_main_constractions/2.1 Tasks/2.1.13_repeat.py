def annual_return(start, percent, years):
    for _ in range(years):
        start *= (percent + 100)/100
        yield start
