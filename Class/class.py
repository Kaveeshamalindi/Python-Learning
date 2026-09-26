class piglet:
    pass
hamlet=piglet()

#--------------------------------------------------------------------------

class piglet:
    def speak(self):
        print("Oink Oink")
hamlet = piglet()
hamlet.speak()

#--------------------------------------------------------------------------------------

class piglet:
    name="piglet"
    def speak(self):
        print("Oink! I'm {}! Onik!".format(self.name))

hamlet=piglet()
hamlet.name="Hamlet"
hamlet.speak()

petunia=piglet()
petunia.name="petunia"
petunia.speak()

#-----------------------------------------------------------------------------------------------------------------------------

class piglet:
    years=0
    def pig_years(self):
        return self.years * 18
    
piggy = piglet()
print(piggy.pig_years())

piggy.years=2
print(piggy.pig_years())



