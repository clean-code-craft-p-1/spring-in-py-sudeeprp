
def calculateStats(fahrenheit_readings):
  if len(fahrenheit_readings) == 0:
    not_a_number = float("nan")
    return {"avg": not_a_number, "max": not_a_number, "min": not_a_number}

  return {
    "avg": sum(fahrenheit_readings) / len(fahrenheit_readings),
    "max": max(fahrenheit_readings),
    "min": min(fahrenheit_readings),
  }
