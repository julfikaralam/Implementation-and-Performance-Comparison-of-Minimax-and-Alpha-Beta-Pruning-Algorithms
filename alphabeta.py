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
    # Leaf node
    if curDepth == targetDepth:
        counter[0] += 1
        return scores[nodeIndex]

    if isMax:

        best = -999999

        # Left child
        val = alphabeta(curDepth + 1,nodeIndex * 2,False,scores,targetDepth,alpha,beta,counter,prune)

        best = max(best, val)
        alpha = max(alpha, best)

        if beta <= alpha:
            prune[0] += 2 ** (targetDepth - curDepth - 1)
            return best

        val = alphabeta(curDepth + 1,nodeIndex * 2 + 1,False,scores,targetDepth,alpha,beta,counter,prune)

        best = max(best, val)

        return best


    else:

        best = 999999

        val = alphabeta(curDepth + 1,nodeIndex * 2,True,scores,targetDepth,alpha,beta,counter,prune)

        best = min(best, val)
        beta = min(beta, best)

        if beta <= alpha:
            prune[0] += 2 ** (targetDepth - curDepth - 1)
            return best

        val = alphabeta(curDepth + 1,nodeIndex * 2 + 1,True,scores,targetDepth,alpha,beta,counter,prune)

        best = min(best, val)

        return best



n = random.choice([8, 16])

scores = [random.randint(1, 25) for _ in range(n)]

treeDepth = int(math.log2(n))

print("Generated Leaf Nodes:", scores)

# Minimax execution
minimax_counter = [0]

minimax_value = minimax(0,0,True,scores,treeDepth,minimax_counter
)

print("\nMinimax:")
print("Nodes Evaluated:", minimax_counter[0])
print("Optimal Value:", minimax_value)


alpha_counter = [0]
pruned_nodes = [0]

alpha_beta_value = alphabeta(0,0,True,scores,treeDepth,-999999,999999,alpha_counter,
                             pruned_nodes
)

print("\nAlpha-Beta Pruning:")
print("Nodes Evaluated:", alpha_counter[0])
print("Nodes Pruned:", pruned_nodes[0])



improvement = ((minimax_counter[0] - alpha_counter[0])/minimax_counter[0]) * 100

print("\nEfficiency Improvement:", round(improvement, 2), "%")