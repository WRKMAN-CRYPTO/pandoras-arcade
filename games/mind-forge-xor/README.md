# MIND//FORGE 0.2 — The Impossible Pattern

This chapter teaches why a single neuron is limited and why hidden layers exist.

## Learning objective

The player should discover through manipulation that one logistic neuron creates one straight decision boundary. The XOR arrangement cannot be solved perfectly by any single straight boundary.

Only after the player has tried several line configurations does the game unlock a larger 2→2→1 network.

The player then trains that network with real gradient descent and can reveal the two learned hidden decision boundaries.

## Design rule

Never teach the solution before the player has felt the limitation.

The first phase intentionally permits productive confusion. The player should always be able to see the consequence of moving a control, but the game does not narrate the solution.

## Technical truth

The first machine is logistic regression:

`p = sigmoid(w1*x + w2*y + b)`

Its 0.5 decision boundary is a straight line.

The second machine is a real neural network with:

- 2 inputs
- 2 sigmoid hidden neurons
- 1 sigmoid output neuron
- binary cross-entropy loss
- full-batch gradient descent
- explicit backpropagation through all 9 trainable parameters

No backend, model API, or simulated training is used.

## Progression

1. Player attempts XOR with one line.
2. After repeated tests, the game suggests the limitation may be architectural rather than a bad knob setting.
3. A hidden layer is unlocked.
4. The player can train manually in 25-step bursts or run continuous training.
5. The player may reveal the two learned hidden boundaries.
6. An unknown jittered XOR batch tests whether the learned rule generalizes beyond the four exact training coordinates.

## What to observe in playtesting

- Does the player first blame their own parameter choices rather than immediately guessing that the problem is impossible?
- Is the eventual architecture realization satisfying rather than frustrating?
- Does watching two hidden boundaries appear make the hidden-layer concept more concrete?
- Does the player understand that training changed the representation capacity being used, not merely found a better single line?
- Is there enough experimentation before the game unlocks the second neuron?

## Next chapter candidate

0.3 should introduce overfitting by giving the player a model capable of scoring perfectly on training examples while failing on unseen examples.