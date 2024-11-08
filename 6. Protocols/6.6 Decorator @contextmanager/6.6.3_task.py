from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    file_backup = open('backup.txt', 'w')
    try:   
        yield file_backup
        file_backup.close()
        with open('backup.txt', 'r') as file1, open(filename, 'w') as file2:
            for line in file1:
                file2.write(line)
    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {type(error).__name__}')