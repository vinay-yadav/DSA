def inorder(root):
    if root is None:
        return []

    result = []
    result.extend(inorder(root.left))
    result.append(root.val)
    result.extend(inorder(root.right))
    return result
