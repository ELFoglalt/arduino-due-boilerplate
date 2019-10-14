import subprocess
import sys

if len(sys.argv) < 2:
    sys.exit(1)

result = subprocess.run(['arduino-cli', 'board', 'list'], stdout=subprocess.PIPE)
output_str = result.stdout.decode("utf-8")
output_lines = output_str.rstrip().split('\n')

for line in output_lines[1:]:
    if line.find(sys.argv[1]):
        print(line.split()[0])
        sys.exit(0)

sys.exit(2)
