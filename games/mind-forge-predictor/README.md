# MIND//FORGE 1.3 · THE PREDICTOR

Purpose: connect the causal next-token objective from 1.2 to the transformer machinery learned in 1.0 and 1.1.

## What is real

- 8D token vectors run locally in the browser.
- A causal single-head attention body can only attend to visible prefix positions.
- The final prefix state is converted into vocabulary logits.
- Softmax produces a next-token distribution.
- Cross-entropy gradients train the output projection in 10-step or 50-step batches.
- Final inspection uses unseen prefixes.

## Teaching sequence

1. Read the legal prefix only.
2. Watch causal attention mix the prefix.
3. Inspect the resulting 8D hidden state.
4. Watch the trainable language-model head turn that state into probabilities.
5. Train in 10-step increments and observe probability mass move.
6. Test unseen prefixes.

## Boundary

The transformer body is fixed in this chapter. Only the output prediction head trains. This is intentional so the learner can isolate where the language-model objective attaches to a decoder-style transformer. Production LLM pretraining updates the transformer parameters as well.

No backend, analytics, account, external model API, pretrained model, or network calls.