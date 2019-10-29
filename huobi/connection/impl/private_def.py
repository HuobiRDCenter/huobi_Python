

class ConnectionState:
    IDLE = 0
    CONNECTED = 1
    WAIT_RECONNECT = 2
    CLOSED_ON_ERROR = 3
    CLOSED = 4

CONNECT_HEART_BEAT_LIMIT_MS = 60000   # max interval between two package
RECONNECT_AFTER_TIME_MS = 63000         # if not need connect immediately, it will enter delay connect status and will connect after setting times