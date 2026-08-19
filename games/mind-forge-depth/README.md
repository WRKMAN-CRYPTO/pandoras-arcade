# MIND//FORGE 0.6: BEND THE SPACE

## Goal
Teach that hidden layers can learn useful representations by transforming the geometry of data across depth.

The player trains a real `2 -> 3 -> 2 -> 1` neural network on a ring-shaped classification problem, then inspects the same physical points in three spaces:

1. raw input coordinates,
2. the first hidden representation,
3. the second hidden representation.

The lesson is not that points literally move in the world. Their internal coordinates change as the network learns features useful for the final decision.

## Model

- Inputs: `(x, y)`
- Hidden layer 1: 3 tanh units
- Hidden layer 2: 2 tanh units
- Output: 1 sigmoid unit
- Objective: binary cross-entropy
- Optimization: full-batch gradient descent implemented directly in the page

No ML library or remote model API is used.

## Teaching sequence

### Stage 1: Train without seeing inside
The player only sees the raw rings and training metrics. Hidden-space views remain locked until the network learns the task well enough.

### Stage 2: Open the machine
The first and second hidden spaces unlock. The player can switch among raw, hidden 1, and hidden 2 while looking at the same labeled examples.

The intended discovery is that the classification problem can become geometrically easier after learned transformations.

### Stage 3: Unknown batch
Fresh points follow the same physical rule but use unseen angles and radii. The network must generalize through the learned representation.

## Design rules protected

- Do not narrate the insight before the player can observe it.
- Keep the real computation visible through consequences rather than equations first.
- Preserve optional terminology in the codex after discovery.
- Keep the chapter phone-first and single-page.
- No backend, account, analytics, or network dependency.

## Important nuance
The 3-unit first hidden layer is displayed using two coordinates at a time. This is a projection of a three-dimensional learned representation, not the complete hidden state. The UI says this explicitly rather than pretending a 2D plot can show all three hidden values.

## Playtest questions

- Did switching from RAW WORLD to HIDDEN 1 or HIDDEN 2 feel meaningfully different?
- Could you perceive the classes becoming easier to separate?
- Did the phrase "internal representation" make more sense after seeing the points move?
- Was training too slow, too fast, or visually flat?
- Did the chapter make depth feel purposeful rather than merely "more neurons"?
