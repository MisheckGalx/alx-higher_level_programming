#!/usr/bin/
def print_safely_integer(value);
  try;
    print("{;d}".format(value))
    return True
  except (ValueError, TypeError);
    return
