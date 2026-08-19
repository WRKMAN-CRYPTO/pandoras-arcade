# MIND//FORGE 1.2 · THE SEALED FUTURE

A mobile-first browser lesson about causal next-token prediction.

## Lesson

The player first sees an evaluator that is allowed to read the target token and therefore reports perfect performance. Deployment hides the future and exposes that result as leakage. A triangular visibility map then seals all future positions while a small trainable causal next-token model learns from legal prefixes only.

The primary training control advances 10 gradient steps and renders every update so changes in the probability distribution can be watched gradually.

## Model

This chapter intentionally isolates the language-model training objective from transformer architecture. It uses a trainable bigram context-to-logit table with softmax and cross-entropy. That is a genuine causal next-token model, but not a transformer.

The important invariant is that a prediction may depend only on the prefix available before the target token. The chapter names this constraint as a causal mask only after the player experiences the failure caused by future leakage.

## Final inspection

Four complete token sequences are withheld from training. They are novel recombinations of local transitions that were observed elsewhere in the training corpus. The final inspection checks each hidden next-token target using only left context.

## Boundaries

- no backend
- no analytics
- no account
- no external model API
- no pretrained model
- no network calls
- tiny fixed vocabulary and corpus
