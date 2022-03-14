"""
leet.py
----------------------------------------------------------------
Send solution code to local desktop from remote Linux workspace
for copy/paste to LeetCode via local browser.

"""

import subprocess
from pathlib import Path

LOCAL = 'C'
DIR_LOCAL = 'Users/Sam/Desktop'
DIR_REMOTE = 'dev/leet'
SOLUTION = 'solution'

LANGUAGES = {
	'c': 'c/src',
	'py': 'py',
}

HOME = {
	'pi': 'home/pi',
	'sabondoc': 'users/ugrad/2020/winter/sabondoc',
}

def transfer(remote: str, sol: int, lang: str):
	path_filename = Path('{0}.{1}'.format(SOLUTION, lang))
	path_dst = (
		Path('{0}:'.format(LOCAL))
		/ Path(DIR_LOCAL)
		/ path_filename
	)
	path_src =  (
		Path('{0}:'.format(remote))
		/ Path(HOME[remote.split('@')[0]])
		/ Path(DIR_REMOTE)
		/ Path('{n:05d}'.format(n = sol))
		/ Path(LANGUAGES[lang])
		/ path_filename
	)
	subprocess.run(['scp', str(path_src), str(path_dst)], shell = True)

def main():
	remote = str(input("Remote: "))
	sol = int(input("Solution: "))
	lang = str(input("Language: "))
	transfer(remote, sol, lang);
			
if __name__ == "__main__":
	main()
