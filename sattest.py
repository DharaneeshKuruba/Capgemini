#1

# C=int(input("enter the capacity of ship: "))
# N=int(input("enter the number of people: "))
# if N % C == 0:
#     rounds = N // C
# else:
#     rounds = (N // C) + 1
# print(rounds)


#2

# n=int(input("enter the number of seats in row: "))
# arr=list(map(int,input("enter 0 or 1: ").split()))
# count=0
# for a in arr:
#     if a==0:
#         count+=1
#     else:
#         continue
# print(count)


#3

# n=int(input("enter the number of kilometers: "))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=i
#     else:
#         continue
# print(sum)


#4

# N=int(input("enter the number of filled rooms: "))
# rooms=list(map(int,input("enter the rooms reserved: ").split()))
# T=int(input("enter total number of rooms: "))
# print(T-N)


#5

# arr=list(map(int,input("enter the baked items: ").split()))
# prod=1
# for a in arr:
#     if a%7==0:
#         prod*=a
#     else:
#         continue
# print(prod)


#6

# N=int(input("enter max's age: "))
# print(N*7)


#7

# s=input("enter a string: ").lower()
# def magic_steps(s):
#     freq = {}
#     i = 0
#     while i < len(s):
#         ch = s[i]
#         if ch in freq:
#             freq[ch] = freq[ch] + 1
#         else:
#             freq[ch] = 1
#         i += 1
#     max_count = 0
#     for ch in freq:
#         if freq[ch] > max_count:
#             max_count = freq[ch]
#     return len(s) - max_count
# print(magic_steps(s))


#8

# h=int(input())
# v=int(input())
# vn=int(input())
# print(h*((v/vn)**2))


#9

# s1=input("enter s1: ")
# s2=input("enter s2: ")
# def ascii_sum_longest_common_substring(s1, s2):
#     max_len = 0
#     max_sum = 0
#     i = 0
#     while i < len(s1):
#         j = 0
#         while j < len(s2):
#             k = 0
#             curr_sum = 0
#             while (i + k < len(s1) and
#                    j + k < len(s2) and
#                    s1[i + k] == s2[j + k]):
#                 curr_sum += ord(s1[i + k])
#                 k += 1
#             if k > max_len:
#                 max_len = k
#                 max_sum = curr_sum
#             j += 1
#         i += 1
#     return max_sum
# print(ascii_sum_longest_common_substring(s1,s2))


#10

# n=int(input("enter total problems: "))
# p=int(input("enter time: "))
# rem_time=240-p
# total_time=0
# count=0
# for i in range(1,n+1):
#     if total_time + 5*i <= rem_time:
#         total_time += 5*i
#         count += 1
#     else:
#         break
# print(count)


#11

# def winning_party(votes):
#     n = len(votes)
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if votes[j] == votes[i]:
#                 count += 1
#         if count * 2 >= n:
#             return votes[i]
#     return -1
# votes=list(map(int,input("enter votes: ").split()))
# print(winning_party(votes))


#12

# def min_possible_sum(arr):
#     max_val = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > max_val:
#             max_val = arr[i]
#     return max_val
# arr=list(map(int,input("enter array: ").split()))
# print(min_possible_sum(arr))


#13

# def team_initials(names):
#     res = ""
#     for name in names:
#         res += name[0].upper()
#     return res
# names=list(map(str,input("enter names: ").split()))
# print(team_initials(names))


#14

# def latest_file_version(files):
#     max_ver = -1
#     for f in files:
#         if len(f) >= 6 and f[0:5] == "File_":
#             num = 0
#             valid = True
#             for i in range(5, len(f)):
#                 if f[i] < '0' or f[i] > '9':
#                     valid = False
#                     break
#                 num = num * 10 + (ord(f[i]) - 48)
#             if valid and num > max_ver:
#                 max_ver = num
#     return max_ver
# files=list(map(str,input("enter files: ").split()))
# print(latest_file_version(files))


#15

# def winning_move(move):
#     if move == "rock":
#         return "Paper"
#     if move == "paper":
#         return "Scissors"
#     if move == "scissors":
#         return "Rock"
# move=input("enter the player A move: ")
# print(winning_move(move))
