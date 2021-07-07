import os
from csv import reader
from os import getcwd, listdir
from re import match


class FileManager:
    """Class to handle reading files."""

    def create_file(self):
        # call gen.py
        print('create_file')

    def get_files(self):
        """Load stored files names into memory."""
        # Search source_path for files.
        file_format = r'\d{4}(-\d{2}){3}(_\d{2}){2}.csv'
        self.files = [f for f in listdir(self.source_path) if match(file_format, f)]
        return self.files

    def get_file_path(self, file_name):
        """"Generates a full file path from a file name."""
        if self.find_file(file_name):
            full_file_path = os.path.join(self.source_path, file_name)
            return full_file_path
        else:
            print(f'Found nothing with filename: {file_name}.')

        return ''

    def find_file(self, file_name):
        """Given a file name, determines if the file
        exists in its data directory."""
        if len(self.files) == 0:
            self.get_files()

        found = False
        for f in self.files:
            if f == file_name:
                found = True
                break

        return found

    def get_content(self, file_name):
        """Gets the content from a file as a list of strings."""
        full_file_path = self.get_file_path(file_name)

        # rows = []
        rows = ""
        with open(full_file_path) as csv_file:
            print(f'Opening {full_file_path}... ')
            csv_reader = reader(csv_file)
            for row in csv_reader:
                full_row = ', '.join(row)
                rows += full_row + os.linesep
        return rows

    def __init__(self, base_folder=os.path.join(os.path.dirname(__file__),
                                                'data')):
        self.source_path = base_folder
        self.files = self.get_files()
