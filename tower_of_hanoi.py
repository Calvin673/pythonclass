def towerOfHanoi(n, source = 'A', auxiliary = 'B', destination = 'C'): 
  if n == 1: 
    print("move from", source, "to", destination)
  else:
    towerOfHanoi(n-1, source, destination, auxiliary) 
    print("move from", source, "to", destination)
    towerOfHanoi(n-1, auxiliary, source, destination)


n = int(input("Enter the number of disks: "))
print("The sequence of moves involved in the Tower of Hanoi are:")
towerOfHanoi(n)