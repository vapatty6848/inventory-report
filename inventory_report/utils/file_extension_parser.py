def get_file_extension(file_path):
    file_pieces = file_path.split('.')
    file_pieces.reverse()

    file_extension = file_pieces[0]

    return file_extension
