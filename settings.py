import configparser
import os

conf = configparser.ConfigParser()
conf.read('settings.ini')

discord_access_token = os.environ.get('DISCORD_ACCESS_TOKEN')
active_channel_name = os.environ.get('ACTIVE_CHANNEL_NAME')

db_url = os.environ.get('DATABASE_URL')

win_rate = float(conf['honda']['win_rate'])
refresh_hour = int(conf['honda']['refresh_hour'])
hour_shift_from_utc = int(conf['honda']['hour_shift_from_utc'])
refresh_hour_utc = refresh_hour - hour_shift_from_utc if refresh_hour >= hour_shift_from_utc else 24 + \
    refresh_hour - hour_shift_from_utc
