#!/usr/bin/env python3
"""holb
"""

from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ holb
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """holb
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """holb
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """hob
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """holb
    """
    for field in fields:
        message = re.sub('{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message


def get_db() -> mysql.connector.connection.MySQLConnection:
    """holb
    """
    db_user = os.environ.get('PERSONAL_DATA_DB_USERNAME', None)
    db_pw = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST', None)
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME', None)

    return mysql.connector.connect(user=db_user,
                                   password=db_pw,
                                   host=db_host,
                                   database=db_name)


def main():
    pass

if __name__ == "__main__":
    main()
