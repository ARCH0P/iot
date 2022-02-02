import time
from Adafruit_IO import Client, Feed, RequestError
import pyfirmata

run_count=0
ADAFRUIT_IO_USERNAME = "Archop"
ADAFRUIT_IO_KEY = "aio_rxtE04lzgJAzzpZCklg8wgtUI9uP"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

board = pyfirmata.Arduino('COM6')
it = pyfirmata.util.Iterator(board)
it.start()

digital_output = board.get_pin('d:13:o')
analog_input = board.get_pin('a:1:i')

try:
    digital = aio.feeds('digital')
except RequestError: 
    feed = Feed(name='digital')
    digital = aio.create_feed(feed)

while True:

    print(analog_input.read())

    #print('Sending count:' , run_count)
    aio.send_data('counter' , analog_input.read())

    data = aio.receive(digital.key)

    print('Data: ' , data.value )

    if data.value == "ON":
        digital_output.write(True)
    else:
        digital_output.write(False)
    time.sleep(3)
