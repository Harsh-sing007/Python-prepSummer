# def simulate():
#     print("Internal Fragmentation Simulate")
#     size = 4096
#     request = 3000

#     print(f"Total Memory Size: {size} bytes")
#     print(f"Requested Memory Size: {request} bytes")
# def get_grade(marks):
#     if marks < 50:
#         return "Fail"
#     elif marks < 60:
#         return "D"
#     elif marks < 70:
#         return "C"
#     elif marks < 80:
#         return "B"
#     elif marks < 90:
#         return "A"
#     elif marks <= 100:
#         return "A+"
#     else:
#         return "Invalid Marks"

# marks = float(input("Enter your marks (0-100): "))

# grade = get_grade(marks)
# print("Grade:", grade)

# def sqrt(x):
#     if not instance(x, (int, float)):
#         raise TypeError("x must Be a int or float")
#     elif x < 0:
#         raise ValueError("x must be non-negative")

# class arraystack:
#     def __init__(self):
#         self.data = []

#         def __len__(self):
#             return len(self.data)
        
#         def is_empty(self):
#             return len(self.data) == 0
        
#         def push(self,e):
#             self.data.append(e)

#         def top(self):
#             if self.is_empty():
#                 raise Exception("Stack is empty")
#             return self.data[-1]
        
#         def pop(self):
#             if self.is_empty():
#                 raise Exception("Stack is empty")
#             return self.data.pop()
        
# jack = arraystack()
# print(jack.is_empty)
# jack.push(10)
# jack.push(20)
# jack.push(30)
# print(len(jack))


# class arrayqueue: 
#     DEFAULT_CAPACITY = 10
    
#     def __init__(self):
#         self.data = [None] * arrayqueue.DEFAULT_CAPACITY
#         self.size = 0
#         self.front = 0
        
#     def __len__(self):
#         return self.size
    
#     def is_empty(self):
#         return self.size == 0
    
#     def first(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")
#         return self.data[self.front]
    
#     def dequeue(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")
#         answer = self.data[self.front]
#         self.data[self.front] = None
#         self.front = (self.front + 1) % len(self.data)
#         self.size -= 1
#         return answer
    
#     def enqueue(self, e):
#         if self.size == len(self.data):
#             self.resize(2 * len(self.data))
#         avail = (self.front + self.size) % len(self.data)
#         self.data[avail] = e
#         self.size += 1
        
#     def resize(self, cap):
#         old = self.data
#         self.data = [None] * cap
#         walk = self.front
#         for k in range(self.size):
#             self.data[k] = old[walk]
#             walk = (1 + walk) % len(old)
#         self.front = 0
import random

Pieces=["bP","bR","bN","bB","bQ","bK","wP","wR","wN","wB","wQ","wK"]

Piece_values={'P':100,'N':300,'B':320,'R':500,'Q':900,'K':20000}

class Gamestate:
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.white_to_move=True
        self.move_log=[]

        self.zobrist_hash=zobrist.get_initial_hash(self.board,self.white_to_move)

    def print_board(board):
        print("\n a b c d e f g h")
        for r in range(8):
            print(f"{8-r}",end="")
            for c in range(8):
                piece=board[r][c]
                print(f"[{piece if piece != '--' else ' '}]")
            print(f"{8-r}")
        print(" a b c d e f g h \n")
    

    


class Move:
    ranks_to_rows={"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rows_to_rank={v:k for k, v in ranks_to_rows.items()}

    files_to_cols={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    cols_to_files={v:k for k,v in files_to_cols.items()}

    def __init__(self,start_sq,end_sq,board):
        self.start_row,self.start_col=start_sq
        self.end_row,self.end_col=end_sq
        self.piece_moved=board[self.start_row][self.start_col]
        self.pieces_captured=board[self.end_row][self.end_col]
        self.move_id=self.start_row*1000+self.start_col*100+self.end_row*10+self.end_col
        

    def __eq__(self,other):
        if instance(other,move):
            return self.move_id == other.move_id
        return False

    def get_algebraic_notation(self):
        return self.get_rank_files(self.start_row,self.start_col)+(self.get_row,self.end_col)

    def get_rank_file(self,row,col):
        return self.cols_to_find[col]+self.rows_to_rank[row]

    
class zobrist:
    def __init__(self):
        self.table=[[[random.getrandbits(64)] for _ in range(12)] for _ in range(8)]
        self.white_to_move_key=random.getrandbits(64)

    def get_initial_hash(self,board,white_to_move):
        h=0
        for r in range(8):
            for c in range[8]:
                piece=board[r][c]
                if piece!='--':
                    piece_idx=piece_to_idx[piece]
                    h^=self.table[r][c][piece_idx]
        if white_to_move:       
            h^=self.white_to_move_key
        return h

zobrist=zobrist()