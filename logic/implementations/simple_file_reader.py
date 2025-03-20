from pathlib import Path

class SimpleFileReader():
    def __init__(self, d_path):
        d_path = Path(d_path)
        files: list[Path] = self.__get_files(d_path)
        self.file_dict = self.__start_dict(files)

    def get_document(self, filename) -> str:
        """
        Public method to get the text of a document from the file dictionary.
        Args:
            filename (str): The name of the file to read.
        Returns:
            str: The text of the document.
        """
        return self.file_dict[filename]

    def __get_files(self, d_path: Path) -> list:
        """
        Private method to get a list of files from a given directory path.
        Args:
            d_path (Path): The directory path from which to read files.
        Returns:
            list: A list of file paths within the given directory.
        """
        print(f"Reading documents from {d_path}:")

        files = []

        
        for path_child in d_path.iterdir():
            print(f"    - Found {path_child}")
            if path_child.is_file():
                files.append(path_child)

        if len(files) == 0:
            print("    No files found, maybe the path is wrong?")
            return []
        else:
            return files            
    
    
    def __start_dict(self, files: list[Path]) -> dict:
        """
        Private method to initialize a dictionary with file names as keys.
        Args:
            files (list): A list of file paths.
        Returns:
            dict: A dictionary with file names as keys and file paths as values.
        """
        file_dict = {}
        for file in files:
            text = open(file=file, mode='rt', encoding="utf-8").read()
            file_dict[file.name] = text

        return file_dict
            

if __name__ == "__main__":

    def test_simple_file_reader():
        reader = SimpleFileReader('C:/Users/gabriel.gomazako/Dev/GABRIEL/prompter/storage/documents/documents_tests')
        print(reader.get_document('reader_test.txt'))
        print(reader.get_document('reader_second_test.txt'))
        
    test_simple_file_reader()
