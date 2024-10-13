from datetime import date

year, month = int(input()), int(input())
for i in range(1, 8):
    if date(year, month, i).weekday() == 3:
        four_thurday = i + 21
        break
result_date = date(year, month, four_thurday)         
print(result_date.strftime('%d.%m.%Y'))