"""
https://contest.yandex.ru/contest/24414/run-report/69485007/

----------------------------- Idea ----------------------------

The hash table for the documents has the following format:
    KEY = hash of the word
    VALUE = list of the format [document_id, word_count]

------------------------ Time Complexity ----------------------

Assume that N is the number of words in the documents and M is
the number of words in the queries, and W is the average word
length.

* Constructing the hash table for the documents' words: O(N * W),
  we need W operations to loop over all word symbols for constructing
  hash.

For each query:
    * For each word from the query ( O(M) )
        * Find corresponding documents in the hash table ( O(W), where W
        is the average word length)

        * Loop over all documents ( O(1) on average )

    * Perform sorting for the all documents: K * log(K), where K is the
    stored counter results. K << N, can be skipped.

Total: O(N * W) + O(M * W)

------------------------ Space Complexity ----------------------

O(N) for storing pointers to the lists.
O(2 * N) for N elements itself (for document id and word count). 

Total: O(N)

"""
n = int(input())

# Step 1. Construct hash table
hash_docs = {}
for i in range(n):
    word_cnt = {}
    for word in input().split():
        hs = hash(word)
        word_cnt[hs] = word_cnt.get(hs, 0) + 1
    
    for hs, num in word_cnt.items():
        doc_list = hash_docs.get(hs)
        if doc_list is not None:
            doc_list.append([i, num])
        else:
            hash_docs[hs] = [[i, num]]

# Step 2. Find relevant documents for each query.
m = int(input())
for i in range(m):
    rel = {}
    for word in set(input().split()):
        hs = hash(word)
        doc_list = hash_docs.get(hs)
        if doc_list is not None:
            for j in range(len(doc_list)):
                doc_id, cnt = doc_list[j]
                if doc_id not in rel:
                    rel[doc_id] = cnt
                else:
                    rel[doc_id] += cnt

    cnts = []
    for it in sorted(rel.items(), key=lambda x: (-x[1], x[0]))[:5]:
        if it[1] == 0:
            break
        cnts.append(it[0] + 1)
    print(*cnts)

