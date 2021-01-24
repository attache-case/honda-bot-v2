from datetime import datetime
from datetime import timedelta

import settings


def get_next_refresh_utc():
    now = datetime.utcnow()
    if now.hour < settings.refresh_hour_utc:
        return now.replace(hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0)
    else:
        return now.replace(day=now.day+1, hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0)


def get_prev_refresh_utc():
    now = datetime.utcnow()
    return get_prev_refresh_utc(now)


def get_prev_refresh_utc(now):
    if now.hour < settings.refresh_hour_utc:
        return now.replace(day=now.day-1, hour=settings.refresh_hour_utc, minute=0, second=0, microsecond=0)
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
