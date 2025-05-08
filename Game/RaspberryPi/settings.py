import gpiozero

PINS: list[gpiozero.Button] = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

LEDS: dict[str: gpiozero.LED] = {
    "CORRECT": None,
    "INCORRECT": None,
}
