from pynput.keyboard import Key, Listener
import csv
import time


class KeyboardMonitor:
    def __init__(self):
        self.f = open('mouse_data/' + str(time.time()) + '.csv', 'wb')
        self.writer = csv.writer(self.f)
        self.writer.writerow(('character', 'time'))

    def on_press(self, key):
        return

    def on_release(self, key):
        self.writer.writerow((str(key), str(time.time())))
        if key == Key.esc:
            # Stop listener
            self.f.close()
            return False

    # Collect events until released
    def run_keyboard(self):
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
