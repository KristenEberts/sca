import cs50

hour = cs50.get_int("What hour is it? ")
passed = cs50.get_int("How many hours will pass? ")

time = hour + passed

if time > 12:
    time = time % 12

print("In %s hours it will be %s o'clock" % (passed, time))
