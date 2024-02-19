class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Visits the nodes of the tree in the following order: left subtree, root node, right subtree.
    def symetric_traversal(self, node=None):
        if node is None:
            node = self.root

        # Left subtree
        if node.left:
            self.symetric_traversal(node.left)
        # Root node
        print(node, end=" ")
        # Right subtree
        if node.right:
            self.symetric_traversal(node.right)

    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root

        # Left subtree
        if node.left:
            self.post_order_traversal(node.left)
        # Right subtree
        if node.right:
            self.post_order_traversal(node.right)
        # Root node
        print(node, end=" ")

    def height(self, node=None):
        if node is None:
            node = self.root

        left_height = 0
        right_height = 0

        if node.left:
            left_height = self.height(node.left)

        if node.right:
            right_height = self.height(node.right)

        if left_height > right_height:
            return left_height + 1

        return right_height + 1

    def tree_sum(self):
        def tree_sum_root(node):
            if node is None:
                return 0
            print(node.data, end=" ")
            return node.data + tree_sum_root(node.left) + tree_sum_root(node.right)

        return tree_sum_root(self.root)


if __name__ == "__main__":

    tree = BinaryTree()

    n1 = Node("a")
    n2 = Node("+")
    n3 = Node("*")
    n4 = Node("b")
    n5 = Node("-")
    n6 = Node("/")
    n7 = Node("c")
    n8 = Node("d")
    n9 = Node("e")

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2

    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e'
    #           /   \
    #         'c'   'd'

    # (a + (b * ((c/d) - e)))

    tree.symetric_traversal()
    print("\nTree Height:", end="")
    print(tree.height())

    tree_digit = BinaryTree()

    n1 = Node(11)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(2)
    n5 = Node(8)
    n6 = Node(13)
    n7 = Node(7)
    n8 = Node(0)
    n9 = Node(4)

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree_digit.root = n2

    #      '3'
    #    /     \
    #  '11'      '4'
    #          /   \
    #        '2'    '8'
    #              /    \
    #            '13'    '4'
    #           /   \
    #         '7'   '0'

    # (11+3+4+2+8+13+7+0+4) = 52

    print("\n\nTree Sum:", end="\n")
    print("\nsum:", tree_digit.tree_sum())

    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")
    n4 = Node("D")
    n5 = Node("E")
    n6 = Node("F")
    n7 = Node("G")
    n8 = Node("H")
    n9 = Node("I")

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n6.left = n8
    n6.right = n9

    tree.root = n1
    print("")
    tree.symetric_traversal()
