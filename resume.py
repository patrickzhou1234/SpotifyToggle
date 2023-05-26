from command import command
from checkTime import checkTime

accessToken = checkTime()

command(accessToken, "resume", "simple")