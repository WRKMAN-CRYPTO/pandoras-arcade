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

- ball vertical position -> transposes a recurring four-note melodic contour inside a compact mid-high register
- ball horizontal position -> stereo position
- projected interception error -> bends the contour away from or back toward its home shape
- player paddle position -> the quiet center inside a soft harmonic field using the same perceptually strong register
- predicted interception alignment -> harmonic stability versus roughness
- time-to-contact -> very small phrase tightening near the player
- successful paddle contact -> completes and resets the phrase into consonant resolution
- miss -> an intentionally wrong PLINK inside the same audible register
- recovery -> the familiar home contour returns

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

This tuning pass changed only the auditory interpretation:

- the moving ball tone still represented the ball's current position,
- the harmonic field settled according to the ball's **projected vertical interception point** at the player's paddle,
- wall bounces were folded into that projection,
- harmonic roughness increased as the paddle moved away from the projected interception path,
- consonance increased as the paddle approached it,
- the field became more present as the ball approached,
- groove and ball voices were softened so the field had more perceptual room,
- clean contact resolution was extended slightly,
- the miss PLINK was sharpened and the field collapsed a little longer before recovery.

The tuning question was:

**Can the player learn to arrive at the interception point before the ball, rather than chase the ball tone after it?**

## Gauntlet 5: protect the attentional hierarchy

Human testing then found a more subtle failure: the repetition frequency carrying speed was more attention-grabbing than the projected-trajectory language.

That meant a secondary variable was stealing the foreground from the information needed to play well.

This pass removed speed from pulse cadence entirely and pushed it underneath trajectory.

The hierarchy became:

**trajectory first -> position inside trajectory -> speed as pressure**

## Gauntlet 6: speed ablation

The next human test asked a more fundamental question: **is an explicit speed cue necessary at all?**

The build removed dedicated speed sonification from the eyes-closed route while preserving actual velocity and its physical consequences.

The result was useful: the language became cleaner and did not collapse, but the player did not yet perceive speed strongly enough from event spacing alone. Human testing also reported that the body and mind were actively trying to adapt, and that the sounds were beginning to be remembered and replayed as nonverbal patterns rather than verbal labels.

That exposed a deeper hypothesis: perhaps the language should be memorable as a **shape**, not decoded as a collection of cues.

## Gauntlet 7: melodic home shape

This pass stopped treating the rally as a set of separately sonified variables and gave it a recurring melodic object.

A four-note contour acted as the phrase's **home shape**.

- the ball's vertical position transposed the whole phrase,
- stereo still carried horizontal position,
- signed projected-interception error bent the contour away from its home tuning,
- improved alignment let the contour return toward its familiar consonant shape,
- the harmonic field remained underneath as context rather than a second melody,
- time-to-contact only tightened phrase spacing slightly near interception rather than announcing raw speed,
- clean contact completed the phrase and reset its contour,
- a miss deliberately fractured the established expectation,
- recovery meant hearing the recognizable contour return.

The important design shift was:

**Do not ask the player to remember what every sound means. Give the nervous system one memorable shape and let game state deform it.**

Human testing exposed a new failure: the low and high portions of the phrase did not have comparable perceptual weight. Low frequencies barely registered compared with the higher material, so the phrase did not feel like one coherent object even when its mathematical relationships were correct.

## Gauntlet 8: palette reset

This pass backs up one layer. It does not add grammar. It repairs the instrument palette first.

The central hypothesis is:

**A sensory mapping is not equivalent merely because its mathematics are symmetrical. Its perceptual weight must also be usable.**

Changes:

- the playable melodic range is compressed upward into a compact mid-high band,
- the four-note home contour uses much smaller intervals so no note escapes into a weak register,
- the ball voice switches from pure sine to a brighter triangle tone for stronger presence,
- paddle-field rails stay close to the same register instead of relying on a low foundation,
- the groove no longer drops an octave below the paddle,
- hit, wall, miss, score, and recovery cues are rebuilt around the same audible band,
- no cue is allowed to depend on sub-bass or very low fundamentals,
- physics, controls, scoring, trajectory projection, and visual play remain unchanged.

The question is deliberately simpler than the last one:

**Do the sounds finally feel like members of the same family, with comparable authority in the ear?**

Only after that succeeds should the melodic grammar be judged again.

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

8. do low-versus-high notes now have comparable perceptual presence,
9. does the entire palette feel like one coherent family,
10. can the recurring contour become recognizable without one register disappearing,
11. can the player feel the contour bending without consciously decoding each note,
12. does good positioning make the phrase feel more like its remembered home shape,
13. can the player move ahead of the ball rather than chase its present pitch,
14. does near-contact tightening create urgency without stealing attention from trajectory,
15. does a clean hit feel like musical completion rather than a reward jingle,
16. does a miss feel structurally wrong because it violates an established expectation,
17. does recovery feel like getting a known phrase back,
18. after practice, can the player hum or internally replay the sensory grammar,
19. after practice, does the player want to keep playing specifically to become better at blind Pong?

Then compare the routes.

The important question is not whether scores are identical. It is whether the same mechanical decision, stakes, error, recovery, and opportunity for mastery survive.

## Known limitations

- Browser haptic support varies and is limited on iPhone, so haptics are supplemental rather than required.
- The eyes-closed route still uses synthesized Web Audio rather than authored sound assets.
- The four-note contour is an experimental grammar, not a finished composition.
- The compact register is tuned from one human playtester's report and is not a universal hearing profile.
- The CPU opponent is intentionally simple and is not part of the perceptual-equivalence claim.
- The current build has been shaped through one human test loop; equivalence for blind players cannot be claimed without testing with people who actually rely on nonvisual play.
- Static implementation can validate architecture and mappings, but perceptual equivalence, fluency, memory, and mastery require human playtesting.

## Failure conditions

The experiment fails if:

- eyes-closed play becomes guessing,
- sound-off play loses actionable timing or direction,
- one route quietly receives easier physics,
- audio narrates the answer instead of exposing game state,
- the melodic contour becomes decorative music unrelated to mechanics,
- important notes have radically unequal perceptual weight,
- the player memorizes a tune but cannot use its deformation to play,
- time-to-contact tightening becomes another foreground speed cue,
- multiple signals compete for the same perceptual territory,
- projected-interception harmony makes the correct action trivially automatic rather than learnable,
- a miss sounds dramatic but does not communicate broken play,
- the player can decode the game but never develops instinctive flow,
- the combined route becomes noisier rather than richer,
- an alternate route feels like a stripped-down substitute rather than a complete game.

## Why this exists

The experiment is a test artifact for the `perceptual-equivalence` design skill.

Its purpose is to make that skill earn its place through a real playable implementation rather than through philosophy alone.
