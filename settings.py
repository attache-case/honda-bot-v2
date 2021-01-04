import configparser
import os

conf = configparser.ConfigParser()
conf.read('settings.ini')

discord_access_token = os.environ.get('DISCORD_ACCESS_TOKEN')
active_channel_name = conf['discord']['active_channel_name']

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_hostname = os.environ.get('DB_HOSTNAME')

db_dbname = conf['db']['dbname']
db_dialect = conf['db']['dialect']
db_driver = conf['db']['driver']

win_rate = float(conf['honda']['win_rate'])
refresh_hour = int(conf['honda']['refresh_hour'])
hour_shift_from_utc = int(conf['honda']['hour_shift_from_utc'])
refresh_hour_utc = refresh_hour - hour_shift_from_utc if refresh_hour >= hour_shift_from_utc else 24 + \
    refresh_hour - hour_shift_from_utc
