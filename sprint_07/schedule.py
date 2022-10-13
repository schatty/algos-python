n = int(input())

lessons = []
for _ in range(n):
    t1, t2 = input().split() #map(float, input().split())
    lessons.append((t1, t2))

lessons.sort(key = lambda x: (float(x[1]), float(x[0])))
# print("Sorted: ", lessons)

cur_lesson = lessons[0]
lessons_picked = [cur_lesson]
for i in range(1, n):
    if float(lessons[i][0]) < float(cur_lesson[1]):
        continue
    cur_lesson = lessons[i]
    lessons_picked.append(cur_lesson)

print(len(lessons_picked))
for lesson in lessons_picked:
    print(*lesson)
