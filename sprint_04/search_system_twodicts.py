n = int(input())

hash_docs_id = {}
hash_docs_cnt = {}
for i in range(n):
    word_cnt = {}
    for word in input().split():
        hs = hash(word)
        # print("WORD", word, hs)
        if hs in word_cnt:
            word_cnt[hs] += 1
        else:
            word_cnt[hs] = 1
    
    for hs, num in word_cnt.items():
        if hs in hash_docs_id:
            hash_docs_id[hs].append(i)
            hash_docs_cnt[hs].append(num)
        else:
            hash_docs_id[hs] = [i]
            hash_docs_cnt[hs] = [num]

        # if hs not in hash_docs_id:
        #     hash_docs_id[hs] = [i]
        #     hash_docs_cnt[hs] = [1]
        # elif i in hash_docs_id[hs]:
        #     ind = hash_docs_id[hs].index(i)
        #     hash_docs_cnt[hs][ind] += 1
        # else:
        #     hash_docs_id[hs].append(i)
        #     hash_docs_cnt[hs].append(1)

# print("DOC HASH")
# print(hash_docs_id)
# print(hash_docs_cnt)

m = int(input())
for i in range(m):
    # print("Query: ", i)
    rel = {}
    query_unique = set()
    for word in input().split():
        hs = hash(word)
        if hs in query_unique:
            continue
        # print("word", word, hs)
        if hs in hash_docs_id:
            for j in range(len(hash_docs_id[hs])):
                doc_id, cnt = hash_docs_id[hs][j], hash_docs_cnt[hs][j]
                if doc_id not in rel:
                    rel[doc_id] = cnt
                else:
                    rel[doc_id] += cnt
        # print("Relevance after", rel)

        query_unique.add(hs)

    cnts = []
    for it in sorted(rel.items(), key=lambda x: (x[1], -x[0]), reverse=True)[:5]:
        if it[1] == 0:
            break
        cnts.append(it[0] + 1)
    print(*cnts)

