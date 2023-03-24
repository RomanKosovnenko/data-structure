# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def add(self, index, value):
        if value not in self.elems[index]:
            self.elems[index].insert(0, value)

    def delete(self, index, value):
        for i, pair in enumerate(self.elems[index]):
            if pair == value:
                del self.elems[index][i]
                return

    def find(self, index, value):
        for key in self.elems[index]:
            if key == value:
                self.write_search_result(True)
                return
        self.write_search_result(False)

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
            return

        index = self._hash_func(query.s)
        if query.type == 'find':
                self.find(index, query.s)
        elif query.type == 'add':
            self.add(index, query.s)
        else:
            self.delete(index, query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
