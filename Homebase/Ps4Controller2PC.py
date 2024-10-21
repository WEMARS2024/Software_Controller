from inputs import get_gamepad
import math
import threading
import socket

class PS4Controller(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.LeftStickY = 0
        self.LeftStickX = 0
        self.RightStickY = 0
        self.RightStickX = 0
        self.L2Trigger = 0
        self.R2Trigger = 0
        self.L1Button = 0
        self.R1Button = 0
        self.CrossButton = 0
        self.CircleButton = 0
        self.TriangleButton = 0
        self.SquareButton = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.ShareButton = 0
        self.OptionsButton = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self):
        LX = self.LeftStickX
        LY = self.LeftStickY
        RX = self.RightStickX
        RY = self.RightStickY
        cross = self.CrossButton
        circle = self.CircleButton
        return [cross, circle, LX, LY, RX, RY]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftStickY = event.state / PS4Controller.MAX_JOY_VAL
                elif event.code == 'ABS_X':
                    self.LeftStickX = event.state / PS4Controller.MAX_JOY_VAL
                elif event.code == 'ABS_RY':
                    self.RightStickY = event.state / PS4Controller.MAX_JOY_VAL
                elif event.code == 'ABS_RX':
                    self.RightStickX = event.state / PS4Controller.MAX_JOY_VAL
                elif event.code == 'ABS_Z':
                    self.L2Trigger = event.state / PS4Controller.MAX_TRIG_VAL
                elif event.code == 'ABS_RZ':
                    self.R2Trigger = event.state / PS4Controller.MAX_TRIG_VAL
                elif event.code == 'BTN_TL':
                    self.L1Button = event.state
                elif event.code == 'BTN_TR':
                    self.R1Button = event.state
                elif event.code == 'BTN_SOUTH':
                    self.CrossButton = event.state
                elif event.code == 'BTN_NORTH':
                    self.TriangleButton = event.state
                elif event.code == 'BTN_WEST':
                    self.SquareButton = event.state
                elif event.code == 'BTN_EAST':
                    self.CircleButton = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.ShareButton = event.state
                elif event.code == 'BTN_START':
                    self.OptionsButton = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state

# Set up the UDP client
ps4_ip = "192.168.137.40"   # Replace with server's IP address
ps4_port = 2222             # Replace with server's listening port

# Create a UDP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == '__main__':
    ps4_controller = PS4Controller()
    while True:
        print(ps4_controller.read())
        # sock.sendto(str(ps4_controller.read()).encode(), (ps4_ip, ps4_port))
