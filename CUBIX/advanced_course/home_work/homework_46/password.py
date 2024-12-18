import getpass
import logging

logging.basicConfig(
    filename = 'app.log',
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d - %(message)s'
)
logging.info("Enter log in information:")
username = input("Username: ")
logging.debug(f"Username entered: {username}")

password = getpass.getpass("Password: ")
logging.info("Password entered (hidden for security)")
print(f"\033[91mUsername:\033[00m {username} \nPassword: {password}")
logging.info("Program completed successfully.")