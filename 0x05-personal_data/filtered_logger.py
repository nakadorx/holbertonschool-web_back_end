#!/usr/bin/env python3
"""
holb
"""

import re
import logging
import os
from typing import List
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ holb """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        holb
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """holb
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """holb
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logStreamHandler = logging.StreamHandler()
    logStreamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(logStreamHandler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """holb
    """

    dbName = os.environ.get("PERSONAL_DATA_DB_NAME")
    dbUserName = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    dbUserPassword = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    dbHost = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")

    dbConnector = mysql.connector.connect(user=dbUserName,
                                          password=dbUserPassword,
                                          host=dbHost,
                                          database=dbName)
    return dbConnector


def main():
    """holb
    """

    mySQLconnector = get_db()
    cursor = mySQLconnector.cursor()
    tableName = "users"
    query = ("SELECT * FROM %s")
    cursor.execute(query, tableName)

    sqlLogger = get_logger()

    retrievedData = []
    for row in cursor:
        inf = f"name={row[0]}; email={row[1]}; phone={row[2]}; " \
              f"ssn={row[3]}; password={row[4]}; ip={row[5]}; " \
              f"last_login={row[6]}; user_agent={row[7]};"
        retrievedData.append(inf)

    for data in retrievedData:
        sqlLogger.info(data)

    cursor.close()
    mySQLconnector.close()


if __name__ == "__main__":
    main()
