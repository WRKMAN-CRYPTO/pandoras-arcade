# MIND//FORGE 1.4 · CHOOSE A FUTURE

Interactive decoding lesson.

## What it teaches

- a next-token probability distribution does not itself select one realized token;
- greedy decoding is deterministic argmax selection;
- temperature rescales logits before softmax;
- top-k truncates the candidate set and renormalizes;
- categorical sampling can produce different outputs from the same model distribution.

## Implementation

Static local HTML/CSS/JS. The lesson uses a small fixed transition-logit model so decoding mechanics can be inspected without retraining a model. Generation, temperature scaling, truncation, softmax, and sampling all execute in-browser.

## Boundary

This is a decoding lesson, not a claim that production LLMs use this exact tiny transition model. Real systems may use transformer-produced logits and additional decoding methods including top-p, penalties, constraints, or deterministic search.
