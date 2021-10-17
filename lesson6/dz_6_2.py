from requests import get, utils
from collections import Counter

src = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(src.headers)
content = src.content.decode(encoding=encodings)
src_par = content.splitlines()

result = []
spammer_list = []
for line in src_par[:]:
    remote_addr, request_type, requested_resource = line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]
    result_tuple = (remote_addr, request_type, requested_resource)
    result.append(result_tuple)
    spammer_list.append(remote_addr)

print(result)
print(f'The Spammer is {Counter(spammer_list).most_common(1)}')

# src_par[:] - взял срез, т.к. изначльно скрипт упирался в какую-то границу в 51k+ строк и писал
# list index out of range. На следующий день чудесным образом заработало, но срез на всякий случай оставил.
