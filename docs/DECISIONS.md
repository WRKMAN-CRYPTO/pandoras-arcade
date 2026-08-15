# Pandora's Arcade — Decisions

This file records small, durable architectural and maintenance decisions so future work can understand not only what exists, but why.

## 2026-08-14 — Preserve the static, mobile-first arcade architecture

### Decision

Keep Pandora's Arcade as a static, mobile-first browser arcade. Continue treating each cabinet as an intentionally small, mostly self-contained experience under its own path rather than introducing a framework, backend, account system, or shared application architecture without a demonstrated need.

### Why

The current structure is simple to understand, easy to deploy, and cheap to extend. A new cabinet can exist as its own small browser game without forcing unrelated games to share state, dependencies, or release machinery.

The architecture should only become more complex when repeated, real requirements make that complexity earn its place.

### Reliability pass

A narrow reliability pass was merged in PR #1 (`Builder Material reliability pass`). It made three changes:

1. **Rebel Reins polished module-load failures are now visible.** The previous loader swallowed module errors with an empty `catch`, which could make a broken load look like an unexplained game failure. The wrapper now logs the error and shows a visible failure state.
2. **The polished Rebel Reins wrapper no longer hard-codes `/pandoras-arcade/` into module URLs.** Modules are resolved relative to the wrapper URL, reducing coupling to the current GitHub Pages repository path.
3. **GitHub Pages now performs minimal static smoke checks before deployment.** The checks verify required arcade/WIP/Rebel Reins files, reject reintroduction of the hard-coded deployment path, and confirm that cabinet targets referenced by the homepage exist.

### Why these changes

They address observed reliability risks without changing the character of the project:

- silent failure made diagnosis difficult,
- hard-coded hosting paths made deployment location part of application behavior,
- direct deployment from `main` had no basic structural verification.

The fixes were intentionally small. They add visibility and guardrails without adding a framework, service, backend, monitoring platform, or build system.

### Explicitly not changed

- game design
- game content
- gameplay rules
- cabinet architecture
- static hosting model
- mobile-first direction
- backend or database
- accounts or identity
- framework adoption

### Maintenance rule

Prefer the smallest safeguard that makes a real failure visible, local, and recoverable. Do not generalize Pandora into a platform merely because it contains multiple games. Extract shared infrastructure only after repeated use proves that duplication has become the larger cost.
