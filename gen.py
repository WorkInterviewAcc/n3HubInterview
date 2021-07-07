# Must guard against missing defaults by explaining how to use

import getopt
from datetime import datetime
from os import getcwd, path, mkdir
# The program must output a csv of n rows specified via the `rows` argument
# The header specified in the `column` option via the column_name must appear in the csv file.
from sys import argv, exit

help_info = ('To list help\n'
             '    -h --help\n'
             '    gen.py -h\n')

parameter_header = 'Parameter Information\n' \
                   '---------------------'

row_information = ('Rows (integer)\n'
                   '    Optional\n'
                   '    -r --rows\n'
                   '    gen.py -r 42 -c Id,integer\n')

output_information = ('Output Path (string)\n'
                      '    Optional\n'
                      '    -o --outPath\n'
                      '    gen.py -o c:\\temp -c Id,integer\n')

column_information = ('headers (string,type)\n'
                      '    Required, Allows Multiple\n'
                      '    type: integer, string\n'
                      '    -c --headers\n'
                      '    gen.py -r 42 -o c:\\temp -c Id,integer\n'
                      '    gen.py -c Id,integer\n'
                      '    gen.py -r 42 -o c:\\temp '
                      '-c Id,integer -c Name,string\n')


def print_all_messages():
    """Print all help information."""
    all_information = [
        help_info,
        parameter_header,
        row_information,
        output_information,
        column_information
    ]

    for information_pack in all_information:
        print(information_pack)


def exit_with_error(error_code, print_all_help=True):
    """Elegantly exit the application with a given error code.
    error_code: The error code to exit the application with.
    print_all_help: Print's all help information."""
    try:
        error_code_int = int(error_code)
    except ValueError:
        error_code_int = ""

    if print_all_help:
        print_all_messages()

    if not error_code_int:
        exit()
    else:
        exit(error_code_int)


def create_file_path(output_path):
    """Creates the file output path.
    output_path: The base path to append our file to.
    returns: The fully qualified file path we will write our csv to."""
    file_name = datetime.now().strftime("%Y-%m-%d-%H_%M_%S") + ".csv"
    if not path.exists(output_path):
        mkdir(path)
    return path.join(output_path, file_name)


def create_file(output_file_path, headers):
    """Creates the requested csv to the provided path.
    output_file_path: The path to output the csv file to.
    headers: The list of headers to write to the csv file."""
    with open(output_file_path, 'w') as f:
        print(f'Writing File to: "{output_file_path}"')
        f.write(", ".join(headers))


def main(request_args):
    # Get our default on
    print(request_args)
    rows = 50
    output_path = getcwd()
    column_provided = False
    headers = []

    try:
        # Read our arguments and read rows, outPath and column.
        options = getopt.getopt(
            request_args,
            "h:r:o:c:",
            ["rows", "outPath", "column"]
        )
    except getopt.GetoptError:
        exit_with_error(2)

    # Process our options.
    for opt, arg in options[0]:
        if opt in ("-h", "--help"):
            print_all_messages()
            exit()
        elif opt in ("-r", "--rows"):
            try:
                rows = int(arg)
            except ValueError:
                exit_with_error(2)
        elif opt in ("-o", "--outPath"):
            output_path = arg
        elif opt in ("-c", "--column"):
            # Validations
            assert "," in arg, \
                (f"Column argument '{arg}' does not have enough "
                 "data. You must specify a name and a type.\n"
                 "For additional help 'gen.py -h'.")
            column_info = arg.split(",")
            column_information_length = len(column_info)
            assert column_information_length == 2, \
                (f"Column information has more data than we expected. "
                 "Expected 2 but got {column_information_length}.\nPlease "
                 "check your column argument: '{arg}'")
            assert (column_info[1].lower() in ("string", "integer")), \
                (f"Column argument '{column_info[1]}' contains an invalid "
                 "type. Valid options include 'string', and 'integer'.")

            # Retrieve our column header.
            headers.append(column_info[0])
            if not column_provided:
                column_provided = True

    assert column_provided, \
        ("No column argument was provided. This is a required argument.\n"
         "{}".format(help_info))

    full_file_path = create_file_path(output_path)

    # Configuration
    config = ("rows: {}"
              "\noutput_path: {}"
              "\ncolumns:").format(rows, full_file_path)
    print(config)
    for header in headers:
        print("\t" + header)

    create_file(full_file_path, headers)


if __name__ == "__main__":
    main(argv[1:])
