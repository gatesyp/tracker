from pynput.keyboard import Key, Controller, Listener
import csv
import time

# All times are in seconds from epoch

f = open('mouse_data/' + str(time.time()) + '.csv', 'wb')
writer = csv.writer(f)
writer.writerow(('character', 'time'))


def on_press(key):
    return


def on_release(key):
    print(str(key).encode('ascii', 'ignore'))
    writer.writerow((str(key), str(time.time())))
    if key == Key.esc:
        # Stop listener
        f.close()
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


def control():
    keyboard = Controller()

    # Press and release space
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    keyboard.press('a')
    keyboard.release('a')

    # Type two upper case As
    keyboard.press('A')
    keyboard.release('A')
    with keyboard.pressed(Key.shift):
        keyboard.press('a')
        keyboard.release('a')

    # Type 'Hello World' using the shortcut type method
    keyboard.type('Hello World')
