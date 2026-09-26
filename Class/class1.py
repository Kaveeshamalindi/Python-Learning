class piglet:
    years=0
    def pig_years(self):
        return self.years * 18
    
piggy = piglet()
print(piggy.pig_years())

piggy.years=2
print(piggy.pig_years())