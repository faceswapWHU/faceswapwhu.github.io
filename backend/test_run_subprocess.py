import subprocess
import os


os.chdir('facefusion')
run_command = ['python', 'run.py', '-s', 'source.png', '-t', 'target.png', '-o', 'output', '--headless']
with subprocess.Popen(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stdout:
        print(line, end='')

    for line in proc.stderr:
        print(line, end='')

proc.wait()
os.chdir('../..')
