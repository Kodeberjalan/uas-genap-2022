class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def search(self, target):
        if self.data == target:
            print("Node found")
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("No Node Found")

    def traversePreorder(self):
        print(self.data,end= ' ')
        if self.left:
            self.left.traversePreorder()
        
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data,end= ' ')
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        
        if self.right:
            self.right.traversePostorder()
        
        print(self.data,end=' ')

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    def getNodeAtDepth(self, depth, nodes=[]):
        if depth==0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodeAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.getNodeAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        return nodes

    def addNode(self, val):
        if self.data == val:
            return
        
        if val < self.data:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.addNode(val)
        
        if val > self.data:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.addNode(val)
    def replace(self, old, new):
        if self.data == old:
            self.data = new
        if self.left:
            self.left.replace(old, new)
        if self.right:
            self.right.replace(old, new)


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traversePreorder(self):
        self.root.traversePreorder()
        print(' ')

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def height(self):
        return self.root.height()

    def getNodeAtDepth(self, depth):
        return self.root.getNodeAtDepth(depth)

    def _nodeToChar(self, n, space):
        if n is None:
            return '_' + (' '*space)
        space = space - len(str(n))+1
        return str(n)+(' '*space)

    def printTree(self, label=''):
        print(self.name + ' ' + label)
        height = self.root.height()
        space = 3
        width = int((2**height-1) * (space+1) +1)

        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth>0:
                print(' '*(offset+1) + (' '*(space+2)).join(['/' + (' '*(space-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodeAtDepth(depth, [])
            print ((' '*offset)+ ''.join([self._nodeToChar(n,space) for n in row]))
            space = offset + 1
            offset = int(offset/2)-1
        print ('')

    def addNode(self, val):
        self.root.addNode(val)
    def replace(self, old, new):
        self.root.replace(old, new)
node = Node('A')

node.left = Node('B')
node.left.left=Node('C')
node.left.right=Node('D')
node.left.right.left=Node('E')
node.right = Node('F')
node.right.left=Node('G')
node.right.left.right=Node('I')
node.right.right=Node('H')
myTree = Tree(node, 'Tree')
myTree.printTree()
myTree.replace('B', 'Y')
node.left.left=Node('B')
node.left.left.left=Node('C')
myTree.replace('F','X')
myTree.printTree()
print('Inorder:')
myTree.traverseInorder()
print('\nPreorder:')
myTree.traversePreorder()
print('Postorder:')
myTree.traversePostorder()