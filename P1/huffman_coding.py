class Node:
    def __init__(self, freq):
        self.freq = freq
        self.char = None
        self.left = None
        self.right = None
        self.left_code = None
        self.right_code = None

    def set_char(self, char):
        self.char = char

    def get_char(self):
        return self.char
    
    def set_left_code(self, left_code):
        self.left_code = left_code

    def get_left_code(self):
        return self.left_code

    def set_right_code(self, right_code):
        self.right_code = right_code

    def get_right_code(self):
        return self.right_code

    def set_left_child(self, left):
        self.left = left

    def get_left_child(self):
        return self.left

    def set_right_child(self, right):
        self.right = right

    def get_right_child(self):
        return self.right

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None

    def __repr__(self):
        return repr((self.freq, self.char))


class Stack:
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0


class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        return repr((self.node.freq, self.node.char))


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
    char_freq_list = list()
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
        
    min_heap_queue = sorted(char_freq_list, key=lambda freq: freq.freq)

    #build a huffman tree by assigning a binary code to each letter, using
    #shorter codes for the more frequent letters. (This is the heart of the
    #huffman algorithm.)

    root = create_huffman_tree(min_heap_queue)

    huffman_code = encode_characters(root)
    
    #trim the Huffman Tree (remove the frequencies from the previously built
    #tree)

    return huffman_code

def create_huffman_tree(min_heap_queue):
    while len(min_heap_queue) > 1:
        first_node = min_heap_queue[0]
        second_node = min_heap_queue[1]
        new_freq = first_node.freq + second_node.freq
        new_node = Node(new_freq)
        new_node.set_left_child(first_node)
        new_node.set_right_child(second_node)
        new_node.set_left_code('0')
        new_node.set_right_code('1')
        if len(min_heap_queue) >= 2:
            del min_heap_queue[0]
            del min_heap_queue[0]
            min_heap_queue.append(new_node)
            min_heap_queue = sorted(min_heap_queue, key=lambda freq: freq.freq)
        
    return new_node

def encode_characters(root):

    stack = Stack()
    node = root
    state = State(node)
    stack.push(state)
    leaf_code = ''
    huffman_code_dict = {}

    while(node is not None):
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            leaf_code += node.get_left_code()
            node = node.get_left_child()
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            leaf_code += node.get_right_code()
            node = node.get_right_child()
            state = State(node)
            stack.push(state)

        else:
            stack.pop()
            if not stack.is_empty():
                huffman_code_dict[node.get_char()] = leaf_code
                leaf_code = ''
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    return huffman_code_dict


string = "MISSISSIPPI RIVER"
print(huffman_encoding(string))