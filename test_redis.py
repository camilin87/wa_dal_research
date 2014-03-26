# development
# > brew install redis
# > sudo pip install redis
# > redis-server

# deployment
# > sudo apt-get install redis-server
# > sudo pip install redis

# sudo sh -c 'echo 1 > /proc/sys/vm/overcommit_memory'
# sudo sed -i 's/appendonly no/appendonly yes/g' /etc/redis/redis.conf

from datetime import datetime
from datetime import timedelta
import redis

def main():
    days_count = 4
    hours_count = 12
    latitudes_count = 50
    longitudes_count = 800
    total = days_count * hours_count * latitudes_count * longitudes_count
    current = 0

    expiration = days_count * hours_count * 60 * 60
    rdb = redis.StrictRedis()
    rpipe = rdb.pipeline()

    for day in _get_days(days_count):
        for hour in _get_hours(hours_count):
            for latitude in _get_coordinate_component(latitudes_count):
                for longitude in _get_coordinate_component(longitudes_count):
                    key_str = _get_key(day, latitude, longitude)
                    rpipe.hmset(key_str, _get_value(hour)).expire(key_str, expiration).execute()

                current += longitudes_count
                percent = current * 100.0 / total
                line_str = "{0:.2f}% {1}".format(percent, key_str)
                _log_progress(line_str)

def _log_progress(line_str):
    print line_str

def _get_value(hour):
    return {
        _format_value("liquid_precipitation_inches", hour): _get_liquid_precipitation_inches(),
        _format_value("pop12_percent", hour): _get_pop12_percent(),
        _format_value("snow_inches", hour): _get_snow_inches(),
        _format_value("apparent_temperature_f", hour): _get_apparent_temperature()
    }

def _format_value(value_name, hour):
    return "{0}-{1}".format(value_name, hour)

def _get_key(date, latitude, longitude):
    return "location_data:" + "{0}:{1}:{2}".format(
            date, latitude, longitude
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
