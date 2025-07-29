from email.contentmanager import raw_data_manager
#
# Rows = int(input("Enter number of rows:"))
# for i in range(1, Rows+1):
#         for space in range(1, Rows-i+1):
#                 print(end =" ")
#         for star in range(1,i+1):
#                 print("*",end=' ')
#         print(' ')


# #################################
#
# Row1 = int(input("Enter number of rows:"))
# for i in range(1,Row1+1):
#         for star in range (1, i+1):
#           print("*", end=" ")
#         print(" ")

################################

# Row2=int(input("Enter Number of Rows:"))
#
# for i in range (1, Row2+1):
#         for space in range (1,Row2-i+1):
#                 print(" ", end=' ')
#
#         for star in range(1, i+1):
#                 print("*",end=' ')
#         print(' ')

# Row3=int(input("Enter number of Rows:"))
# for i in range (1, Row3+1):
#         for star in range (1,Row3+1):
#                 print("*", end=' ')
#         print(" ")
#
# Row4=int(input("Enter number of Rows:"))
# for i in range (1, Row4+1):
#         for space in range (1, Row4-i+1):
#                 print(end= ' ')
#
#         for star in range (1,i+1):
#                 print("*", end=' ')
#         print(' ')
#
#         for star1 in range(Row4, Row4+1):
#                 print("*")

rows=int(input("Enter number of rows:"))

for i in range(rows):
        for space in range (1,rows-i+1):
                print(end=' ')
        for star in range(1, i+1):
                print("*",end=' ')
        print(" ")

        for j in range (rows-1,0,-1):
                print(" "*(rows-j)+"*"*(j))





