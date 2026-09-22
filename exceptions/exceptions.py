# Add timestamp and useful information

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Invalid input")
logging.error("Database error")



import logging

logging.basicConfig(
    filename="app.log",
    level=logging.info
)

logging.info('Application Strat')
logging.warning("Invalid input")
logging.error("payment failed")