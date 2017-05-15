from pynput import mouse
import csv
import time

# All times are in seconds from epoch

f = open('mouse_data/movements/' + str(time.time()) + '.csv', 'wb')
move_writer = csv.writer(f)
move_writer.writerow(('x', 'y', 'time'))


t = open('mouse_data/clicks/' + str(time.time()) + '.csv', 'wb')
click_writer = csv.writer(t)
click_writer.writerow(('x', 'y', 'button', 'time'))


s = open('mouse_data/scrolls/' + str(time.time()) + '.csv', 'wb')
scroll_writer = csv.writer(s)
scroll_writer.writerow(('x', 'y', 'dx', 'dy', 'time'))


def on_move(x, y):
    move_writer.writerow((str(x), str(y), str(time.time())))


def on_click(x, y, button, pressed):
    return True
    # click_writer.writerow((str(x), str(y), str(button), str(pressed), str(time.time())))
    # print(button)
    # print(pressed)
    # if not pressed:
        # Stop listener
        # f.close()
        # t.close()
        # s.close()
        # return False


def on_scroll(x, y, dx, dy):
    scroll_writer.writerow((str(x), str(y), str(dx), str(dy), str(time.time())))


# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
