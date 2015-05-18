# IP or hostname of your MythTV backend
hostname = "<ip or hostname>"

# Port number of your MythTV backend (this is the default, can probably leave as-is)
host_port = "6544"

# A list of MythTV recording directories, full paths in quotes, separated by commas
mythtv_recording_dirs = ["/pool/mythtv/recordings-kids/"]

# Path to write symlinks
symlinks_dir = "/pool/myth2kodi/recordings/"

# API key for TheTVDB
ttvdb_key = "<your ttvdb key>"

# Path to store TheTVDB series zips
ttvdb_zips_dir = "/pool/myth2kodi/ttvdb/"

# API key for TheMovieDB
tmdb_key = "<your tmdb key>"

# MythTV database host, username, password, and database name
db_host = "localhost"
db_user = "mythtv"
db_passwd = "mythtv"
db_name = "mythconverg"

# Comskip location
comskip_exe = "/home/mythtv/comskip/comskip.exe"

# Encoder settings
mythcommflag_verbose = False
tune = film
mythcommflag_enabled = False
nicevalue = 0
profile = high
level = 41
videocodec = libx264
preset = veryfast
remux_enabled = False
deinterlace = True
audiocodec = copy
threads = 2
transcode_enabled = False
