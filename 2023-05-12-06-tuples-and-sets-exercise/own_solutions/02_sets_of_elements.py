n, m = (map(int, input().split()))
# print(n, m)

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

print(*(n_set & m_set), sep="\n")
