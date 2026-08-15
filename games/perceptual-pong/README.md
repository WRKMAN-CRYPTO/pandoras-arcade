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
- ball speed -> pulse repetition rate
- player paddle vertical position -> the silent center between two soft tonal rails
- paddle field strength -> increases as the ball approaches the player's side
- paddle collision -> brief convergence / impact cue
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
| Ball vertical position | geometry / edge cue | ball pitch | — |
| Ball horizontal position | geometry | stereo pan | — |
| Ball speed | trail / wake length | pulse rate | — |
| Player paddle position | geometry | silent spectral center between two rails | — |
| Ball approaching player | geometry | paddle field becomes more present | — |
| Paddle impact | side-localized flash | convergence / impact cue | short pulse where supported |
| Wall impact | geometry | positional wall tone | short pulse where supported |
| Score / miss | score state | rising/falling sequence | distinct pulse where supported |

## Gauntlet 1: information equivalence

The first implementation proved useful but exposed two immediate failures:

1. Hiding the playfield initially intercepted touch input, which changed the control model. The mask was corrected so sensory removal does not change player agency.
2. The eyes-closed route signaled point outcome but did not expose cumulative score, which hid match stakes from the audio route. Score-state audio was added.

That was enough to show the skill could catch real cross-channel design errors.

## Gauntlet 2: perceptual fluency

Human testing of the first audio language exposed a deeper weakness: the sounds were individually informative but felt like separate labeled signals.

The player's paddle also occupied the same pitch language as the ball. That forced conscious comparison and caused the two signals to compete.

The second audio design changes the relationship:

- the ball remains the moving tonal center,
- the paddle no longer announces its center with another competing note,
- two quiet tones sit above and below the paddle's mapped center,
- the paddle itself is represented by the **missing space between them**,
- the player tries to place the moving ball tone inside that gap,
- the paddle field becomes more audible as the ball approaches the player's side and recedes when the immediate interception decision matters less.

The goal is no longer merely "can the player decode the signals?"

The stronger test is:

**Can the player stop consciously decoding them and begin to feel alignment, approach, interception, and miss as one learned auditory relationship?**

This is a distinction between **information equivalence** and **perceptual fluency**.

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

For the eyes-closed route, add three stronger questions:

8. does the paddle feel like a place in the sound field rather than a second competing object,
9. can the player sense alignment without mentally naming two pitches,
10. after practice, does interception begin to feel anticipatory rather than decoded?

Then compare the routes.

The important question is not whether scores are identical. It is whether the same mechanical decision, stakes, and opportunity for mastery survive.

## Known limitations

- Browser haptic support varies and is limited on iPhone, so haptics are supplemental rather than required.
- The current eyes-closed route uses synthesized Web Audio rather than authored sound assets.
- The CPU opponent is intentionally simple and is not part of the perceptual-equivalence claim.
- Static implementation can validate architecture and mappings, but perceptual equivalence and perceptual fluency require human playtesting.

## Failure conditions

The experiment fails if:

- eyes-closed play becomes guessing,
- sound-off play loses actionable timing or direction,
- one route quietly receives easier physics,
- audio narrates the answer instead of exposing game state,
- multiple sound signals compete for the same perceptual territory,
- the combined route becomes noisier rather than richer,
- players can function but cannot develop mastery,
- an alternate route feels like a stripped-down substitute rather than a complete game.

## Why this exists

The experiment is a test artifact for the `perceptual-equivalence` design skill.

Its purpose is to make that skill earn its place through a real playable implementation rather than through philosophy alone.
