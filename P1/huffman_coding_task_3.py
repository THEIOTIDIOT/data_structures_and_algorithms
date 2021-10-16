import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.char = None
        self.left_child = None
        self.right_child = None
        self.left_code = None
        self.right_code = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_char(self, char):
        self.char = char
    
    def get_char(self):
        return self.char

    def set_left_child(self, left):
        self.left = left

    def get_left_child(self):
        return self.left_child

    def set_right_child(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None
    
    def set_left_code(self, left_code):
        self.left_code = left_code
    
    def get_left_code(self):
        return self.left_code
    
    def set_right_code(self, right_code):
        self.right_code = right_code
    
    def get_right_code(self):
        return self.right_code

    def __repr__(self):
            return repr((self.value, self.char))

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

def char_freq_dict(data):
    char_freq = {}
    for char in data:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq

def huffman_encoding(data):

    freq = ''
    freq_tup = tuple()
    char_freq_list = list()
    char_freq_lo_hi_list = list()
    char_set = set(data)
    char_list = list(char_set)

    #take a string and determine the relevant frequencies of the characters
    char_dict = char_freq_dict(data)

    #build and sort a list of tuples from lowest to highest frequencies
    for item in char_list:
        freq = char_dict[item]
        new_node = Node(freq)
        new_node.set_char(item)
        char_freq_list.append(new_node)

    #one way to generate a sorted list 
    #char_freq_lo_hi_list = min_heap_queue(char_freq_list)
    char_freq_lo_hi_list = sorted(char_freq_list, key=lambda freq: cha)

    #build a huffman tree by assigning a binary code to each letter, using
    #shorter codes for the more frequent letters. (This is the heart of the
    #huffman algorithm.)
    

    #trim the Huffman Tree (remove the frequencies from the previously built
    #tree)
    return char_freq_lo_hi_list

def recursive_huffman_tree(char_freq_lo_hi_list):
    #if char_freq_lo_hi_list == 1:
    #    return
    pass



def min_heap_queue(char_freq_list):
    #return sorted(char_freq_list, key=lambda freq: node.value)
    pass




#def huffman_decoding(data,tree):
 #   pass

