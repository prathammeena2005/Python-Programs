l=float(input('Enter length of box(in cm): '))
b=float(input('Enter width of box(in cm): '))
h=float(input('Enter height of box(in cm): '))
def volume_box(length=1,width=1,height=1):
    vol=length*width*height
    print("Volume=",vol,"cm^3")
volume_box(l,b,h)