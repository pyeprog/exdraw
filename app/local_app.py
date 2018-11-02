from time import sleep, time


class LocalApp(object):
    def run(self):
        start_t = time()
        while True:
            sleep(1)
            running_time = int(time() - start_t)
            print("\rServer is running for {}s".format(running_time), end="", flush=True)
