# Напишите функцию, которая принимает количество дней от текущей даты и # возвращает дату, которая наступит через указанное количество дней.
# Дополнительно, выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta


def future_date(days):
    now = datetime.now()
    future = now + timedelta(days=days)
    format_date = future.strftime('%Y-%m-%d')
    return format_date


print(future_date(10))
