import concurrent.futures
import logging

def init():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(process)d - %(levelname)s - %(message)s")
    logging.info("app initialized")
    return True

def  main():
    logging.info("main started")
    logging.info("main ended")

if __name__ == "__main__":
    init()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as worker:
        worker.submit(main)
    logging.info("app finished")
