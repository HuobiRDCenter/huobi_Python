class WebsocketRequest(object):

    def __init__(self):
        self.subscription_handler = None
        self.is_trading = False
        self.error_handler = None
        self.json_parser = None
        self.update_callback = None
