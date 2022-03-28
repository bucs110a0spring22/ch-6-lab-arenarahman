import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        
        if(n % 2) == 0:        # n is even
            n = n // 2
            count = count + 1
        else:                 # n is odd
            n = n * 3 + 1
            count = count + 1
    return count            # the last print is 1

def graph_max_iterations(n):
  writer = turtle.Turtle()
  wn = turtle.Screen()
  wn.mode('world')
  wn.reset()
  wn.setworldcoordinates(0,0,10,10)
  grapher = turtle.Turtle()
  max_so_far = 0
  for iterations in range(1,n + 1):
    result = seq3np1(iterations)
    if result > max_so_far:
      max_so_far = result
    writer.clear()
    writer.penup()
    writer.goto(0,max_so_far)
    message = "Maximum so far:",iterations,result
    writer.write(message)
    wn.setworldcoordinates(0,0,n+10,max_so_far + 10)
    grapher.goto(iterations,result)
  wn.exitonclick()

def main():
  n = int(input("Value for upper bound of range: "))
  if n <= 0:
    return
  for start in range(1,n + 1):
    count = seq3np1(start)
    print("current value of start:",start,", number of iterations", count)
  graph_max_iterations(n)
  
  

main()




