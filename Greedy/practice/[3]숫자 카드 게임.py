N, M = map(int, input().split())
list = []

max_candidates = []
for i in range(N) :
    tmp_list = map(int, input().split())
    max_candidates.append(min(tmp_list))

print(max(max_candidates))