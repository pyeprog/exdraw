from os.path import join, realpath


class LocalConfig:
    WATCH_PATH = join(realpath("."), "underwatch")
