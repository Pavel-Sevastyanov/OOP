def print_file_content(filename):
    try:
        with open(filename, 'rt', encoding='utf-8') as file:
            print(file.read())
    except:
        print('Файл не найден')
