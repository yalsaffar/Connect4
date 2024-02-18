from copy import deepcopy
import math
import random

class Node():
    def __init__(self, state, parent=None):
        """
        Initializes a Node object.

        Args:
            state: The state of the node.
            parent: The parent node. Default is None.
        """
        self.visits = 1
        self.reward = 0.0
        self.state = state
        self.children = []
        self.children_move = []
        self.parent = parent

    def add_child(self, child_state, move):
        """
        Adds a child node to the current node.

        Args:
            child_state: The state of the child node.
            move: The move made to reach the child node.
        """
        child = Node(child_state, self)
        self.children.append(child)
        self.children_move.append(move)

    def update(self, reward):
        """
        Updates the reward of the node.

        Args:
            reward: The reward to be added to the node's reward.
        """
        self.reward += reward
        self.visits += 1

    def fully_explored(self):
        """
        Checks if all possible moves have been explored.

        Returns:
            True if all possible moves have been explored, False otherwise.
        """
        if len(self.children) == len(self.state.legal_moves()):
            return True
        return False



def MTCS(maxIter, root, factor):
    """
    Performs Monte Carlo Tree Search.

    Args:
        maxIter: The maximum number of iterations.
        root: The root node of the tree.
        factor: The exploration factor.

    Returns:
        The best child node found.
    """
    for inter in range(maxIter):
        front, turn = tree_policy(root, 1, factor)
        reward = default_policy(front.state, turn)
        backup(front, reward, turn)

    ans = best_child(root, 0)
    return ans


def tree_policy(node, turn, factor):
    """
    Selects the next node to explore in the tree.

    Args:
        node: The current node.
        turn: The turn of the player.
        factor: The exploration factor.

    Returns:
        The next node to explore and the updated turn.
    """
    while node.state.terminal() == False and node.state.winner() == 0:
        if node.fully_explored() == False:
            return expand(node, turn), -turn
        else:
            node = best_child(node, factor)
            turn *= -1
    return node, turn


def expand(node, turn):
    """
    Expands the node to fully explore the tree.

    Args:
        node: The node to expand.
        turn: The turn of the player.

    Returns:
        The newly added child node.
    """
    tried_children_move = [m for m in node.children_move]
    possible_moves = node.state.legal_moves()

    for move in possible_moves:
        if move not in tried_children_move:
            row = node.state.try_move(move)
            new_state = deepcopy(node.state)
            new_state.board[row][move] = turn
            new_state.last_move = [row, move]
            break

    node.add_child(new_state, move)
    return node.children[-1]


def best_child(node, factor):
    """
    Returns the best child node using an evaluation formula.

    Args:
        node: The current node.
        factor: The exploration factor.

    Returns:
        The best child node.
    """
    bestscore = -10000000.0

    best_children = []
    for c in node.children:
        exploit = c.reward / c.visits
        explore = math.sqrt(math.log(2.0 * node.visits) / float(c.visits))
        score = exploit + factor * explore
        if score == bestscore:
            best_children.append(c)
        if score > bestscore:
            best_children = [c]
            bestscore = score
    return random.choice(best_children)


def default_policy(state, turn):
    """
    Evaluates the score of the state.

    Args:
        state: The current state.
        turn: The turn of the player.

    Returns:
        The score of the state.
    """
    while state.terminal() == False and state.winner() == 0:
        state = state.next_state(turn)
        turn *= -1
    return state.winner()


def backup(node, reward, turn):
    """
    Performs the backpropagation algorithm.

    Args:
        node: The current node.
        reward: The reward to be propagated.
        turn: The turn of the player.
    """
    while node != None:
        node.visits += 1
        node.reward -= turn * reward
        node = node.parent
        turn *= -1
    return
