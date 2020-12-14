import os
import json
import pandas as pd
from chardet import detect


def get_encoding(file):
    """
    To get the encoding format of the file to read.
    :param file: The file to read.
    :return: The encoding of the file to read.
    """
    with open(file, 'rb+') as f:
        content = f.read()
        encoding = detect(content)['encoding']
    return encoding


class Reader:
    """
    To read certain cols from csv files.
    Basically exactly the same as pandas.
    --------
    TODO: Improving functions.
    """
    def __init__(self, root_path=None):
        """
        To obtain the root path of the files to be read.
        :param root_path: User specified root path or default from config.
        """
        if root_path:
            self.csvpath = root_path
        else:
            with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as json_file:
                config = json.load(json_file)
                self.csvpath = config['directory']
        if not os.path.exists(self.csvpath):
            raise ValueError('Path {} doesn\'t exit')

    def read_one(self, csv_name=None, tag=None):
        """
        To read one certain col from a csv file.
        :param csv_name: The csv to read.
        :param tag: The certain col to read.
        :return: The certain col from the csv file, format as DataFrame.
        """
        csv_path = os.path.join(self.csvpath, '{}.csv'.format(csv_name))
        data = pd.read_csv(csv_path, usecols=[tag], encoding=get_encoding(csv_path))
        return data

    def read_many(self, csv_name=None, tags=None):
        """
        To read certain cols from a csv file.
        :param csv_name: The csv to read.
        :param tags: The certain cols to read.
        :return: The certain cols from the csv file, format as DataFrame.
        """
        csv_path = os.path.join(self.csvpath, '{}.csv'.format(csv_name))
        data = pd.read_csv(csv_path, usecols=tags, encoding=get_encoding(csv_path))
        return data
