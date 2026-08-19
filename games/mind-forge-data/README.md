# MIND//FORGE 0.4 · BAD INGREDIENTS

## Purpose

Teach a different failure mode from architecture and overfitting: the model may be functioning correctly while the training evidence itself is misleading.

The player should discover three ideas through manipulation before the terminology is introduced:

1. **Label noise** — an incorrect label can distort nearby predictions.
2. **Sampling bias / coverage** — a dataset can be internally consistent while failing to represent parts of the world it will face.
3. **Data quality** — improving the evidence can outperform changing the model.

## Play loop

- The classifier begins as a fixed 1-nearest-neighbor model.
- Training accuracy is initially perfect because each sample is its own nearest neighbor.
- Two labels are deliberately suspicious and sit inside neighborhoods of the opposite class.
- The player may inspect and quarantine any training sample.
- Field validation then exposes performance by geographic yard, making missing coverage visible.
- A survey action adds evidence from the previously underrepresented yards.
- The final batch is untouched and locks further curation.

## Why 1-nearest-neighbor

The model is intentionally simple and transparent. The player already encountered k-nearest-neighbors in 0.3, so 0.4 can shift attention away from model choice and toward evidence quality.

With k=1, mislabeled samples exert a local, visible influence and missing neighborhoods remain genuinely unsupported.

## Deterministic expected behavior

Initial dataset:
- 12 active samples
- 12/12 training accuracy
- approximately 7/10 validation accuracy

After quarantining the two suspicious manual relabels:
- 10 active samples
- 10/10 training accuracy
- approximately 9/10 validation accuracy
- missing-yard weakness remains

After surveying the blind yards but leaving bad labels:
- validation improves but remains imperfect

After both cleaning suspicious labels and adding missing-yard evidence:
- 10/10 validation
- 10/10 current final test set

The pass threshold is intentionally 9/10 so the game does not imply that real generalization must be perfect.

## Teaching rule

Do not tell the player which samples are wrong. Provide provenance and neighborhood context, then let the contradiction become visible.

Do not frame collection as “more data is always better.” The new samples are useful because they cover missing regions, not because the count increased.

## Technical architecture

- static HTML/CSS/JavaScript
- no backend
- no analytics
- no model API
- no network calls
- Canvas visualization
- exact Euclidean 1-nearest-neighbor inference in-browser

## Playtest questions

After play, ask:

- Did the two suspicious points become obvious from their neighborhoods, their provenance note, or both?
- Did the yard-by-yard validation make the coverage problem legible?
- Did the survey action feel like “collect the missing evidence” or merely “press the next button”?
- Did it become clear that the classifier itself never changed?
- Was the difference between bad labels and missing coverage distinct enough?

## Next chapter candidate

Move from static classification toward representations or sequence learning. A useful next bridge is feature engineering: give the model raw measurements that are individually weak, then let the player construct a feature that makes the underlying structure easier to learn.
