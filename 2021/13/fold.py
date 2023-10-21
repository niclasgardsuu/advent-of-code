with open("input.txt",'r') as f:
    data = f.read()
data = data.split('\n\n')
dotsdata  = data[0]
foldsdata = data[1]

dots = []
for dot in dotsdata.split('\n'):
    v = dot.split(',')
    dots.append([int(v[0]), int(v[1])])

folds = []
for fold in foldsdata.split('\n'):
    v = fold.split()[-1].split('=')
    folds.append([v[0], int(v[1])])
# folds = [folds[0]] # Part 1

for fold in folds:
    for dot in dots:
        if fold[0] == 'x':
            if dot[0] > fold[1]:
                dot[0] = fold[1] - abs(dot[0] - fold[1]) 
        elif fold[0] == 'y':
            if dot[1] > fold[1]:
                dot[1] = fold[1] - abs(dot[1] - fold[1]) 

paper_size = [0,0]
for dot in dots:
    if dot[0] > paper_size[0]:
        paper_size[0] = dot[0]
    if dot[1] > paper_size[1]:
        paper_size[1] = dot[1]

dot_count = 0
paper = [['.' for _ in range(paper_size[0]+1)] for _ in range(paper_size[1]+1)]
for dot in dots:
    if paper[dot[1]][dot[0]] == '.':
        paper[dot[1]][dot[0]] = '#'
        dot_count += 1

for p in paper:
    print(''.join(p))
print(dot_count, 'dots')