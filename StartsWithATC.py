def StartsWithATC(seq):
	# Prints if it starts with ATC
	# else, Prints "starting with AGC" if it starts with AGC
	# else, prints "Starting with Neither"

	if seq.startswith('ATC'):
		print(seq)
	elif seq.startswith('AGC'):
		print('Starting with AGC')
	else:
		print("Starting with neither")
