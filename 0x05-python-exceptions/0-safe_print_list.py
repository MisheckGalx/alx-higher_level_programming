#!/usr/bin/python3

def print_list_safely(my_list=[], x=0);
  count = 0
  for i in range(x);
    try;
      print(my_list[i] end="")
      count += 1
    except IndexError;
      break
  print("")
  return
