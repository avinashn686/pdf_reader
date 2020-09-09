import sys
import json
import pdfplumber
inputs = sys.argv[1]
output = sys.argv[2]
data = {}
levels = {}
content_list = []
lines = 1
pdf = pdfplumber.open(inputs)
page = pdf.pages[0]
text = page.extract_text()
content_level = text.split('\n')
content_level = [data.strip() for data in content_level if data.strip()]
for content in content_level:
    if '____' in content:
        lines += 1
        content_list = []
    else:
        level = 'level' + str(lines)
        content_list.append(content)
        levels[level] = content_list
for key, value in levels.items():
    if key == 'level1':
        data['name'] = levels['level1'][0]
        address_ = levels['level1'][1]
        address_ = address_.split('|')
        address_ = [x.strip() for x in address_ if x.strip()]
        address = address_[0] + ',' + levels['level1'][2]
        data['address'] = address
        email = address_[-1]
        data['email'] = email
        next_key = levels['level1'][-1]
    else:
        temp = value[-1]
        del value[-1]
        data[next_key] = ' '.join(value)
        next_key = temp
data = {key: ' '.join(value.split()) for key, value in data.items()}
data = {key: value.replace('\u200b,', '') for key, value in data.items()}
with open(output, "w") as outfile:
    json.dump(data, outfile)
