# MIND//FORGE 0.1 Technical Notes

## Architecture

The prototype is a dependency-free static web application. HTML, CSS, rendering, game state, and learning logic are all contained in `index.html` so the first build is easy to run, inspect, copy, and repair.

No backend is required. Progress is stored in `localStorage`.

## Model

For a stone with mass `x1` and heat `x2`:

```text
z = w1*x1 + w2*x2 + b
p = sigmoid(z)
sigmoid(z) = 1 / (1 + exp(-z))
```

The prediction rule is:

```text
RED  if p >= 0.5
BLUE otherwise
```

The visible line on the plot is the set of points for which `z = 0`:

```text
w1*x1 + w2*x2 + b = 0
```

That is why changing a weight tends to rotate the line and changing bias tends to translate it.

## Loss

The prototype uses mean binary cross-entropy:

```text
L = -mean(y*log(p) + (1-y)*log(1-p))
```

Probabilities are clamped slightly away from 0 and 1 for numerical stability when displaying loss.

## Gradient descent

For logistic regression with binary cross-entropy, the gradient for one sample simplifies to:

```text
error = p - y

dL/dw1 = error*x1
dL/dw2 = error*x2
dL/db  = error
```

The game averages these gradients over the current training batch and updates:

```text
w := w - learning_rate * gradient
```

The three learning-rate presets are intentionally pedagogical rather than optimized:

- Tiny: `0.03`
- Medium: `0.20`
- Huge: `1.50`

## Rendering

The scatterplot is drawn on a `<canvas>` and scaled for device pixel ratio. The plotted decision boundary is recalculated from the current model parameters on every parameter change or training step.

## Inspect mode

When a stone is selected, the game exposes:

- mass contribution `w1*x1`
- heat contribution `w2*x2`
- bias
- total score `z`
- predicted probability of red

This is deliberately optional. The primary layer remains experiential; the inspect layer lets curiosity drill into the arithmetic without interrupting play.

## Persistence

`localStorage['mindforge01']` stores contract progress, parameters, learning rate, and discoveries. Automatic training is never restored as active after reload.

## Security and privacy

The application sends no player data anywhere. It makes no network calls and contains no credentials.
