from datetime import datetime

now = datetime.now()

format_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

day_week = now.strftime('%A')
week_num = now.strftime('%U')

print(f'{format_datetime} - {day_week} - {week_num}')

