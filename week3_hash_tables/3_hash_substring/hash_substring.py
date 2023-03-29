# python3
class RabinKarpAlgorithm:
    def __init__(self, pattern: str, text: str):
        self.pattern = pattern
        self.text = text
        self.pattern_len = len(pattern)
        self.text_len = len(text)
        self.hash_pattern = self.hash_func(pattern)

    def hash_func(self, str_val: str) -> int:
        return sum(ord(char_val) for char_val in str_val)

    def search(self) -> list:
        pattern_hash = self.hash_pattern
        start, end = 0, self.pattern_len
        curr_substring_hash = self.hash_func(self.text[start:end])
        indices = []

        if pattern_hash == curr_substring_hash and self.text[:self.pattern_len] == self.pattern:
            indices.append(0)
        for i in range(1, self.text_len - self.pattern_len +1):
            curr_substring_hash = curr_substring_hash - ord(self.text[i-1]) + ord(self.text[i+self.pattern_len-1])

            if pattern_hash == curr_substring_hash and self.text[i:i+self.pattern_len] == self.pattern:
                indices.append(i)
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

