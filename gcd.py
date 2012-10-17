import math

def gcd(a, b):
	if a < b:
		c = a
		a = b
		b = c
	remainder = b
	while remainder > 0:
		a = b
		b = remainder
		remainder = a % b
	return b

def extendedGcd(a, b):
	swap = False
	if a < b:
		c = a
		a = b
		b = c
		swap = True
	remainder = b
	oldRemainder = b
	u = 0
	v = 1
	oldU = 1
	oldV = 0
	multiplier = 1
	while remainder > 0:
		oldRemainder = remainder
		toSubtract = u * a + v * b
		multiplier = remainder / toSubtract
		multiplier = math.floor(multiplier)
		toSubtract *= multiplier
		remainder -= toSubtract
		newU = u * (- multiplier) + oldU
		oldU = u
		u = newU
		newV = v * (- multiplier) + oldV
		oldV = v
		v = newV
	if swap:
		c = u
		u = v
		v = c
	return (oldRemainder, u, v)

