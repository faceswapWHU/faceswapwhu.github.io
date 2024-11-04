import subprocess
import os

os.chdir('facefusion')
mv_command = 'mv output/* output.png'
# use shell to ensure that the wildcard is expanded correctly
with subprocess.Popen(mv_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True) as proc:
    for line in proc.stdout:
        print(line, end='')

    for line in proc.stderr:
        print(line, end='')

proc.wait()

os.chdir('../..')
