from command import command
from checkTime import checkTime

accessToken = checkTime()

command(accessToken, "skip_next", "simple")