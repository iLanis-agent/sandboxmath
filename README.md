# Sandbox math

Backyard sandbox planning arithmetic: the box names the sand, the perimeter names the boards, and the overhang names the cover.

Live at https://ilanis-agent.github.io/sandboxmath/

## The three tools

- **Sand plan** - liters = length x width x fill depth in cm x 10; bags = ceil(liters / labeled 25 L), with top-up, weekend-build and truckload bands.
- **Frame plan** - perimeter = 2 x (length + width); boards = ceil(perimeter / labeled 2.4 m), plus 4 corner posts, with step-in, sit-in and kingdom bands.
- **Cover plan** - cover = box + labeled 0.25 m overhang each side; strips = ceil(cover width / labeled 2 m fabric), with picnic-rug, real-tarp and small-sail bands.

## Formulas and limits

- Volumes, perimeters and areas are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: bag size, board length, overhang, fabric width.
- Illustrative planning arithmetic only. Measure your own materials and read the supplier's bag before you buy; this is not a materials list.

## Development

- `engine.js` - calculation and render engine (browser global `SandboxMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
