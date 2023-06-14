# 读取txt文件，并打印出来，然后转换成rgb文件
import re

# 打开wind.txt文件
with open('humidity.txt', 'r') as f:
    # 读取文件的第一行内容
    ct = f.readline().strip()

    # 打印第一行内容
    print(ct)

    lines = f.readlines()

    s = 'GEOAI color table'
    file_name = f'G_{ct}.rgb'
    file = open(file_name, "w", encoding="utf-8")
    file.write(f'# GEOAI color table - {ct}\r')
    file.write('# number of colors in table\r')
    file.write(f'ncolors = {len(lines)+1}\r')
    file.write('\r')
    file.write('# r g b\r')

    # 逐行读取文件内容
    for line in lines:
        hex_color = f'#{line.strip()}'
        rgb_color = tuple(int(re.findall(r'\w\w', hex_color)[i], 16) for i in (0, 1, 2))
        print(rgb_color[0])
        rgb_line = f'{rgb_color[0]} {rgb_color[1]} {rgb_color[2]}\r'
        file.write(rgb_line)

    file.close()