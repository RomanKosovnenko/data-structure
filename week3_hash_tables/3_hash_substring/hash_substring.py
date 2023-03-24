# python3
class RabinKarpAlgorithm:
    def __init__(self, pattern: str, text: str):
        self.pattern = pattern
        self.text = text
        self.hash_pattern = self.hash_func(pattern)
        self.M = len(pattern)

    def hash_func(self, str_val: str) -> int:
        prime = 257
        hash_val = sum(ord(char_val) for char_val in str_val)
        return hash_val % prime

    def search(self) -> list:
        N = len(self.text)
        pattern_hash = self.hash_pattern
        start, end = 0, self.M
        curr_substring_hash = self.hash_func(self.text[start:end])
        indices = []

        while end <= N:
            if (pattern_hash == curr_substring_hash and 
                self.pattern == self.text[start:end]):
                indices.append(start)
            if end == N:
                break
            curr_substring_hash -= ord(self.text[start])
            curr_substring_hash += ord(self.text[end])
            start += 1
            end += 1
        return indices

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    rabin_karp = RabinKarpAlgorithm(pattern=pattern, text=text)
    return rabin_karp.search()

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

