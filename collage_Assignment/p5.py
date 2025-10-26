#bit Operations

val =0xCAFE
Last4 =val & 0xF
if bin(Last4).count('1')>=3:
    print("At least three of last four bits are ON")
else:
    print("Less than three are ON")

reservedValue=((val & 0xFF)<< 8) | ((val>>8) & 0xFF)
print("Reserved byte order =", hex(reservedValue))

rotatedValue=((val<<4) |(val >> 12)) & 0xFFFF
print("Rotate 4 bits =", hex(rotatedValue))
