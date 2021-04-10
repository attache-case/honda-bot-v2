from datetime import datetime
from datetime import timedelta

import settings


def get_next_refresh_utc():
    now = datetime.utcnow()
    if now.hour < settings.refresh_hour_utc:
        return now.replace(hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0)
    else:
        return now.replace(hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0) + timedelta(days=1)


def get_prev_refresh_utc():
    now = datetime.utcnow()
    return get_prev_refresh_utc_from(now)


def get_prev_refresh_utc_from(now):
    if now.hour < settings.refresh_hour_utc:
        return now.replace(day=now.day, hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0) - timedelta(days=1)
    else:
        return now.replace(hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0)


# def get_hello_message():
#     dt_next_refresh = get_next_refresh_utc() + timedelta(hours=settings.hour_shift_from_utc)
#     s = ""
#     s = s + constants.HELLO_MESSAGE_BASE
#     s = s + "（次回のじゃんけん回数リセットは" + \
#         dt_next_refresh.strftime('%Y-%m-%d %H:%M:%S') + "）"
#     return s


def has_keyword(text, keyword_list):
    has_kw = False
    for key in keyword_list:
        if key in text:
            has_kw = True
            break
    return has_kw

def read_famous_saying(path):
    famous_saying_list = []
    with open(path, 'r', encoding='utf-8') as f:
        one_saying = []
        while line:
            line = f.readline()
            line = line.rstrip()
            if line == '-----':
                famous_saying_list.append(one_saying)
                one_saying = []
                continue
            one_saying.append(line)
    return famous_saying_list
