from time import sleep, time


class LocalApp(object):
    def run(self):
        self.start()
        try:
            self.watch(self.handler, 1)
        except KeyboardInterrupt:
            self.end()

    def start(self):
        print("DO some preparation")

    def end(self):
        print("DO some cleaning")

    def watch(self, handler, t_interval):
        start_t = time()
        while True:
            sleep(t_interval)
            handler()
            running_time = int(time() - start_t)
            print("\rServer is running for {}s".format(running_time), flush=True)

    def handler(self):
        print("handle some work")
