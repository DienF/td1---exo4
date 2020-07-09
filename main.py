def on_button_pressed_a():
    global x, y
    led.unplot(x, y)
    if x == 0:
        if y == 0:
            x = 4
            y = 4
            led.plot(x, y)
        else:
            x = 4
            y += -1
            led.plot(x, y)
    else:
        x += -1
        led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x, y
    led.unplot(x, y)
    if x == 4:
        if y == 4:
            x = 0
            y = 0
            led.plot(x, y)
        else:
            x = 0
            y += 1
            led.plot(x, y)
    else:
        x += 1
        led.plot(x, y)
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
x = 0
y = 0
led.plot(x, y)

def on_forever():
    pass
basic.forever(on_forever)
