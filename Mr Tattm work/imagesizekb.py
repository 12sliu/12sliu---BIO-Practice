import math

BITS_TO_BYTES = 8
BITS_TO_KILOBYTES = 8_000
BITS_TO_MEGABYTES = 8_000_000

while True:
    width = int(input("width: "))
    height = int(input("height: "))
    color_depth = int(input("color depth: "))

    bits = width * height * math.log(color_depth, 2)

    print(f"Size is {bits} bits")
    print(f"Size is {bits / BITS_TO_KILOBYTES} kilobytes")
    print(f"Size is {bits / BITS_TO_MEGABYTES} megabytes")
