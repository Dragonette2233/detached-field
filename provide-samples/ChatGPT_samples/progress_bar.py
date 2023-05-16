import time
from progress.spinner import Spinner

mylist = [1,2,3,4,5,6,7,8]

bar = Spinner('Countdown', max = len(mylist))

for item in mylist:
    bar.next()
    time.sleep(1)

bar.finish()
