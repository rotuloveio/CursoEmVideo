# Teste se o site pudim.com.br está acessível pelo PC
import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except:
	print('ERRO')
else:
	print('OK')
	print(str(site.read()).replace('\\n', '\n'))
