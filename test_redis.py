# development
# > brew install redis
# > sudo pip install redis
# > redis-server

# deployment
# > sudo apt-get install redis-server
# > sudo pip install redis

import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

r.set("foo", "bar")

print r.get("foo")
