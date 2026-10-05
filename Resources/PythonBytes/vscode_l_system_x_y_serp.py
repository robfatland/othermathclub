from turtle import Turtle, Screen, tracer, update

def RuleS(s):
  ns = ''
  for c in s:
    if   c == 'x': ns += 'y+x+y'                 
    elif c == 'y': ns += 'x-y-x'
    else:          ns += c
  return ns

def DrawTheorem(t, s, d, x0, y0):
  '''
  t is a turtle
  s is a theorem string (only pay attention to '+' and '-')
      Every + means: t.right(60) and t.forward(d)
      Every - means: t.left(60) and t.forward(d)
  d is how far to move after each turn
  Returns: (min_x, max_x, min_y, max_y) - bounding box of the drawing
  '''
  tracer(0,0)
  t.penup()
  t.setpos(x0, y0)
  t.pendown()
  t.dot()
  
  # Track extrema for bounding box
  min_x = max_x = x0
  min_y = max_y = y0
  
  for c in s:
    if c == '+': 
      t.right(60); 
      t.pencolor('red');  
      t.forward(d)
    if c == '-': 
      t.left(60);  
      t.pencolor('blue'); 
      t.forward(d)
    
    # Update extrema
    x, y = t.pos()
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
  
  update()
  return (min_x, max_x, min_y, max_y)

# Up above we have defined two functions
#   RuleS() substitutes substrings inside a longer string
#   DrawCommand() has the turtle draw a command
# Now: Here is where things get going!

if __name__ == '__main__':
  screen = Screen()
  t = Turtle()
  print(t)
  t.hideturtle()        # do not show the little arrow
  t.speed(0)            # draw as fast as possible

  
  s = 'x'              # s is the command string
  iterate = 10          # iterate is how many times to apply Rule S
  x0 = 0
  y0 = 0
  if   iterate == 1: forward  = 100
  elif iterate == 2: forward  =  50
  elif iterate == 3: forward  =  25
  elif iterate == 4: forward  =  18
  elif iterate == 5: forward  =  12
  elif iterate == 6: forward  =   7
  elif iterate == 7: forward  =   4
  elif iterate == 8: forward  =   3
  elif iterate == 9: forward  = 1.5
  else:              forward  =  .5


  print('\nHere is the command at the start:\n')
  print(s)


  # this keeps feeding s back into RuleS()
  for i in range(iterate): s = RuleS(s)

  print('\nAfter iteration: \n')
  print(s[0:60])

  # this little fix helps keep the figure in view
  # if iterate%2: t.left(60)

  # First pass: draw to get bounding box (invisible)
  bbox = DrawTheorem(t, s, forward, x0, y0)
  
  # Print bounding box information
  min_x, max_x, min_y, max_y = bbox
  width = max_x - min_x
  height = max_y - min_y
  box_size = max(width, height)
  
  print(f'\nBounding box:')
  print(f'  X: [{min_x:.2f}, {max_x:.2f}] (width: {width:.2f})')
  print(f'  Y: [{min_y:.2f}, {max_y:.2f}] (height: {height:.2f})')
  print(f'  Square bounding box size: {box_size:.2f}')
  
  # Scale and center the display based on bounding box
  padding = box_size * 0.1  # 10% padding around the figure
  center_x = (min_x + max_x) / 2
  center_y = (min_y + max_y) / 2
  half_size = box_size / 2 + padding
  
  # Clear and set world coordinates
  t.clear()
  screen.setworldcoordinates(
    center_x - half_size,  # llx (lower left x)
    center_y - half_size,  # lly (lower left y)
    center_x + half_size,  # urx (upper right x)
    center_y + half_size   # ury (upper right y)
  )
  
  print(f'\nDisplay centered at ({center_x:.2f}, {center_y:.2f})')
  print(f'Display range: [{center_x - half_size:.2f}, {center_x + half_size:.2f}]')
  
  # Second pass: redraw with proper scaling
  DrawTheorem(t, s, forward, x0, y0)

  input('Press Enter to close the window...')
