

class FileManager:
    # File operations
    # 'r' Open a file for reading. (default)
    # 'w' Open a file for writing. Creates a new file if it does not exist or truncates the file if exist.
    # 'x' Open a file for exclusive creation. If the file already exists, the operation fails.
    # 'a' Open for appending at the end of the file without truncating it. Creates a new file if does not exist
    # 't' Open in text mode. (default)
    # 'b' Open in binary mode
    # '+' Open a file for updating (reading and writing)
    file = None

    def __init__(self, dir_path, filename, write_op, read_op, logger):
        logger.log.info("Init file content manager class")
        self.dir_path = dir_path.rstrip('/')
        self.filename = filename
        self.write_op = write_op
        self.read_op = read_op
        self.logger = logger

    def write_file(self, content):
        """
        Write contentn into file

        Args:
            message (str): Text to insert on file
        """
        # 2DO check if file already exist, if not empty check for overwite
        self.__open_file_for(self.write_op)
        self.logger.log.info(f'Writting the file \'{self.dir_path}/{self.filename}\'')
        self.file.write(content)
        self.__close_file()

    def read_file(self, position = None):
        """
        This function read all the file

        Args:
            position (int, optional): Set line position. Defaults to None.
        """
        self.__open_file_for(self.read_op)
        self.logger.log.info(f'Reading the file \'{self.dir_path}/{self.filename}\'')
        result = None
        if position:
            result = self.file.read(position)
        else:
            result = self.file.read()

        self.__close_file()
        return result

    def __open_file_for(self, operation):
        """
        Initialice the text file
        """
        self.logger.log.info(f'Opening the file \'{self.dir_path}/{self.filename}\'')
        self.file = open (f'{self.dir_path}/{self.filename}', operation, encoding="utf8")

    def __close_file(self):
        """
        Close opened file
        """
        self.logger.log.info(f'Clossing the file \'{self.dir_path}/{self.filename}\'')
        self.file.close()
