import threading
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

from huobi.connection.impl.private_def import *
from huobi.utils.time_service import get_current_timestamp


def watch_dog_job(*args):
    watch_dog_obj = args[0]

    for idx, websocket_manage in enumerate(watch_dog_obj.websocket_manage_list):
        if websocket_manage.request.auto_close:  # setting auto close no need reconnect
            pass
        elif websocket_manage.state == ConnectionState.CONNECTED:
            if watch_dog_obj.is_auto_connect:
                ts = get_current_timestamp() - websocket_manage.last_receive_time
                if ts > watch_dog_obj.heart_beat_limit_ms:
                    watch_dog_obj.logger.warning("[Sub][" + str(websocket_manage.id) + "] No response from server")
                    websocket_manage.close_and_wait_reconnect(watch_dog_obj.wait_reconnect_millisecond())
        elif websocket_manage.state == ConnectionState.WAIT_RECONNECT:
            watch_dog_obj.logger.warning("[Sub] call re_connect")
            websocket_manage.re_connect()
            pass
        elif websocket_manage.state == ConnectionState.CLOSED_ON_ERROR:
            if watch_dog_obj.is_auto_connect:
                websocket_manage.close_and_wait_reconnect(watch_dog_obj.reconnect_after_ms)
                pass


class WebSocketWatchDog(threading.Thread):
    mutex = threading.Lock()
    websocket_manage_list = list()

    def __init__(self, is_auto_connect=True, heart_beat_limit_ms=CONNECT_HEART_BEAT_LIMIT_MS, reconnect_after_ms=RECONNECT_AFTER_TIME_MS):
        threading.Thread.__init__(self)
        self.is_auto_connect = is_auto_connect
        self.heart_beat_limit_ms = heart_beat_limit_ms
        self.reconnect_after_ms = reconnect_after_ms if reconnect_after_ms > heart_beat_limit_ms else heart_beat_limit_ms
        self.logger = logging.getLogger("huobi-client")
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(watch_dog_job, "interval", max_instances=10, seconds=1, args=[self])
        self.start()

    def run(self):
        self.scheduler.start()

    def on_connection_created(self, websocket_manage):
        self.mutex.acquire()
        self.websocket_manage_list.append(websocket_manage)
        self.mutex.release()

    def on_connection_closed(self, websocket_manage):
        self.mutex.acquire()
        self.websocket_manage_list.remove(websocket_manage)
        self.mutex.release()

    # calculate next reconnect time
    def wait_reconnect_millisecond(self):
        wait_millisecond = int(self.reconnect_after_ms - self.heart_beat_limit_ms)
        now_ms = get_current_timestamp()
        wait_millisecond = wait_millisecond if wait_millisecond else 1000
        # job loop after 1 second
        return (wait_millisecond + now_ms)



