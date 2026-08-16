# PONG//EQUIVALENT — Two-Tone Primitive

## Why this reset exists

After multiple richer auditory-language experiments, the next build deliberately removes almost all interpretation and tests the smallest possible relationship.

## Primitive

- Paddle vertical position produces one continuous sine tone.
- Ball vertical position produces the same sine tone through the same pitch map.
- Both tones are mono, equal-gain, and use the same timbre.
- When vertical positions match, the frequencies match and should perceptually fuse.
- When vertical positions differ, the split or beating between the tones should make mismatch obvious.

## Removed on purpose

This build removes:

- melodic contour
- projected-interception sonification
- dedicated speed sonification
- stereo ball-position encoding
- harmonic field
- groove
- audio collision cues
- audio score cues
- musical hit and miss flourishes

The game physics, paddle control, CPU, scoring, and visual geometry remain.

## Test question

**Can the player hear vertical mismatch and deliberately move until the two tones become one?**

If yes, this becomes the perceptual foundation. Future audio features must earn their place by adding useful game information without weakening this relationship.

If no, do not add complexity. Change only the primitive mapping or sound source until the relationship becomes intuitive.

## Design lesson

**Build outward from proven perception, not inward from imagined completeness.**
