n = int(input())
box = set(input() for _ in range(n))
box = sorted(box)
box = sorted(box, key=lambda x : len(x))

print('\n'.join(box))
