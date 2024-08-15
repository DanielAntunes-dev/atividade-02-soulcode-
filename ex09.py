def inverter_string(s):
  if len(s) == 0:
    return ''
  else:
    return s[-1] + inverter_string(s[:-1])
  
print(inverter_string("resursividade"))