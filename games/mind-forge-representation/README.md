# MIND//FORGE 0.5 · THE WRONG EYES

## Purpose

Teach representation and feature engineering by keeping the model fixed while changing how the same physical world is encoded for it.

## Core lesson

The player first trains one sigmoid neuron directly on raw X/Y position measurements for a ring-shaped classification problem. Gradient descent is real, but the straight decision boundary cannot express the circular rule well.

After repeated honest failure, the input bench unlocks. The player can compare:

- raw X/Y;
- a rotated linear coordinate system, X+Y and X−Y;
- a nonlinear derived feature, distance from center: `sqrt(X^2 + Y^2)`.

The model remains exactly one sigmoid neuron. The radius representation converts a difficult geometric problem into a simple threshold.

## Teaching sequence

1. Present the physical pattern without terminology.
2. Let the player train the raw model and see it plateau.
3. Unlock representation changes only after repeated attempts.
4. Show that a mere rotation of the axes does not increase what a linear neuron can express.
5. Let the player discover that distance from center captures the structure.
6. Test the chosen representation on untouched positions.
7. Only then name feature, representation, and feature engineering.

## Mathematical truth

The model is logistic regression:

`p(y=1|x) = sigmoid(w·phi(x) + b)`

where `phi(x)` is the representation selected by the player.

For raw coordinates:

`phi(x,y) = [x, y]`

For rotated coordinates:

`phi(x,y) = [x+y, x-y]`

For the nonlinear radius feature:

`phi(x,y) = [sqrt(x^2+y^2)]`

The raw and rotated forms remain linear transforms of the same two-dimensional coordinates, so a single neuron still produces a straight boundary. Radius changes the representation nonlinearly, allowing the same neuron to separate inner from outer points with a threshold.

## Validation

- JavaScript syntax checked with Node before commit.
- Deterministic numerical smoke test confirms raw X/Y plateaus near chance-to-moderate accuracy while radius reaches full training accuracy.
- The final test set uses different angles and radii from training.

## Boundaries

No backend, analytics, account, model API, or network call is introduced. All learning occurs locally in the browser.
