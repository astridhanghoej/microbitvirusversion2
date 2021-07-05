def on_received_number(receivedNumber):
    global sickCounter, isInfected
    # Only happens if receiving microbit has non-infected status.
    if not (isInfected):
        sickCounter += linearConversion(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH),
            -128,
            -42,
            0,
            1)
    # When receiving a signal and sickCounter is high enough, infect this microbit.
    if not (isInfected) and sickCounter > 10:
        isInfected = 1
        basic.show_icon(IconNames.SKULL)
radio.on_received_number(on_received_number)

def linearConversion(x: number, in_min: number, in_max: number, out_min: number, out_max: number):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
# This handle ensures that one or more microbits can be set to patient zero during game play.

def on_button_pressed_ab():
    global isInfected
    isInfected = 1
    basic.clear_screen()
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

isInfected = 0
sickCounter = 0
sickCounter = 0
isInfected = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    if isInfected:
        radio.send_number(isInfected)
    # The virus only transmits every 5 seconds so there is a chance you could be close to someone who is infected and not know it.
    # 
    # Tweak it to make it less visible to people around you.
    control.wait_micros(1000000)
basic.forever(on_forever)
