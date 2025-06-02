
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""

i'm going to assume that each node is an integer with no goofy characters
that means i will use something like # or a comma as a delimiter to separate nodes
    perhaps in the same format as shown in the question

this was not a fun question
i never want to do this ever again

runtime: O(n) where n is the number of nodes
space: O(n)

"""

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str

        will use a breadth first search to add each layer by layer to the string
        (,) = delimiter
        (#) = null
        [1,2,3,null,null,4,5] -> "", queue = [1]
        [2,3,null,null,4,5] -> "1", queue = [2,3]
        [null,null,4,5] -> "1,2,3", queue = [null, null, 4, 5]
        [1,2,3,null,null,4,5] -> "1,2,3,#,#,4,5"

        """
        
        if not root:
            return ""

        res = ""
        queue = deque([root])
        while queue:
            curr = queue.pop()

            if curr:
                if curr.left:
                    queue.appendleft(curr.left)
                else:
                    queue.appendleft(None)
                if curr.right:
                    queue.appendleft(curr.right)
                else:
                    queue.appendleft(None)

            if curr:
                res += str(curr.val)
            else:
                res += "#"
            res += ","

        print(res[:-1])
        return res[:-1]
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode

        recap of serialize
            will use a breadth first search to add each layer by layer to the string
            (,) = delimiter
            (#) = null
            [1,2,3,null,null,4,5] -> "", queue = [1]
            [2,3,null,null,4,5] -> "1", queue = [2,3]
            [null,null,4,5] -> "1,2,3", queue = [null, null, 4, 5]
            [1,2,3,null,null,4,5] -> "1,2,3,#,#,4,5", queue = []
        
        start your TreeNode with the first character in string
        can probably just use another bfs to build the tree
        use some kind of stack and keep popping the top two elements as the children of
        the element at the top of the stack

        "1,2,3,#,#,4,5" -> [], queue = [1]
        "2,3,#,#,4,5" -> [1], queue = [2,3]
        "#,#,4,5" -> [1,2,3], queue = [null, null, 4, 5]
        "" -> [1,2,3,null,null,4,5], queue = []
        """

        
        if len(data) == 0:
            return None
        if data[0] == "#":
            return None
        
        data = data.split(",")
        root = TreeNode(data[0])
        queue = deque([root])
    
        i = 1
        while queue:
            curr = queue.popleft()

            if data[i] != "#":
                left = TreeNode(int(data[i]))
                curr.left = left
                queue.append(left)
            i += 1

            if data[i] != "#":
                right = TreeNode(int(data[i]))
                curr.right = right
                queue.append(right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))