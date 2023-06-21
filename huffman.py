import heapq
import operator

f = open("/Users/zeyadhassan/Desktop/textfile.txt", "r")
data = f.read()


class node:
    def __init__(self, char, letters_freq, left=None, right=None):
        self.letters_freq = letters_freq
        self.char = char
        self.right = right
        self.left = left

    def __lt__(self, other):
        return self.letters_freq < other.letters_freq


def leaf(root):
    return root.left is None and root.right is None


def huff_en(root, s, code):
    if root is None:
        return

    if leaf(root):
        code[root.char] = s if len(s) > 0 else '1'
    huff_en(root.right, s + '1', code)
    huff_en(root.left, s + '0', code)


letters = 'abcdefghijklmnopqrstuvwxyz'
letters_freq = {letter: 0 for letter in letters}
for char in data.lower():
    if char in letters:
        letters_freq[char] += 1

letters_freq = {k: v for k, v in letters_freq.items() if v != 0}

sort_freq = dict(sorted(letters_freq.items(), key=operator.itemgetter(1)))
q = [node(k, v) for k, v in sort_freq.items()]

heapq.heapify(q)

while len(q) > 1:
    left = heapq.heappop(q)
    right = heapq.heappop(q)
    total_freq = left.letters_freq + right.letters_freq
    heapq.heappush(q, node(None, total_freq, left, right))

root = q[0]

huffman_code = {}
huff_en(root, '', huffman_code)
ch = list(huffman_code.keys())
freq = list(huffman_code.values())
print(data)
print(sort_freq)
print(' Char | Huffman code ')
print('----------------------')
for i in range(len(ch)):
    print(ch[i], "    |       ", freq[i])


bina = ""
for i in data:
    bina += huffman_code.get(i)
print("Encode output :", bina)

decoded_str = ""
current_node = root
for bit in bina:
    if bit == "0":
        current_node = current_node.left
    elif bit == "1":
        current_node = current_node.right
    if leaf(current_node):
        decoded_str += current_node.char
        current_node = root

print("Decode output: ", decoded_str)


suii = list(sort_freq.values())
freq_bits = sum(suii)
char_bits = len(ch) * 8
size = []
for i in range (len(suii)):
    size.append(len(freq[i]) * suii[i])
size_bits = sum(size)
print("{} + {} + {} = ".format(char_bits , freq_bits , size_bits) , char_bits + freq_bits + size_bits , "bits")
