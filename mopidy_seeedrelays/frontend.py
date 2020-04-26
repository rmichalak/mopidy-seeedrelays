import logging

import pykka
import smbus

from mopidy import core

DEVICE_REG_MODE1 = 0x06

logger = logging.getLogger(__name__)


class SeeedRelaysFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(SeeedRelaysFrontend, self).__init__()
        self.i2c = config["seeedrelays"]["i2c"]
        self.device_address = int(config["seeedrelays"]["address"], 0)
        self.relay = config["seeedrelays"]["relay"]

        self.bus = smbus.SMBus(self.i2c)

    def playback_state_changed(self, old_state, new_state):
        if new_state == 'playing':
            self.__check_and_set_relay_state(True)
        if new_state == 'stopped':
            self.__check_and_set_relay_state(False)
        pass

    def __check_and_set_relay_state(self, new_state):

        data = self.bus.read_byte_data(self.device_address, DEVICE_REG_MODE1)
        mask = 1 << (self.relay - 1)
        current_state = (data & mask) == 0

        if current_state != new_state:
            if new_state:
                data &= ~(0x1 << (self.relay - 1))
            else:
                data |= (0x1 << (self.relay - 1))
            self.bus.write_byte_data(self.device_address, DEVICE_REG_MODE1, data)
