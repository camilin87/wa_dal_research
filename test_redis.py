# development
# > brew install redis
# > sudo pip install redis
# > redis-server

# deployment
# > sudo apt-get install redis-server
# > sudo pip install redis

from datetime import datetime
from datetime import timedelta
import redis

def main():
    rdb = redis.StrictRedis()

    for day in _get_days(3):
        for hour in _get_hours(1):
            for latitude in _get_coordinate_component(2):
                for longitude in _get_coordinate_component(1):
                    key_str = _get_key(day, hour, latitude, longitude)
                    rdb.hmset(key_str, _get_value())
                    print key_str

def _get_value():
    return {
        "liquid_precipitation_inches": _get_liquid_precipitation_inches(),
        "pop12_percent": _get_pop12_percent(),
        "snow_inches": _get_snow_inches(),
        "apparent_temperature_f": _get_apparent_temperature()
    }

def _get_key(date, hour, latitude, longitude):
    return "location_data:" + "{0}|{1}|{2}|{3}".format(
            date, hour, latitude, longitude
        )

def _get_liquid_precipitation_inches():
    return 0.0

def _get_pop12_percent():
    return 21.0

def _get_snow_inches():
    return 0.0

def _get_apparent_temperature():
    return 55.0

def _get_coordinate_component(max_count):
    for i in range(0, max_count):
        yield "{0:.2f}".format(i / 100.0)

def _get_days(max_days):
    for day_inc in xrange(-max_days, 0):        
        adjusted_date = datetime.utcnow() + timedelta(days=day_inc)
        yield adjusted_date.strftime("%m-%d-%Y")

def _get_hours(max_hour):
    for hour in xrange(0, max_hour):
        yield hour

if __name__ == "__main__":
    main()
