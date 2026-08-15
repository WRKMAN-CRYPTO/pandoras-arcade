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

Current audio language:

- ball vertical position -> melody pitch
- ball horizontal position -> stereo position
- ball speed -> melodic pulse rate
- player paddle position -> the quiet center inside a soft harmonic field
- alignment -> harmonic stability versus roughness
- approach -> field presence increases as the interception matters more
- successful paddle contact -> musical resolution and continuation of the phrase
- miss -> an intentionally wrong PLINK that breaks the phrase
- recovery -> the coherent field returns and the player can find the groove again

Headphones are strongly recommended because stereo position carries horizontal state.

### Sound off

The same game runs without audio.

Current visual mapping:

- ball position -> direct geometry
- ball horizontal travel direction -> cyan/violet motion language
- ball speed -> trail length / wake
- vertical movement -> wave amplitude
- paddle impact -> side-localized screen hue pulse
- persistent score and serve/live state -> HUD

## Design law

**Same ball. Same paddle. Same timing. Same right to miss, learn, and get better.**

The alternate route must not replace the decision with an instruction such as "press now." It must expose enough state for the player to make the same interception decision.

## Gauntlet 1: information equivalence

The first implementation proved useful but exposed two immediate failures:

1. Hiding the playfield initially intercepted touch input, which changed the control model. The mask was corrected so sensory removal does not change player agency.
2. The eyes-closed route signaled point outcome but did not expose cumulative score, which hid match stakes from the audio route. Score-state audio was added.

That showed the skill could catch real cross-channel design errors.

## Gauntlet 2: perceptual fluency

Human testing of the first audio language exposed a deeper weakness: the sounds were individually informative but felt like separate labeled signals.

The player's paddle also occupied the same pitch language as the ball. That forced conscious comparison and caused the two signals to compete.

The second audio design changed the relationship:

- the ball remained the moving tonal center,
- the paddle stopped announcing itself with a competing center note,
- two quiet tonal rails formed a missing space around the paddle,
- the player could begin to place the moving ball into that perceptual opening,
- the field strengthened as the ball approached the player's side.

This exposed the distinction between **information equivalence** and **perceptual fluency**.

## Gauntlet 3: flow, error, and recovery

Human testing then identified a stronger target through a Guitar Hero analogy: when play is going well, the sensory language should flow. A mistake should feel immediately and musically wrong, and recovery should mean finding the flow again.

This pass treats the rally as one musical phrase rather than a collection of independent cues.

- the ball acts as a moving melodic voice,
- the paddle field provides harmonic context without duplicating the ball's pitch,
- alignment reduces beating and roughness,
- poor alignment destabilizes the field,
- a recurring low groove gives the rally temporal continuity,
- clean player contact resolves into a consonant continuation,
- consecutive clean contacts subtly strengthen that sense of continuity without changing gameplay,
- a missed ball triggers a deliberately dissonant PLINK and briefly collapses the field,
- the field then returns so recovery is perceptible as re-entering the phrase.

The target is no longer merely successful sensory decoding.

**The target is that good play starts to sound right before the player has to explain why.**

The miss should be felt as a break in coherence, and improvement should include learning how to preserve and recover that coherence.

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

For the eyes-closed route, add these stronger questions:

8. does the paddle feel like a place in the sound field rather than a second competing object,
9. can the player sense alignment without mentally naming two pitches,
10. does good positioning begin to sound more settled before contact,
11. does a miss feel wrong before the player consciously analyzes it,
12. can the player feel themselves recover the phrase after a mistake,
13. after practice, does the player want to keep playing specifically to become better at blind Pong?

Then compare the routes.

The important question is not whether scores are identical. It is whether the same mechanical decision, stakes, error, recovery, and opportunity for mastery survive.

## Known limitations

- Browser haptic support varies and is limited on iPhone, so haptics are supplemental rather than required.
- The eyes-closed route still uses synthesized Web Audio rather than authored sound assets.
- The current harmonic language is an experimental grammar, not a finished composition.
- The CPU opponent is intentionally simple and is not part of the perceptual-equivalence claim.
- Static implementation can validate architecture and mappings, but perceptual equivalence, fluency, and flow require human playtesting.

## Failure conditions

The experiment fails if:

- eyes-closed play becomes guessing,
- sound-off play loses actionable timing or direction,
- one route quietly receives easier physics,
- audio narrates the answer instead of exposing game state,
- multiple signals compete for the same perceptual territory,
- musical feedback becomes decorative and stops carrying mechanical truth,
- a miss sounds dramatic but does not communicate broken play,
- the player can decode the game but never develops instinctive flow,
- the combined route becomes noisier rather than richer,
- an alternate route feels like a stripped-down substitute rather than a complete game.

## Why this exists

The experiment is a test artifact for the `perceptual-equivalence` design skill.

Its purpose is to make that skill earn its place through a real playable implementation rather than through philosophy alone.
