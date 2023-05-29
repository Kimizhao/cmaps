# 读取wind.json文件，并打印出来，给出代码示例
import json
import os
import re

# https://tooltt.com/js-object-to-json/

# 打开wind.json文件
with open('wind.json', 'r') as f:
    # 读取文件内容json
    data = json.load(f)

    s = 'GEOAI color table'
    file = open("G.rgb", "w", encoding="utf-8")
    file.write('# GEOAI color table\r')
    file.write('# number of colors in table\r')
    file.write('ncolors = 18\r')
    file.write('\r')
    file.write('# r g b\r')

    # 打印json内容
    for i in data['items']:
        hex_color = i['color']
        rgb_color = tuple(int(re.findall(r'\w\w', hex_color)[i], 16) for i in (0, 1, 2))

        print(rgb_color[0])
        rgb_line = f'{rgb_color[0]} {rgb_color[1]} {rgb_color[2]}\r'
        file.write(rgb_line)

    file.close()
