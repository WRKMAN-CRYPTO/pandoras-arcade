# MIND//FORGE 0.1 — Teach the First Neuron

A mobile-first browser game that teaches the mechanics of a single artificial neuron by making the player use one before naming the concepts.

## Play

Open `index.html` in any modern browser. No build step, account, backend, model API, or network connection is required after the page is loaded.

For deployment, the entire project can be hosted as a static site on GitHub Pages, Cloudflare Pages, Netlify, or any plain web server.

## What the player actually builds

The machine is a real logistic neuron:

```text
z = w_mass * mass + w_heat * heat + bias
p(red) = sigmoid(z)
```

The automatic training control performs gradient descent on binary cross-entropy loss. Nothing is delegated to an LLM or external AI service.

## Prototype scope

Six contracts teach:

1. Prediction
2. Weights
3. Bias
4. Loss
5. Training / gradient descent
6. Learning rate

The final inspection evaluates the learned rule on an unseen set.

## Design rule

> Never teach the solution before the player has felt the problem.

Formal terminology appears after the player has manipulated or needed the underlying mechanism.

## Mobile design

- portrait-first layout
- large touch targets
- no hover interactions
- no keyboard requirement
- persistent local progress via `localStorage`
- optional inspect panel for deeper numerical detail

## Files

- `index.html` — complete playable game, including styles and learning implementation
- `docs/DESIGN.md` — design goals, loop, progression, and constraints
- `docs/TECHNICAL.md` — model math and implementation notes
- `docs/TESTING.md` — prototype test checklist and learning-validation questions

## Version boundary

0.1 intentionally stops at one neuron. It does not contain hidden layers, XOR, backpropagation derivation, datasets at scale, embeddings, or transformers. Those concepts only earn a place after the player encounters a limitation that requires them.
