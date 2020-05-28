class Triangle():
    def __init__(t):
        t.x1=0
        t.x2=0
        t.x3=0
        t.y1=0
        t.y2=0
        t.y3=0
    def read(t):
        t.x1=int(input('Enter x1 : '))
        t.y1=int(input('Enter y1 : '))
        t.x2=int(input('Enter x2 : '))
        t.y2=int(input('Enter y2 : '))
        t.x3=int(input('Enter x3 : '))
        t.y3=int(input('Enter y3 : '))
    def centroid(t):
        t.x=(t.x1+t.x2+t.x3)/3
        t.y=(t.y1+t.y2+t.y3)/3
        print(f'Centroind : ({t.x},{t.y})')
tri=Triangle()
tri.read()
tri.centroid()