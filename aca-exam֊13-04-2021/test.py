from resourcereader import ResourceReader

# res = ResourceReader('reddit-rss-en.txt')
# print(res.read())
#
# res.close()

res = ResourceReader('https://aca.am/hy')
print(res.read())

res.close()

# res = ResourceReader('http://non-existing-location')
