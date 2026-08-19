# MIND//FORGE 0.3 — The Machine That Memorized

## Learning goal

Teach overfitting, validation, model selection, generalization, and test-set discipline by making a perfect training score initially feel desirable, then showing why that score can be misleading.

## Core interaction

The player controls `k` in a real k-nearest-neighbors classifier.

- `k = 1` memorizes each training example and scores 17/17 on the training floor.
- several training labels are intentionally noisy.
- held-out validation examples follow the underlying clean rule.
- increasing `k` lowers training beauty but improves validation performance.
- the final untouched test batch is shown only after the player selects a setting with strong validation evidence.

The intended discovery is that the best training score is not necessarily the best model.

## Teaching order

1. Tempt the player with the training score.
2. Let `k=1` achieve perfection.
3. Unlock validation only after the player has interacted with the training objective.
4. Allow the perfect model to fail on held-out examples.
5. Let the player discover that a less-perfect training score can generalize better.
6. Lock tuning before the final test batch.
7. Name the concepts only after they have been experienced.

## Real ML underneath

The browser runs a genuine k-nearest-neighbors classifier. For a query point it:

1. measures Euclidean distance to every training point;
2. sorts those points by distance;
3. takes the nearest `k` labels;
4. predicts by majority vote.

No backend or external model API is used.

## Dataset design

Training data contains deliberate label noise. Validation and final test data follow the clean underlying boundary. This is intentional: `k=1` can memorize the noise, while modest smoothing can recover the more general rule.

Current deterministic scores:

| k | Training | Validation | Final test |
|---|---:|---:|---:|
| 1 | 17/17 | 9/14 | 11/16 |
| 3 | 13/17 | 13/14 | 15/16 |
| 5 | 14/17 | 12/14 | 14/16 |
| 7 | 15/17 | 11/14 | 14/16 |
| 9 | 14/17 | 13/14 | 14/16 |

The game therefore rewards evidence rather than requiring one magic setting.

## Design rule preserved from earlier chapters

**Never teach the solution before the player has felt the problem.**

For this chapter, that means the words *overfitting* and *validation* arrive after the player has already been seduced by the training score.

## Playtest questions

- Did the 17/17 score feel trustworthy before validation opened?
- Did the validation result create surprise or merely confirm an expectation?
- Did lowering the training score feel wrong at first?
- Was it clear why the final batch could only be used once for an honest test?
- Did the lesson feel discovered rather than explained?

## Future chapter

A natural next lesson is dataset quality: a machine can faithfully learn a biased or corrupted world and still optimize exactly what it was asked to optimize.