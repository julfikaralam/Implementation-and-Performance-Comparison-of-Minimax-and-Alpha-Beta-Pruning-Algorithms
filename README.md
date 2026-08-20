# Implementation-and-Performance-Comparison-of-Minimax-and-Alpha-Beta-Pruning-Algorithms
Implementation and Performance Comparison of Minimax and Alpha-Beta Pruning Algorithms Using a Random Binary Game Tree

---

## 🎯 Objectives

The objectives of this project are:

- To understand the working process of the Minimax algorithm.
- To implement Alpha-Beta Pruning as an optimization technique.
- To generate a random binary game tree with leaf node scores.
- To compare the performance of Minimax and Alpha-Beta Pruning.
- To calculate the efficiency improvement of Alpha-Beta Pruning.

---

## 📝 Problem Statement

In Artificial Intelligence, game-playing agents need to make optimal decisions by exploring possible future states. The Minimax algorithm is commonly used for this purpose, but it becomes inefficient for large game trees because it evaluates every possible node.

Alpha-Beta Pruning improves Minimax by eliminating branches that cannot affect the final decision. In this project, both algorithms are applied to the same randomly generated binary game tree to find the optimal value and compare their efficiency.

---

# 🧠 Algorithms Used

## 1. Minimax Algorithm

Minimax is a recursive decision-making algorithm used in two-player games.

- The **MAX player** tries to maximize the score.
- The **MIN player** tries to minimize the score.
- The algorithm explores the complete game tree and returns the optimal value.

### Working Steps:

1. Start from the root node.
2. Recursively explore child nodes.
3. MAX selects the highest value.
4. MIN selects the lowest value.
5. Return the final optimal value.

---

## 2. Alpha-Beta Pruning Algorithm

Alpha-Beta Pruning is an optimized version of the Minimax algorithm.

It reduces unnecessary calculations by ignoring branches that do not influence the final decision.

### Working Steps:

1. Maintain two values:
   - Alpha: Best value for MAX player.
   - Beta: Best value for MIN player.
2. Evaluate child nodes recursively.
3. Update alpha and beta values.
4. Skip branches when further searching is unnecessary.
5. Return the optimal value.

---

# ⚙️ Implementation Details

### Programming Language

- Python 3

### Libraries Used

| Library | Purpose |
|---------|---------|
| random | Generate random leaf node values |
| math | Calculate tree depth |

### Tree Configuration

- Binary game tree
- 16 leaf nodes
- Randomly generated node scores
- Automatic tree depth calculation

---
## 💻 Source Code Implementation

The complete implementation of **Minimax** and **Alpha-Beta Pruning** algorithms is written in Python.

```python
import random
import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, counter):
    # Leaf node
    if curDepth == targetDepth:
        counter[0] += 1
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth, counter),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, counter)
        )

    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth, counter),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, counter)
        )


def alphabeta(curDepth, nodeIndex, isMax, scores, targetDepth, alpha, beta, counter, prune):
    if curDepth == targetDepth:
        counter[0] += 1
        return scores[nodeIndex]

    if isMax:
        best = -999999

        val = alphabeta(
            curDepth + 1,
            nodeIndex * 2,
            False,
            scores,
            targetDepth,
            alpha,
            beta,
            counter,
            prune
        )

        best = max(best, val)
        alpha = max(alpha, best)

        if beta <= alpha:
            prune[0] += 2 ** (targetDepth - curDepth - 1)
            return best

        val = alphabeta(
            curDepth + 1,
            nodeIndex * 2 + 1,
            False,
            scores,
            targetDepth,
            alpha,
            beta,
            counter,
            prune
        )

        best = max(best, val)

        return best

    else:
        best = 999999

        val = alphabeta(
            curDepth + 1,
            nodeIndex * 2,
            True,
            scores,
            targetDepth,
            alpha,
            beta,
            counter,
            prune
        )

        best = min(best, val)
        beta = min(beta, best)

        if beta <= alpha:
            prune[0] += 2 ** (targetDepth - curDepth - 1)
            return best

        val = alphabeta(
            curDepth + 1,
            nodeIndex * 2 + 1,
            True,
            scores,
            targetDepth,
            alpha,
            beta,
            counter,
            prune
        )

        best = min(best, val)

        return best


# Generate random leaf nodes
n = random.choice([8, 16])

scores = [random.randint(1, 25) for _ in range(n)]

treeDepth = int(math.log2(n))

print("Generated Leaf Nodes:", scores)


# Minimax Execution
minimax_counter = [0]

minimax_value = minimax(
    0,
    0,
    True,
    scores,
    treeDepth,
    minimax_counter
)

print("\nMinimax:")
print("Nodes Evaluated:", minimax_counter[0])
print("Optimal Value:", minimax_value)


# Alpha-Beta Execution
alpha_counter = [0]
pruned_nodes = [0]

alpha_beta_value = alphabeta(
    0,
    0,
    True,
    scores,
    treeDepth,
    -999999,
    999999,
    alpha_counter,
    pruned_nodes
)

print("\nAlpha-Beta Pruning:")
print("Nodes Evaluated:", alpha_counter[0])
print("Nodes Pruned:", pruned_nodes[0])


# Efficiency Calculation
improvement = (
    (minimax_counter[0] - alpha_counter[0])
    /
    minimax_counter[0]
) * 100

---

![image alt](alph1.png)
![image alt](alph2.png)
