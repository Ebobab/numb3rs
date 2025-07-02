import re
import sys


def main():
    user_input = input("IPv4 Adress: "
    validated = validate(user_input)
    print(validated)

def validate(ip):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$", ip):
        return True
    else:
        return False
        
if __name__ == "__main__":
    main()
