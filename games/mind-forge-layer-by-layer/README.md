# MIND//FORGE 1.1 · LAYER BY LAYER

## Purpose

Teach transformer depth as successive representation transformation. The learner watches the same token set move through three miniature transformer blocks and sees later blocks operate on the representations created by earlier blocks.

## Experience

- Four tiny sentences begin as 8D token vectors dominated by lexical identity.
- The UI shows a clearly labeled 2D projection of those states.
- The learner advances one block at a time.
- Each transition animates for roughly 1.6 seconds and can be replayed.
- A projection-based nearest-centroid role-clarity score shows how structural neighborhoods emerge across depth.
- The current block's attention matrix remains inspectable.
- Final inspection sends a fifth sentence with unseen vocabulary through all three blocks and classifies the projected final states against the learned workshop neighborhoods.

## Mechanism

Each miniature block performs:

1. softmax self-attention routing,
2. value mixing,
3. residual addition,
4. token-wise normalization,
5. a deterministic feed-forward-style transformation,
6. normalization of the resulting state.

The fixed parameter schedule is tuned so the early representation remains genuinely messy, useful structure appears at intermediate depth, and the final block yields clean structural neighborhoods. A deterministic smoke test of the exact JavaScript algorithm reaches 4/4 on the unseen sentence.

## Boundary

This is a fixed-parameter teaching stack with a deliberately tiny regular grammar. It demonstrates how depth can refine representations. It does not claim broad language understanding or reproduce a production LLM architecture.

Static HTML/CSS/JavaScript only. No backend, analytics, account, external model API, pretrained model, or network call.