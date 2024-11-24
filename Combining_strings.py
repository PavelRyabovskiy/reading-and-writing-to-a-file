import os

def combine_files(file_list, output_file):
    file_info = []

    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((file, line_count, lines))

    file_info.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_name, count, lines in file_info:
            out_f.write(f"{file_name}\n{count}\n")
            out_f.writelines(lines)

input_files = ['1.txt', '2.txt','3.txt']
output_file = 'result.txt'
combine_files(input_files, output_file)