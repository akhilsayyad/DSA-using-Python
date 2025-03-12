# n=5
# for i in range(n):
#     print(" " * (n-i-1) + "*" * (2*i+1))
# for j in range(n,0,-1):
#     print("*" * (n-1) + " " * (2*j+1))



# number=5
# for i in range(1,number+1):
#     for j in range(i):
#         print(i,end=' ')
#     print(' ')

# num=5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print(' ')


# num=6
# for i in range(1,num+1):
#     for j in range(i):
#         print(i,end=' ')
#     print(' ')
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=' ')
#     print()

# num=5
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(n-i+1,end=' ')
#     print()

n=5
for i in range(1,n+1):
    for j in range(n-1,-1):
        print(" ",end=' ')
    for k in range(i):
        print(k,end=' ')
    print()