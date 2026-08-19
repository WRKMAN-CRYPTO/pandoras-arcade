# MIND//FORGE 1.0 · THE TRANSFORMER BLOCK

A mobile-first assembly lesson for the core dataflow inside a miniature transformer block.

## Teaching goal

The learner should be able to mentally replay the block as a sequence of transformations rather than remember a static architecture diagram.

The chapter reveals the pipeline one stage at a time:

1. token vectors
2. scaled dot-product self-attention
3. first residual addition
4. layer normalization
5. position-wise feed-forward network
6. second residual addition + layer normalization

After the complete pass, the learner deliberately removes the first residual path and compares how much of each token's original representation survives. Restoring the bypass unlocks an unseen-vocabulary routing inspection.

## Implementation

Everything runs locally in one static page.

- four 8D token vectors
- deterministic query/key role projections
- scaled dot-product scores and softmax attention
- value mixing over the real token vectors
- residual additions
- token-wise layer normalization
- deterministic 8 → 12 → 8 ReLU feed-forward network
- second residual + normalization

The chapter uses fixed already-learned parameters. It is an assembly/inspection lesson, not a training lesson. That distinction is intentional.

## Final inspection

The sentence vocabulary changes from `MIRA MOVES RED CRATE` to `LEO PAINTS BLUE WALL`. The same role structure is used with the same block parameters, and the final check verifies that each query role still routes to the intended key role.

## Boundary

This is a miniature post-normalization transformer-style block built for conceptual inspection. Production transformer families differ in normalization placement, dimensionality, multi-head structure, nonlinearities, positional encoding, masking, and many other details. The page does not claim to reproduce a modern LLM architecture.

No backend, analytics, account, model API, pretrained model, or network call is used.