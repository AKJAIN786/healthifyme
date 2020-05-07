import time
print("Welcome to Healthy me")
class User123:
    def __init__(self, name, number):
        self.name = name
        # self.domain = domain
        self.number = number

    @property
    def form(self):
        a = self.name.split()
        global a1, a2
        a1 = a[0]
        a2 = a[1]
        # email = f"{a1}.{a2}@{self.domain}.com"
        return \
            print(f"your info \n*Name-- {self.name},\n*Number-- {self.number} ")

    @staticmethod
    def sound(activity_name):
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.spVoice")
        speak.speak(f"It is time to {activity_name} "
                    f"please get up {m}")
        time.sleep(30)
        speak.speak(f"Type 'Done' in CMD if you're done with this ")

    @staticmethod
    def entry_system(activity_name):
        peal = input("Type Done if you have completed  ")
        with open("Time table", 'a+') as f:
            f.write(f"\n {m} + {activity_name} + {time.asctime()}")
            f.write(f"  Task status {peal}")
            f.close()

while True:
    m = str(input("Provide your full name "))
    o = str(input("Provide Number "))
    metre = User123(m, o)
    print("Enter Time Details in minute")
    BPE = float(input("Enter exercise(At least 30 min)"))
    BPW = float(input("Enter Water(Should be more than Quiet more than Exercise)"))
    joy = float(input("Enter for eye(Should be more than Quiet more than Exercise)"))
    print(metre.form)
    g=input(f"{m}  Can we start Y/N   ")
    if g == "Y":
        print("Now minimize Tab \nWe will handle all")
        x = 0
        while x <= 8:
            time.sleep(30 * BPE)
            User123.sound(" Exercise")
            User123.entry_system("exercise")
            time.sleep(30 * BPW - 30 * BPE)
            User123.sound("Drink Water")
            User123.entry_system('water')
            time.sleep(30 * joy - 30 * BPE)
            User123.sound("Eyes Exercise")
            User123.entry_system('eyes exercise')
    elif g=="N":
        print("something wrong \n**Maybe yor inputs")
    else:print("You're done for Today")
