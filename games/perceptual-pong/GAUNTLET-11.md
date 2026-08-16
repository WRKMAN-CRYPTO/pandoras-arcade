# Gauntlet 11: alternating pitch comparison

Human testing of the two-tone continuous primitive suggested the core vertical mapping was beginning to become audible, but simultaneous continuous tones could be harder to compare cleanly.

This pass changes only the presentation of that primitive.

- paddle vertical position -> short sine beep A
- ball vertical position -> short sine beep B
- both use the exact same pitch map, timbre, gain, and envelope
- A and B alternate at a fixed cadence
- the beeps do not overlap
- no stereo, speed, trajectory projection, melody, harmony field, groove, collision cue, or score cue is added
- game physics and controls remain unchanged

The intended perceptual task is simple: compare A with B and move the paddle until the two pitches sound the same.

## Test question

**Does alternating paddle/ball pitch make vertical mismatch easier to hear and deliberately correct than simultaneous continuous tones?**

If this primitive works, future audio layers must preserve its clarity and earn their place one at a time.
