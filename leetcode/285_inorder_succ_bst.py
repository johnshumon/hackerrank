class Node:
    "Node structure of the tree"

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def insert_node(self, node: Node, key: int) -> Node:
        """Inserts a node in the tree"""
        # > Tree is empty
        # ------------------
        if node is None:
            return Node(key)

        # > Node already exists
        #   avoid duplication of keys
        # ---------------------------
        if key == node.key:
            return node

        # > Add node recursively in the sub-tree
        # --------------------------------------
        if key < node.key:
            if node.left:
                self.insert_node(node.left, key)
            else:
                node.left = Node(key)
                node.left.parent = node

        elif key > node.key:
            if node.right:
                self.insert_node(node.right, key)
            else:
                node.right = Node(key)
                node.right.parent = node

        return node

    def inorder_successor(self, node: Node) -> Node:
        """Returns in-order successor of a given node
        if exists. None otherwise.
        """
        # > The successor is somewhere lower in the right subtree
        #   successor: one step right and then all the way left.
        if node.right:
            return self.get_leftmost_node(node.right)

        # > The successor is somewhere upper in the tree
        parent = node.parent
        child = node

        while parent.right == child:
            if parent.parent is None:
                return None

            child = parent
            parent = parent.parent

        return parent

    def get_leftmost_node(self, node: Node) -> Node:
        """Returns the left most node of a given
        node if any. i.e. Returns the key with
        the minimum value.
        """
        if node is None:
            return None

        return node if node.left is None else self.get_leftmost_node(node.left)

    def build_tree(self, elements: list) -> list:
        """build a binary search tree with the
        given list of elements
        """
        print("build tree with these elements: {}".format(elements))

        root = Node(elements[0])
        for i in range(1, len(elements)):
            self.insert_node(root, elements[i])

        return root


def main():
    solution = Solution()

    # builds the binary search tree
    # bst = solution.build_tree([20, 8, 22, 4, 12, 10, 14, 8])
    # bst = None
    # bst = solution.build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    bst = solution.build_tree([5, 6, 3, 1, 2, 4])

    inorder_succ = solution.inorder_successor(bst.left.right)
    print(
        "in-order successor of {} is: {}".format(bst.left.right.key, inorder_succ.key)
    )


if __name__ == "__main__":
    main()
