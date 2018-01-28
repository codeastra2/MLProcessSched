from subprocess import Popen, PIPE
import os

PROGRAMS = os.getcwd()+ '/programs/'
EXE = os.getcwd() + '/exe/'

if not os.path.exists(EXE):
	os.makedirs(EXE)

for file in os.listdir(PROGRAMS):
	command = 'gcc %s -o %s%s' % (file, EXE, file.split('.')[0])
	Popen(command, shell=True, stdout=PIPE, cwd = PROGRAMS).stdout
