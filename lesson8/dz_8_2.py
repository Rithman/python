import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        RE_REMOTE_ADDR = re.compile(r"^((\d+\.){3}\d+)|([(a-z0-9)]{3,4}:){5,7}[(a-z0-9)]{3,4}|"
                                    r"([(a-z0-9)]{3,4}:){2,3}:([(a-z0-9)]{3,4}:){3,4}([(a-z0-9)]{3,4})|"
                                    r"([(a-z0-9)]{3,4}:){2,4}:[(a-z0-9)]{1,4}")
        remote_addr = RE_REMOTE_ADDR.search(line)
        RE_REQUEST_DATETIME = re.compile(r"(\[([^\[]+)\])")
        request_datetime = RE_REQUEST_DATETIME.search(line)
        RE_REQUEST_TYPE = re.compile(r'(GET|HEAD)')
        request_type = RE_REQUEST_TYPE.search(line)
        RE_REQUESTED_SOURCE = re.compile(r"\/downloads/product_\d")
        requested_source = RE_REQUESTED_SOURCE.search(line)
        RE_RESPONSE_CODE_SIZE = re.compile(r'\s\d{3}')
        response_code = RE_RESPONSE_CODE_SIZE.search(line)
        RE_RESPONSE_SIZE = re.compile(r'(?<=\s\d{3}\s)\d{1,8}')
        response_size = RE_RESPONSE_SIZE.search(line)

        with open('result.txt', 'a', encoding='utf-8') as f:
            print(remote_addr.group(0), request_datetime.group(0), request_type.group(0), requested_source.group(0),
              response_code.group(0), response_size.group(0), sep=', ', file=f)

