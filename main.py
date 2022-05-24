from bs4 import BeautifulSoup 
from lxml import etree
import re
import hashlib

#le arquivo xml
tree = etree.parse('teste.xml')
#remove tags xml
notags = etree.tostring(tree, encoding='utf8', method='text')
notags = notags.decode('utf8')

#remove espaços e quebras de linha
notags = re.sub('\s+', '', notags)
print(notags)
#remove hash
nohash = notags[:-32]
#gera hash md5 da string nohash
hash = hashlib.md5()
hash.update(nohash.encode('ISO-8859-1'))
hash = hash.hexdigest()

print(hash)


  
