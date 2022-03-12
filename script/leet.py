import subprocess
from pathlib import Path

LOCAL = 'C'
DIR_LOCAL = 'Users/Sam/Desktop'
REMOTE = 'eecs.uci.edu'
DIR_REMOTE = 'users/ugrad/2020/winter/sabondoc/dev/leet'
SOLUTION = 'solution'

LANGUAGES = {
	'c': 'c/src',
	'py': 'py',
}

def transfer(sol: int, lang: str, server: str = 'zuma'):
	path_filename = Path('{0}.{1}'.format(SOLUTION, lang))
	path_dst = (
		Path('{0}:'.format(LOCAL))
		/ Path(DIR_LOCAL)
		/ path_filename
	)
	path_src =  (
		Path('sabondoc@{0}.{1}:'.format(server, REMOTE))
		/ Path(DIR_REMOTE)
		/ Path('{n:05d}'.format(n = sol))
		/ Path(LANGUAGES[lang])
		/ path_filename
	)
	subprocess.run(['scp', str(path_src), str(path_dst)], shell = True)
		
def main():
	sol = int(input("Solution: "))
	lang = str(input("Language: "))
	transfer(sol, lang);
			
if __name__ == "__main__":
	main()
