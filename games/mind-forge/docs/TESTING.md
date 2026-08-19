# MIND//FORGE 0.1 Test Plan

## Functional smoke test

- Page loads on a phone-sized viewport.
- Mass and heat sliders move the decision boundary immediately.
- Bias remains locked until Contract 3.
- Test Machine reports correct classifications and outlines misses.
- Tapping a stone updates Inspect Machine values.
- Completing a contract advances exactly once.
- Training controls appear only when intended.
- Train 1 Step changes real model parameters and generally changes loss.
- Let It Learn can be paused.
- Changing learning-rate preset changes the step size.
- Final inspection uses unseen data and does not enable parameter editing.
- Reload restores progress but does not resume automatic training.
- Restart Workshop clears saved progress.

## Learning validation

After completing 0.1, ask the player without showing the codex:

1. If the heat weight is zero, what information is the model ignoring?
2. If the boundary has the right angle but is in the wrong place, which parameter would you change?
3. What does the loss number tell you that raw accuracy may hide?
4. What is training actually doing to the machine?
5. If loss bounces wildly after every training step, what setting would you inspect first?
6. Why can the final unseen batch score differ from the training score?

The prototype has taught the intended concepts if the player can answer these in causal language, even if they do not remember every formal term.

## Usability test

Watch for:

- random knob-twiddling with no understanding of the boundary
- controls too small for one-thumb operation
- inspect panel becoming required rather than optional
- excessive text reading before the first meaningful action
- automatic training feeling magical because manual learning did not establish the analogy first
- final inspection feeling arbitrary rather than like a legitimate new-data test

## Scope test

If a proposed feature does not improve the player's understanding of prediction, weights, bias, loss, training, learning rate, or unseen evaluation, defer it beyond 0.1.
