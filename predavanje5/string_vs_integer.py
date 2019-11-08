import sys

print('Prazan int je', sys.getsizeof(int()), 'bytes')
print('Prazan str je', sys.getsizeof(str()), 'bytes')

print('\nint=1 je', sys.getsizeof(int(1)), 'bytes')
print("str='1' je", sys.getsizeof(str("1")), 'bytes')

print('\nint=1111 je', sys.getsizeof(int(1111)), 'bytes')
print("str='1111' je", sys.getsizeof(str("1111")), 'bytes')

print('\nint=65000 je', sys.getsizeof(int(65000)), 'bytes')
print("str='65000' je", sys.getsizeof(str("65000")), 'bytes')
print("str='6500ž' je", sys.getsizeof(str("6500ž")), 'bytes')