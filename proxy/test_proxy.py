import urllib2

proxy_server = "62.201.200.17"

proxy_support = urllib2.ProxyHandler({"http": proxy_server})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)


url = "http://example.com/figs/cat.jpg?from=" + proxy_server

image = urllib2.urlopen(url)

output = open('cat_' + proxy_server + '.jpg', 'wb')
output.write(image.read())
output.close()
