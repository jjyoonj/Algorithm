N = int(input())
channels = []
commands = []
pointer = 0

for _ in range(N):
    channels.append(input())

idx_kbs1 = channels.index('KBS1')

for _ in range(idx_kbs1):
    commands.append('1')
    pointer += 1
    
for _ in range(idx_kbs1):
    commands.append('4')
    channels[pointer], channels[pointer-1] = channels[pointer-1], channels[pointer]
    pointer -= 1
    
idx_kbs2 = channels.index('KBS2')

for _ in range(idx_kbs2):
    commands.append('1')
    pointer += 1
    
for _ in range(idx_kbs2-1):
    commands.append('4')
    channels[pointer], channels[pointer-1] = channels[pointer-1], channels[pointer]
    pointer -= 1
    
print(''.join(commands))