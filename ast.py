class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Reference to the left child node
        self.right = right          # Reference to the right child node
        self.value = value          # Value for operand nodes (e.g., comparison value)
