input.onButtonPressed(Button.A, function () {
    led.unplot(x, y)
    if (x == 0) {
        if (y == 0) {
            x = 4
            y = 4
            led.plot(x, y)
        } else {
            x = 4
            y += -1
            led.plot(x, y)
        }
    } else {
        x += -1
        led.plot(x, y)
    }
})
input.onButtonPressed(Button.B, function () {
    led.unplot(x, y)
    if (x == 4) {
        if (y == 4) {
            x = 0
            y = 0
            led.plot(x, y)
        } else {
            x = 0
            y += 1
            led.plot(x, y)
        }
    } else {
        x += 1
        led.plot(x, y)
    }
})
let y = 0
let x = 0
x = 0
y = 0
led.plot(x, y)
basic.forever(function () {
	
})
