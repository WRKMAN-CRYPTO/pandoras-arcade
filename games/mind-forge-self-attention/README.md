# MIND//FORGE 0.9 · EVERY WORD ASKS

Interactive lesson for self-attention.

## What the player experiences

A four-token sentence begins with nearly uniform attention. The player first sees that equal listening cannot provide useful context. Training then adjusts shared query/key vectors so each token role learns a different destination inside the same sentence.

The primary control advances 10 gradient steps and renders every intermediate update so the attention matrix can be watched as it sharpens.

## Mechanism

- Four token roles: WORKER, VERB, TRAIT, OBJECT.
- Each role has a trainable 3D query vector and a trainable 3D key vector.
- Scores are scaled dot products: `q · k / sqrt(3)`.
- Softmax converts the four scores into one attention row.
- Cross-entropy trains the intended relation for each querying role.
- Gradients are computed directly in the browser and update both query and key vectors.

The teaching targets are intentionally simple and inspectable:

- WORKER → VERB
- VERB → OBJECT
- TRAIT → OBJECT
- OBJECT → TRAIT

Actual vocabulary changes across workshop sentences. Final inspection uses entirely new surface words, testing whether the learned routing depends on role geometry rather than memorized vocabulary.

## Teaching boundary

This is a genuine trainable single-head self-attention mechanism, but it intentionally isolates query/key routing. It is not presented as a complete transformer block. A production transformer also uses learned value/output projections, residual connections, normalization, feed-forward layers, positional information, and usually many attention heads.

## Design rule

Do not define self-attention before the player experiences the failure of uniform listening and watches different rows acquire different destinations.

## Runtime

Static HTML/CSS/JavaScript. No backend, model API, pretrained model, analytics, account, or network call.