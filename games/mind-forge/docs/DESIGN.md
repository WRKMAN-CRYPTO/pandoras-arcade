# MIND//FORGE 0.1 Design Document

## Mission

Create a 15–20 minute game in which a player gains an operational intuition for the smallest useful learning model: a single logistic neuron.

The prototype succeeds when the player can reason about a broken model without merely repeating definitions.

## Core fantasy

The player has inherited a workshop sorter that receives two measurements from each stone:

- mass
- heat

Red and blue stones must be separated. The machine begins ignorant. The player teaches it by adjusting parameters and later allowing the machine to adjust those same parameters automatically.

## Core loop

1. Observe classifications.
2. Adjust a parameter.
3. Watch the decision boundary change.
4. Test the machine.
5. Inspect mistakes.
6. Reduce error.
7. Complete the work order.

The decision boundary is always visible so parameter changes are spatially legible.

## Teaching pattern

Every concept follows the same order:

1. **Need** — the current machine becomes inconvenient or insufficient.
2. **Experiment** — the player receives a mechanism to manipulate.
3. **Consequence** — the world responds immediately.
4. **Discovery** — the formal term is named.
5. **Mastery** — the player must use it without step-by-step instruction.

## Contracts

### Contract 1 — Sort This

The player manipulates mass and heat weights to improve classification. The goal is not mathematical optimization. It is discovering that inputs can influence a decision with different strengths and directions.

### Contract 2 — Make Mass Matter

The player is pushed toward reasoning about one feature's contribution rather than moving knobs randomly. Tapping a stone exposes its weighted contributions and predicted probability.

### Contract 3 — Move the Line

The dataset shifts. Correct orientation alone is insufficient. Bias is unlocked and presented first as an offset control. Once used, it is named formally.

### Contract 4 — How Wrong Are You?

Accuracy alone becomes an incomplete signal. Binary cross-entropy loss is exposed as "Total error." The player learns to distinguish a barely wrong prediction from a confidently wrong one.

### Contract 5 — Teach Yourself

The player has already done the job that training automates. Gradient descent becomes available only after manual parameter adjustment has become repetitive.

### Contract 6 — Don't Overshoot

The learning-rate selector provides Tiny, Medium, and Huge steps. Large steps are allowed to behave badly. Failure is evidence, not a modal warning.

## Final inspection

The learned model is evaluated on an unseen batch with controls locked. This plants the seed of generalization before version 0.2 formally introduces train/test splits and overfitting.

## Failure philosophy

The game should avoid "Wrong answer" messages wherever the underlying system can show the reason instead.

Bad weights rotate or invert the boundary.
Bad bias shifts it.
A huge learning rate can oscillate.
Wrong stones are outlined visibly.
Inspect mode exposes the numerical contributions that produced a decision.

## Scope protection

Do not add hidden layers, transformers, code editors, currencies, accounts, leaderboards, cloud saving, narrative campaigns, or cosmetic progression to 0.1.

The core question is whether one neuron can be made understandable and satisfying.

## Planned progression

- 0.2 — generalization and overfitting
- 0.3 — XOR and the limit of one neuron
- 0.4 — hidden layers
- 0.5 — backpropagation
- 0.6 — image classification
- 0.7 — dataset quality and bias
- 0.8 — sequence models
- 0.9 — attention
- 1.0 — transformer construction
