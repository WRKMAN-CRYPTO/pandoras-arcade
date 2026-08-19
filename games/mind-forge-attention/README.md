# MIND//FORGE 0.8 · THE LOUD ROOM

A mobile-first lesson about **attention as learned routing**.

## Teaching target

The player first experiences the failure of equal weighting: four memories contain four different tool values, and a uniform read produces an ambiguous 25% mixture.

Only after that failure does the attention bench unlock.

The model learns to answer a query such as `MIRA needs their tool` by assigning most of its softmax weight to the memory slot whose key is `MIRA`.

## What is real

This chapter uses a trainable compatibility matrix `W`.

For query name `q` and memory key `k`:

```text
score(q, k) = W[q][k]
attention = softmax(scores)
```

Each memory carries a one-hot tool value. The output tool distribution is the attention-weighted sum of those values.

Because every room is a permutation of the tools, a fixed `MIRA -> HAMMER` lookup cannot solve the task. The tool associated with each name changes from room to room. The useful rule is to route the query to the matching key and then read that slot's value.

Training minimizes cross-entropy on the correct memory. For this permutation task, the gradient with respect to each score is:

```text
attention[k] - 1[k == correct_key]
```

The chapter updates `W` directly with gradient descent.

## Training cadence

The primary control advances **10 training steps** and animates every intermediate step. A 50-step control exists as a secondary accelerator.

This is intentional: watching the attention distribution move is part of the lesson.

## Generalization check

Sixteen tool permutations are used for training.

Eight different permutations are held out for the final inspection. The model must route correctly in those unseen arrangements.

## Boundary

This is genuine **key-value softmax attention**, but it is not yet a full transformer or self-attention block. Names serve as queries/keys and tools serve as values. Later chapters can add learned token embeddings, projections, multiple tokens attending to one another, and transformer structure without pretending those pieces are already present here.

Everything runs locally in the browser. No backend, analytics, account, external model API, pretrained model, or network call is used.
