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
- ball speed -> subtle pressure inside the existing phrase, not pulse frequency
- player paddle position -> the quiet center inside a soft harmonic field
- predicted interception alignment -> harmonic stability versus roughness
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

This pass treated the rally as one musical phrase rather than a collection of independent cues.

- the ball acts as a moving melodic voice,
- the paddle field provides harmonic context without duplicating the ball's pitch,
- alignment reduces beating and roughness,
- poor alignment destabilizes the field,
- a recurring low groove gives the rally temporal continuity,
- clean player contact resolves into a consonant continuation,
- consecutive clean contacts subtly strengthen that sense of continuity without changing gameplay,
- a missed ball triggers a deliberately dissonant PLINK and briefly collapses the field,
- the field then returns so recovery is perceptible as re-entering the phrase.

The target became:

**Good play should start to sound right before the player has to explain why.**

## Gauntlet 4: tuning for anticipation

The next human test reported that the language was forming, but remained early. The correct response was tuning rather than adding more systems.

A key weakness in the previous implementation was that harmonic alignment compared the paddle against the ball's **current** vertical position. That could encourage the player to chase the moving tone instead of learning interception.

This tuning pass changes only the auditory interpretation:

- the moving ball tone still represents the ball's current position,
- the harmonic field now settles according to the ball's **projected vertical interception point** at the player's paddle,
- wall bounces are folded into that projection,
- harmonic roughness increases as the paddle moves away from the projected interception path,
- consonance increases as the paddle approaches it,
- the field becomes more present as the ball approaches,
- groove and ball voices were softened so the field has more perceptual room,
- clean contact resolution was extended slightly,
- the miss PLINK was sharpened and the field collapses a little longer before recovery.

This does not choose the action for the player. It exposes trajectory through another perceptual language, analogous to seeing where a visible ball is headed.

The tuning question is:

**Can the player learn to arrive at the interception point before the ball, rather than chase the ball tone after it?**

## Gauntlet 5: protect the attentional hierarchy

Human testing then found a more subtle failure: the repetition frequency carrying speed was more attention-grabbing than the projected-trajectory language.

That meant a secondary variable was stealing the foreground from the information needed to play well.

This pass removes speed from pulse cadence entirely:

- ball and groove pulse rates are now stable rather than speeding up with velocity,
- trajectory and projected interception remain the dominant changing structure,
- speed now produces only a small change in note duration, gain, and field pressure,
- speed therefore changes the felt urgency of the same phrase without becoming a separately countable signal.

The hierarchy is now intentional:

**trajectory first -> position inside trajectory -> speed as pressure**

The tuning question is:

**Can the player notice that the rally is faster without having attention pulled away from where the ball will arrive?**

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
11. can the player move ahead of the ball rather than chase its present pitch,
12. does speed feel like pressure without becoming the thing attention follows,
13. does a miss feel wrong before the player consciously analyzes it,
14. can the player feel themselves recover the phrase after a mistake,
15. after practice, does the player want to keep playing specifically to become better at blind Pong?

Then compare the routes.

The important question is not whether scores are identical. It is whether the same mechanical decision, stakes, error, recovery, and opportunity for mastery survive.

## Known limitations

- Browser haptic support varies and is limited on iPhone, so haptics are supplemental rather than required.
- The eyes-closed route still uses synthesized Web Audio rather than authored sound assets.
- The current harmonic language is an experimental grammar, not a finished composition.
- The CPU opponent is intentionally simple and is not part of the perceptual-equivalence claim.
- Static implementation can validate architecture and mappings, but perceptual equivalence, fluency, flow, anticipation, and attentional hierarchy require human playtesting.

## Failure conditions

The experiment fails if:

- eyes-closed play becomes guessing,
- sound-off play loses actionable timing or direction,
- one route quietly receives easier physics,
- audio narrates the answer instead of exposing game state,
- multiple signals compete for the same perceptual territory,
- a secondary variable such as speed steals attention from trajectory,
- musical feedback becomes decorative and stops carrying mechanical truth,
- projected-interception harmony makes the correct action trivially automatic rather than learnable,
- a miss sounds dramatic but does not communicate broken play,
- the player can decode the game but never develops instinctive flow,
- the combined route becomes noisier rather than richer,
- an alternate route feels like a stripped-down substitute rather than a complete game.

## Why this exists

The experiment is a test artifact for the `perceptual-equivalence` design skill.

Its purpose is to make that skill earn its place through a real playable implementation rather than through philosophy alone.
