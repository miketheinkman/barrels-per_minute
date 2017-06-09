from time import sleep
from threading import Thread


barrels = 0


def new_barrels():
    global barrels

    while True:
        barrels = input()


def counter():
    global barrels
    running_barrels = 0

    while True:
        running_barrels += int(barrels)
        barrels_five_sec = running_barrels / 12
        for _ in range(30):
            print()
        print("Current barrels: %s" % barrels)
        print("Running Barrels: %s" % "{:,.2f}".format(barrels_five_sec))
        print("Enter Barrels Per Minute:")
        sleep(5)


if __name__ == '__main__':
    Thread(target=counter).start()
    Thread(target=new_barrels).start()
