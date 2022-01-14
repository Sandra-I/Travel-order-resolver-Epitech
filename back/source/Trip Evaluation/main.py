import evaluate_city as ec
import evaluate_token as et
import evaulate_token_strength as ets
import evaluate_trip as etr

import test as test

def main_test(str):
  cities, doc = ec.evaluate_city(str)
  # if len(cities) == 1:
  #   return cities
  if cities == 83:
    return "Invalid Sentence."
  tokens = et.evaluate_token(cities, doc)
  tokens_strength = ets.evaluate_token_strength(tokens)
  city_order = etr.evaluate_trip(tokens_strength)
  return city_order

right = 0
nb_of_request = len(test.test_string)

for i in range(len(test.test_string)):
  str, trip_expected = test.test_string[i]
  trip = main_test(str)
  print("\n\n")
  print(f"trip:    {trip}")
  print(f"trip expected: {trip_expected}")
  if trip == trip_expected:
    right = right + 1
    print("RIGHT ANSWER")
  else:
    print("WRONG ANSWER")
  print("\n\n")


accuracy = (right/nb_of_request) * 100
print("The accuracy of the model is ", accuracy, " with ", nb_of_request, "requests.")
