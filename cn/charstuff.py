#18501A0581
n = int(input('enter no.of frames:'))
frames = ['' for i in range(n)]
frameLens = []
i = 0
while i<n:
    frames[i] = input('enter frame{}:'.format(i+1))
    if len(frames[i])&7 != 0:
        print('!! size of frame should be x8')
        i -= 1
    i += 1

dle = input('enter dle:')
stx = input('enter stx:')
etx = input('enter etx:')

print('final frame\n', end='')
for frame in frames:
    print('{}{}'.format(dle, stx), end='')
    for i in range(0, len(frame), 8):
        character = frame[i:i+8]
        print('{}'.format(character), end='')
        if character==dle:
            print('{}'.format(dle), end='')
    print('{}{}'.format(dle, etx), end='')