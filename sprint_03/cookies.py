n_children = int(input())
children = list(map(int, input().split()))
n_cookies = int(input())
cookies = list(map(int, input().split()))

children.sort()
cookies.sort()

n_eaten = 0
i_cookie = 0
for i in range(n_children):
    while i_cookie < n_cookies and cookies[i_cookie] < children[i]:
        i_cookie += 1

    if i_cookie == n_cookies:
        break

    n_eaten += 1
    i_cookie += 1


print(n_eaten)
