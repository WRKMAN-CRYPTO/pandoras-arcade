# PONG//EQUIVALENT

A small perceptual-equivalence experiment for Pandora's Arcade.

## Question

Can the same game remain mechanically intact, learnable, and satisfying when its important state is carried through different sensory routes?

The test deliberately keeps one physics model and one control model. The perceptual route changes. The game does not.

## Three routes

### Full senses

Visual, audio, and available haptic signals cooperate. The test is whether the channels complement rather than compete.

### Eyes closed

The playfield is intentionally hidden after play begins. The player controls the same paddle with the same vertical drag input.

Current audio mapping:

- ball vertical position -> pitch
- ball horizontal position -> stereo pan
- ball speed -> chirp repetition rate
- player paddle vertical position -> reference pulse pitch on the left
- paddle collision -> distinct impact cue
- wall collision -> positional pitch cue
- score / miss -> distinct directional sequence

Headphones are strongly recommended because stereo position carries horizontal state.

### Sound off

The same game runs without audio.

Current visual mapping:

- ball position -> direct geometry
- ball horizontal travel direction -> cyan/violet motion language
- ball speed -> trail length / wake
- vertical movement -> wave amplitude
- horizontal direction and vertical position -> edge direction cue
- paddle impact -> side-localized screen hue pulse
- persistent score and serve/live state -> HUD

## Design law

**Same ball. Same paddle. Same timing. Same right to miss, learn, and get better.**

The alternate route must not replace the decision with an instruction such as "press now." It must expose enough state for the player to make the same interception decision.

## Perceptual mapping

| Mechanical truth | Visual | Audio | Haptic |
| --- | --- | --- | --- |
| Ball vertical position | geometry / edge cue | continuous pitch mapping | — |
| Ball horizontal position | geometry | stereo pan | — |
| Ball speed | trail / wake length | chirp rate | — |
| Player paddle position | geometry | reference pitch pulse | — |
| Paddle impact | side-localized flash | impact + contact pitch | short pulse where supported |
| Wall impact | geometry | positional wall tone | short pulse where supported |
| Score / miss | score state | rising/falling sequence | distinct pulse where supported |

## Battle-test protocol

Do not judge only whether each route is technically playable.

For each route, test whether a player can:

1. orient to the ball,
2. predict where it is going,
3. move deliberately rather than guess,
4. distinguish contact from miss,
5. understand why a point was lost,
6. improve after several rallies,
7. build anticipation rather than merely react.

Then compare the routes.

The important question is not whether scores are identical. It is whether the same mechanical decision, stakes, and opportunity for mastery survive.

## Known limitations of this first experiment

- Browser haptic support varies and is limited on iPhone, so haptics are supplemental rather than required.
- The current eyes-closed route uses synthesized Web Audio rather than authored sound assets.
- The CPU opponent is intentionally simple and is not part of the perceptual-equivalence claim.
- This implementation has passed static code/syntax inspection, but perceptual equivalence itself requires human playtesting. It should not be declared proven from implementation alone.

## Failure conditions

The experiment fails if:

- eyes-closed play becomes guessing,
- sound-off play loses actionable timing or direction,
- one route quietly receives easier physics,
- audio narrates the answer instead of exposing game state,
- the combined route becomes noisier rather than richer,
- players can function but cannot develop mastery,
- an alternate route feels like a stripped-down substitute rather than a complete game.

## Why this exists

The experiment is a test artifact for the `perceptual-equivalence` design skill.

Its purpose is to make that skill earn its place through a real playable implementation rather than through philosophy alone.
