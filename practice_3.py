#Rudimentary logic of pattern printing
# for i in range(5):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

#Improved logic for pattern printing
n = 5
# for i in range(1, 2*n):
#     star = i if i<=n else 2*n-i
#     print("*"*star)

# #Mirror pattern
# for i in range(1, 2*n):
#     star = i if i<=n else 2*n-i
#     spaces = n - star
#     print(" " * spaces + "*" * star)

#Butterfly pattern
for i in range(1, 2*n):
    star = i if i<=n else 2*n-i
    spaces = 2 * (n - star) + 1
    print("*" * star + " " * spaces + "*" * star)