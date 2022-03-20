"""
leet.py
----------------------------------------------------------------
Send solution code to local desktop from remote Linux workspace
for copy/paste to LeetCode via local browser.

"""

import argparse
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

parser = argparse.ArgumentParser(description = "SCP LeetCode submission.")
parser.add_argument('--port', help = "Optional port number.")

def transfer(remote: str, port: str, sol: int, lang: str):
	path_filename = Path('{0}.{1}'.format(SOLUTION, lang))
	path_dst = (
		Path('{0}:/'.format(LOCAL))
		/ Path(DIR_LOCAL)
		/ path_filename
	)
	usr = remote.split('@')[0]
	path_src = (
		Path('{0}:'.format(remote))
		/ Path(HOME[usr])
		/ Path(DIR_REMOTE)
		/ Path('{n:05d}'.format(n = sol))
		/ Path(LANGUAGES[lang])
		/ path_filename
	)
	opt = ""
	if (port != None):
		opt = "-P {0} ".format(port)
	cmd = "scp {0}{1} {2}".format(opt, str(path_src), str(path_dst))
	print(cmd)
	subprocess.run(cmd)

def setup_parser() -> argparse.ArgumentParser:
	ret = argparse.ArgumentParser(description = "SCP LeetCode submission from remote to local.")
	ret.add_argument(
		'--remote',
		'-r',
		type = str,
		required = True,
		help = "Remote server source (e.g. \"sabondoc@zuma.eecs.uci.edu\")."
	)
	ret.add_argument(
		'--solution',
		'-s',
		required = True,
		type = int,
		help = "Solution number (e.g. \"69\")."
	)
	ret.add_argument(
		'--language',
		'-l',
		required = True,
		type = str,
		help = "Language (e.g. \"c\")."
	)
	ret.add_argument(
		'--port',
		'-p',
		required = False,
		type = int,
		help = "Port number for port forwarding (e.g. \"22\")."
	)
	return ret

def main(args: argparse.Namespace = setup_parser().parse_args()):
	transfer(args.remote, args.port, args.solution, args.language);
			
if __name__ == "__main__":
	main()
