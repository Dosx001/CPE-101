# Name:		Andres Rodriguez 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Moonlander
# Term:         Winter 2020


def main():
	show_welcome()
	x = get_altitude()
	fa = get_fuel()
	v = 0
	t = 0
	fr = 0
	while x > 0:
		display_state(t, x, v, fa, fr)
		t += 1
		if fa != 0:
			fr = get_fuel_rate(fa)
		else:
			fr = 0
		a = update_acceleration(1.62, fr)
		x = update_altitude(x, v, a)
		v = update_velocity(v, a)
		fa = update_fuel(fa, fr)
	display_state(t, x, v, fa, fr)
	display_landing_status(v)
	

def show_welcome():
	print('\nWelcome aboard the Lunar Module (LM) Flight Simulator!\n')
	print('  To begin, provide an initial altitude and fuel amount.')
	print('  To simulate the actual LM, use 1300 meters and 500 liters.\n')
	


def get_altitude():
	x = 0
	while x < 1 or x > 9999:
		x = int(input('Enter initial altitude (1 to 9999 meters): '))
		if x >= 1 and x <= 9999:
			return x
		else:
			print('[ERROR] Altitude out of range')


def get_fuel():
	x = -1
	while x <= 0:
		x = int(input('Enter initial fuel amount (in liters): '))
		if x > 0:
			return x
		else:
			print('[ERROR] Fuel amount must be positive')


def get_fuel_rate(fa):
	x = 10
	while x < 0 or x > 9:
		x = int(input('Enter fuel rate (0 to 9 liters per second): '))
		if x >= 0 and x <= 9:
			if x > fa:
				return fa
			else: 
				return x
		else:
			print('[ERROR] Fuel rate out of range')


def display_state(t, x, v, fa, fr):
	x = float(x)
	v = float(v)
	if t == 0:
		print('\nLM state at retrorocket cutoff')
	if x == 0:
		print('\nLM state at landing/impact')
	if fa > 0 or x == 0:
		print(f"    Time: {t:4} s")
		print(f"    Fuel: {fa:4} l")
		print(f"    Rate: {fr:4} l/s")
		print(f"Altitude: {x:7.2f} m")
		print(f"Velocity: {v:7.2f} m/s\n")	
	else:
		print(f"[OUT OF FUEL] Time: {t:4} Altitude: {x:7.2f} Velocity: {v:7.2f}")


def display_landing_status(v):
	if v >= -1:
		print('[LANDING STATUS] The Eagle has landed!')
	elif v > -10 and v < -1: 
		print('[LANDING STATUS] Enjoy your oxygen while it lasts!')
	else:
		print('[LANDING STATUS] Ouch, that hurt!')



def update_acceleration(g, fr):
	return 1.62 * (fr / 5 - 1)


def update_altitude(x, v, a):
	x2 = x + v + (a / 2)
	if x2 > 0:
		return x2
	else:
		return 0


def update_velocity(v, a):
	return v + a


def update_fuel(fa, fr):
	if fr > fa:
		return 0
	else:
		return fa - fr


if __name__ == "__main__":
    main()
