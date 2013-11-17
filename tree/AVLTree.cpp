/**
 * In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if they differ by more than one, rebalancing is done.
 * Complexity - O(log n)
 */
class AVLTree
{
private: 
	class Node
	{
	private:
		int data;
		int height;
		Node *parent;
		Node *left_child;
		Node *right_child;
	public:
		Node(int val) {
			data = val;
			height = 0;
			parent = (Node*)0;
			left_child = (Node*)0;
			right_child =(Node*)0;
		}

		int getData() {
			return data;
		}

		int getHeight() {
			return height;
		}

		int updateHeight() {
			if (left_child != 0 && right_child != 0) {
				if (left_child->getHeight() > right_child->getHeight())
					height = left_child->getHeight() + 1;
				else
					height = right_child->getHeight() + 1;
			} else if (left_child != 0) {
				height = left_child->getHeight() + 1;
			} else if (right_child != 0) {
				height = right_child->getHeight() + 1;
			} else {
				height = 0;
			}

			return height;
		}

		int getBalance() {
			Node *n = this;
			if (n->getLeftChild() != 0 && n->getRightChild() != 0) {
				return n->getLeftChild()->getHeight() - n->getRightChild()->getHeight();
			} else if (n->getLeftChild() != 0) {
				return n->getLeftChild->getHeight + 1;
			} else if (n->getRightChild() != 0) {
				return (-1) * (n->getRightChild()->getHeight() + 1);
			} else {
				return 0;
			}
		}

		Node* getParent() {
			return parent;
		}

		void removeParent() {
			parent = (Node*)0;
		}

		Node* getLeftChild() {
			return left_child;
		}

		Node* setLeftChild(Node* new_left) {
			if (new_left != 0)
				new_left->parent = this;
			left_child = new_left;
			updateHeight();

			return left_child;
		}

		Node* getRightChild() {
			return right_child;
		}

		Node* setRightChild(Node* new_right) {
			if (new_right != 0)
				new_right->parent = this;
			right_child = new_right;
			updateHeight();

			return right_child;
		}
	};
}