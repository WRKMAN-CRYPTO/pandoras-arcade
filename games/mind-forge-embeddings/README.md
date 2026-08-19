# MIND//FORGE 0.7 · WORDS BECOME PLACES

## Purpose

Teach the idea of an **embedding** by letting the player watch words acquire learned coordinates from relationships.

The chapter begins with arbitrary 2D positions. Training optimizes those positions so related word pairs are pulled toward a small target distance while unrelated-category pairs are pushed apart by a margin. The result is a learned geometric representation.

This is intentionally **not yet a language model** and it is not presented as word2vec. It is a small metric-learning system designed to expose the core idea that symbolic items can become vectors whose relative positions carry useful structure.

## Vocabulary

Sixteen words are used across four intentionally legible semantic neighborhoods:

- royal: KING, QUEEN, PRINCE, PRINCESS
- animals: DOG, CAT, WOLF, FOX
- fruit: APPLE, PEAR, BANANA, ORANGE
- tools: HAMMER, WRENCH, SAW, DRILL

The category colors are visible to the player because the teaching question is not whether the human can discover the categories. The question is whether the machine can learn a geometry consistent with the supplied relationships.

## Training objective

Each word has a trainable vector:

`e(word) = [x, y]`

For a supplied related pair `(a, b)`, the loss encourages a small nonzero target distance `t`:

`L_positive = 0.5 * (||e(a)-e(b)|| - t)^2`

For unrelated pairs closer than margin `m`, a hinge-style repulsion applies:

`L_negative = 0.5 * weight * (m - ||e(a)-e(b)||)^2`

The browser performs direct gradient descent on the coordinates. Positions are recentered after each step so the whole map does not drift away from the viewport.

## Withheld-relation test

Eight within-neighborhood pairs are deliberately removed from the positive training evidence:

- KING ↔ PRINCESS
- QUEEN ↔ PRINCE
- DOG ↔ FOX
- CAT ↔ WOLF
- APPLE ↔ ORANGE
- PEAR ↔ BANANA
- HAMMER ↔ DRILL
- WRENCH ↔ SAW

The final inspection checks whether each withheld partner still ends closer than the nearest word from an unrelated neighborhood. This demonstrates that useful geometry can recover relationships indirectly through shared structure.

It does **not** establish human-like semantic understanding. The vocabulary and relationship graph are tiny and curated.

## Teaching sequence

1. Words begin at arbitrary coordinates.
2. The player trains the embedding and watches neighborhoods form.
3. Once the learned neighborhood score is strong, a tap-based inspector unlocks.
4. The player selects a word and sees its nearest neighbors by numeric distance.
5. Formal vocabulary appears only after the geometry has been experienced.
6. The final inspection evaluates relationships withheld from direct training.

## What to protect

- The words must visibly move during optimization.
- Distance must be calculated from the actual trained vectors.
- The inspector must report real nearest neighbors.
- The withheld pairs must remain absent from positive training evidence.
- The game must say clearly that this is an embedding lesson, not a full language model.
- No server, external API, account, analytics, or hidden pretrained model.

## Next conceptual door

A later chapter can replace hand-supplied relationship tickets with **context from sequences of text**, letting the player discover why words used in similar contexts can learn nearby representations. That creates the bridge from embeddings to next-token prediction and attention.