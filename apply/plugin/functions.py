import time
from progress.bar import ChargingBar

def plugin(language, stack_name):
    print('Plugin is being add to {0} stack...'.format(stack_name))
    if language != "":
        download('Building plugin in {0} ...'.format(language), 200)
    else:
        download('Building plugin...', 200)
    print('Plugin added successfully to stack {0} !'.format(stack_name))

def download(message, value):
    bar = ChargingBar(message, max=value)
    for i in range(value):
        time.sleep(0.010)
        bar.next()
    bar.finish()