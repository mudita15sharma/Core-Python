class Trail:

    def __init__(self):
        print("Welcome in Trails...")

    def trial_1(self,function1):
        print('Calling function one through object, Tell us your name\n', function1)

    def trail_2(self,function2):
        print('Calling function one through object, Tell us your name\n', function2)

obj= Trail()
obj.trial_1('abc')
obj.trail_2('xyz')


print("\nYou Got it!!!")
