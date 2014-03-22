# development
# > brew install redis
# > sudo pip install redis
# > redis-server

# deployment
# > sudo apt-get install redis-server
# > sudo pip install redis

from datetime import datetime
from datetime import timedelta

def main():
    for day in _get_days(3):
        for hour in _get_hours(24):
            print day, hour

def _get_days(max_days):
    for day_inc in xrange(-max_days, 0):        
        adjusted_date = datetime.utcnow() + timedelta(days=day_inc)
        yield adjusted_date.strftime("%m-%d-%Y")

def _get_hours(max_hour):
    for hour in xrange(0, max_hour):
        yield hour

if __name__ == "__main__":
    main()
