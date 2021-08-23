from password_generator import PasswordGenerator

def password():
    pwo = PasswordGenerator()
    pwo.minlen = 8 # (Optional)
    pwo.maxlen = 10 # (Optional)
    pwo.minuchars = 1 # (Optional)
    pwo.minlchars = 4 # (Optional)
    pwo.minnumbers = 2 # (Optional)
    pwo.maxchars = 2 # (Optional)

    power =pwo.generate()
    print(power)

if  __name__ == "__main__":
        x = range(10)
        for n in x:
            password()