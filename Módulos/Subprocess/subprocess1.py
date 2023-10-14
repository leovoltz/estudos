import subprocess
import sys

# sys.platform = linux, linux2. darwin, win32

cmd = ['ls -lah /']
encoding = 'utf-8'
system = sys.platform


if system == 'win32':
    cmd = ['dir']
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding, shell=True
)

print()

# print(proc.args)
# print(proc.stdout)
# print(proc.returncode)
print(proc.stdout)
