from a_numb3rs import validate

def test256():
  assert validate("256.255.255.255") == False
  assert validate("255.255.255.256") == False
def test4reps():
  assert validate("1.2.3.4") == True
  assert validate("1.2.3.4.5") == False
  assert validate("1.2.3") == False
def testcat():
  assert validate("cat") == False