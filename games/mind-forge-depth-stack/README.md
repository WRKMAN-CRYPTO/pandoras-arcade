# MIND//FORGE 1.1 · LAYER BY LAYER

## Purpose

Teach depth as successive representation transformation. The learner watches the same token set move through three miniature transformer blocks and inspects how the representation handed to each later block differs from the raw input.

## Teaching rule

Do not define depth before the learner sees the same data change across multiple blocks.

## Mechanism

- Four tiny four-token sentences are embedded into 8D vectors.
- Each block performs local scaled-score self-attention, value mixing, residual addition, token-wise normalization, and a deterministic feed-forward-style transformation.
- The feed-forward transformation progressively exposes role structure in the first two dimensions so the learner can watch neighborhoods emerge.
- The UI plots dimensions 1 and 2 only and says so explicitly. It does not claim the 2D picture is the full 8D state.
- Each block transition is animated over 1.5 seconds and can be replayed.
- A simple nearest-centroid role-clarity score is computed in the displayed 2D projection.
- The final inspection sends a new sentence through all three blocks and classifies its final projected positions against the role centroids formed by the four workshop sentences.

## Important boundary

This is a miniature fixed-parameter teaching stack, not a trained production language model. The grammar is intentionally tiny and regular so the learner can isolate the concept of depth. The point is that later blocks receive transformed representations from earlier blocks, not that this toy system demonstrates broad language understanding.

## Runtime

Static HTML/CSS/JavaScript. No backend, analytics, account, external model API, pretrained model, or network call.