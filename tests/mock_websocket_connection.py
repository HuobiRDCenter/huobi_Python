
class MockWebsocketConnection:
    def __init__(self, request):
        self.request = request
        self.send_data_buffer = list()

    def send(self, data):
        self.send_data_buffer.append(data)

    def pop_output_message(self):
        return self.send_data_buffer.pop(0)


