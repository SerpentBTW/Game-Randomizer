import json
import random

with open("gameRandomizer\main.json") as f:
  data = json.load(f)


gameCount = len(data["Games"])
rand = random.randint(0, gameCount - 1 )
print(data["Games"][rand])


#new test