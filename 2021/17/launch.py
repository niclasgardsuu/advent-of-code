data,vel = [int(v) for v in open('input.txt','r').read().replace('target area: x=','').replace(', y=',' ').replace('..',' ').split()],[]
for xv,yv in __import__('itertools').product(range(500),range(-200,200)):
        init_yv,init_xv,x,y=yv,xv,0,0
        while x <= data[1] and y >= data[2]: x,y,yv,xv,vel = x+xv, y+yv, yv-1, (xv,xv-1)[xv!=0], (vel,vel+[(init_xv,init_yv)])[x >= data[0] and x <= data[1] and y >= data[2] and y <= data[3]]
print(sum(range(max(vel,key=lambda x: x[1])[1]+1)),'\n',len(set(vel)),sep='')