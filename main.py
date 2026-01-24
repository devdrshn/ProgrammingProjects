import sys
import os
import time
import winsound

os.system('cls')
def drawgrid(rows,cols,curxpos,curypos):
    grid=[]                         #Build a List of Lists
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append('.')
        grid.append(row)

    grid[curypos][curxpos]="#"      #Give the represntation for Robot

    print('\n')
    for row in grid:
        print("  ".join(row))       #Join Function joins components of a list
    print('\n'*3)


print("\nINSTRUCTIONS \n-The Top Most Left grid is assigned the coordinates (1,1)\n-The Directions must be given continuously, without any spaces.\n" )
nrows=int(input("Enter the no.of Rows of the Grid:"))
ncol=int(input("Enter the no.of Columns of the Gird:"))
currxpos= int(input("Enter the current X coordinate:"))
currypos= int(input("Enter the current Y Coordinate:"))
currxpos-=1                                #Because list indexing begins in (0,0)
currypos-=1


dirs= input("Enter the directions seperated by comma:")
dirlist=dirs.split(',')
currcor=[currxpos,currypos]

for j in dirlist:                                  #Access each direction individually

    os.system('cls')                               #Clears the console for Animation
    print(f'Next Direction is:{j}')                #Display the Next Direction
    drawgrid(nrows,ncol,currcor[0],currcor[1])     #Display the Current states
    winsound.Beep(2000,300)
    time.sleep(.5)                                 #Framerate

    i=j.strip().capitalize()
    if i=='Left':
        currcor[0]-=1
    elif i=='Right':
        currcor[0]+=1
    elif i=='Up':
        currcor[1]-=1
    else:
        currcor[1]+=1

    if (currcor[0]<0 or currcor[0]>=ncol or currcor[1]<0 or currcor[1]>=nrows):
        print("Oops! Robot bumped into a wall!")
        sys.exit()                                #Stops the program altogether

os.system('cls')                                  #if OS is Mac,change cls to clear
drawgrid(nrows,ncol,currcor[0],currcor[1])
winsound.Beep(1000,800)

newcor=[x+1 for x in currcor]                     #Implement List comprehension
print("The New co-ordinates of the Robot is:",newcor)