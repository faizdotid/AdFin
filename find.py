import requests
import threading
import os 

def check_file():
	if os.path.isfile('panels.txt'):
		pass
	else:
		with open('panels.txt', 'w+') as f:
			f.write(requests.get('https://raw.githubusercontent.com/faizgans14/AdFin/main/panels.txt').text)
			f.close()

def find(urls):
	try:
		req = requests.get(urls, headers={}, timeout=14)
		req.raise_for_status()
		print('\n\n\033[0;32m[√] Admin Login Found : '+urls+'\033[0m\n')
		open('found.txt', 'a').write(urls+'\n')
	except requests.RequestException:
		print('\033[0;31m[x] Not Found : '+urls, end='\r'*2+'\033[0m')

def fetch(url):
	check_file()
	paths = open('panels.txt', mode='r').read().splitlines()
	while not len(paths) == 0:
		path = paths.pop()
		urls = url+path
		find(urls)

def Main():
	print("""
{}     _       _ _____ _       \n    / \   __| |  ___(_)_ __  \n   / _ \ / _` | |_  | | '_ \ \n  / ___ \ (_| |  _| | | | | |\n /_/   \_\__,_|_|   |_|_| |_|\n\n {}Simple Admin Page Login Finder{}
""".format('\033[0;32m', '\033[0;36m', '\033[0m'))
	target = input('Target : ')
	if '://' in target:target = target
	else:target = 'http://'+target
	t1 = threading.Thread(target=fetch, args=(target,))
	t1.start()
	t1.join()
	print('\n\n[!] Scanning Finished ')


Main()
