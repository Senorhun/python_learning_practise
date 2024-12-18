import sys
import logging

logging.basicConfig(
    filename = 'app.log',
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d - %(message)s'
)
result = 0
for argumentum in sys.argv[1:]:
    logging.debug(f"Processing argument: {argumentum}")
    result += int(argumentum)

if __name__ == '__main__':
    logging.info(f"Sum of arguments: {result}")
    print(f"\033[91mSUM of arguments:\033[00m {result}")

