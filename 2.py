def is_generator(g, p):
  for n in range(2, p):
    if pow(g, n, p) == g:
      return False
  return True

p = 28151
for g in range(p):
  if is_generator(g, p):
    print("g is", g)
    break