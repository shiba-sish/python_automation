import logging

class LogGen:
    @staticmethod
    def logGen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%m%d%Y %I:%M:%S %p",
                            force=True)
        logg=logging.getLogger()
        logg.setLevel(logging.INFO)
        return logg