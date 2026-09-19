from time import time, sleep

a = 1; b = 1
print("First logic check")
print(a == b)
if a == b: print(True)
else:      print(False)

a = 0
print("Second logic check")
print(a == b)
print(not (a == b))

print(not ((a == b) or not (a == b))) 

toc = time()
print(toc)
sleep(3)
tic = time()
print(tic)
print('elapsed time (seconds) =', tic - toc)
print(tic - toc > 0)
print(not (tic - toc > 0))

print('End of logic examples')
