radio.onReceivedNumber(function (receivedNumber) {
    // Only happens if receiving microbit has non-infected status.
    if (!(isInfected)) {
        sickCounter += linearConversion(radio.receivedPacket(RadioPacketProperty.SignalStrength), -128, -42, 0, 1)
    }
    // When receiving a signal and sickCounter is high enough, infect this microbit.
    if (!(isInfected) && sickCounter > 10) {
        isInfected = 1
        basic.showIcon(IconNames.Skull)
    }
})
function linearConversion (x: number, in_min: number, in_max: number, out_min: number, out_max: number) {
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
}
// This handle ensures that one or more microbits can be set to patient zero during game play.
input.onButtonPressed(Button.AB, function () {
    isInfected = 1
    basic.clearScreen()
    basic.showIcon(IconNames.Skull)
})
let isInfected = 0
let sickCounter = 0
sickCounter = 0
isInfected = 0
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (isInfected) {
        radio.sendNumber(isInfected)
    }
    // The virus only transmits every 5 seconds so there is a chance you could be close to someone who is infected and not know it.
    // 
    // Tweak it to make it less visible to people around you.
    control.waitMicros(1000000)
})
