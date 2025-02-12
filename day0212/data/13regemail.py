import re

emails = "master@est.com  or  master@est.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

send = re.findall(pattern, emails)
print(send)  # ['master@est.com', 'master@est.org’]
