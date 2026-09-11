# Live View Sketch Geometry and Placement

Use this reference whenever a deliverable contains 实况窗/Live View card, status-bar capsule, expanded capsule, or compact circular outer-display treatment. It supplements the frozen Live View guide; it does not replace the eligibility, lifecycle, privacy, interaction, text-limit, or color rules in the guide. For an expanded phone card, [expanded-live-view-card.md](expanded-live-view-card.md) supersedes conflicting geometry, placement, radius, material, and local-region values below.

## Source and measurement rules

- Source: user-supplied `HarmonyOS 实况通知样式模板0411.sketch`, added 2026-09-10.
- Source SHA-256: `4f97e57d8a705f98bd081bb6504048829a499aa4d8687704a6b9de3bbaae169e`.
- The Sketch document uses a design-unit grid. The capsule annotation labels its 80-unit width as `80dp`; the linked HarmonyOS guide expresses component geometry in vp. Preserve the template geometry in design specifications and use the system Live View API/component in production rather than hard-coding raster coordinates.
- Coordinates below are local to the component, with `(0,0)` at its upper-left. The documentation-artboard coordinates are not device placement values.
- Preserve the existing baseline when this older editable template differs from the current guide. In particular, its brand-color capsule examples are illustrative; the current guide remains authoritative for system-provided capsule color, text color, eligibility, and behavior.

## Live View card geometry

When the extension region is absent, use the unaffected `336 x 72 vp` base/collapsed-card frame with `16 vp` corner radius. Do not leave an empty lower half.

For every expanded phone card, do **not** use a fixed outer size or the Sketch's resolved fixed-region coordinates. Read [expanded-live-view-card.md](expanded-live-view-card.md) and calculate:

```text
card = (16, 50, W-32, (W-32)x6/17) vp
radius = 20 vp
```

The expanded phone card retains the established 12 vp horizontal inset, icon/text anchors, optional 44 x 44 vp auxiliary region, and extension templates, but derives all right-aligned widths and x-coordinates from the calculated card width.

For the unaffected base/collapsed card only, the older Sketch simulates material as white at 60% opacity in Light or black at 82% opacity in Dark, with backdrop blur 50, saturation 2x, and radius 16. Never apply those fill/radius values to an expanded phone card. Expanded phone cards use the Pura X View treatment: blurred underlay, 48% neutral dark overlay, 25% neutral perimeter outline, and 20 vp radius.

## Status-bar capsule geometry

### Default state

- Outer frame: `80 x 28`; Sketch fixed corner radius: `16`.
- Source-icon slot: `24 x 24` at `(2,2)`.
- Visible icon artwork: `18 x 18` at `(5,5)`, centered in the slot.
- First text slot: `45 x 16` at `(29,6)`.
- The measured gap from the icon artwork's right edge to the text slot is `6`; the text slot ends `6` before the capsule's right edge.

### Expanded state

- Outer frame: `128 x 28`; Sketch fixed corner radius: `16`.
- Source-icon slot and first text slot remain at the same coordinates as the default state.
- Second text slot: `45 x 16` at `(80,6)`.
- Preserve the template's slot geometry; do not stretch the 80-unit default capsule to make the expanded state.

Capsule example text uses HarmonyHeiTi Medium at `14 fp`. Follow the current Live View guide's preferred content model: one or two concise segments, with main text typically 1–3 Chinese characters and secondary text 1–6.

## Capsule placement and state selection

- Treat the capsule as system-owned status-bar content. Do not place it by copying its `(79,1646)` or `(216,1646)` documentation-artboard coordinates.
- On a centered punch-hole device, align the capsule to the centered hardware opening so software and hardware read as one centered form.
- On a side-punch or no-hole device, place the system capsule at the left side of the status bar.
- Keep it clear of time, connectivity, and battery elements. Preserve the system's coexistence, compression, and collision behavior rather than manually overlapping fixed status content.
- Use the `80 x 28` default state on ordinary portrait phones.
- Use the `128 x 28` expanded state only when the actual status-bar host provides sufficient horizontal space; the Sketch names landscape, foldables, and tablets as examples. Device class alone is not permission to overlap a cutout or fixed status items.
- Do not blindly apply the generic “phone landscape temporarily hides the status bar” rule to a required Live View state. Resolve whether the system is presenting Live View in that state; if it is, use the system-owned host and the expanded geometry only when the available status-bar space is verified.
- Tapping a single capsule opens its floating Live View card and removes the capsule while the card is open. Do not show both forms for the same activity in the same context.

## Compact circular outer-display treatment

For the source's `小外屏圆形适配` template:

- design canvas/mask: `224 x 224` circle;
- standard content example: source icon `36 x 36` at `(94,23)`, title block `72 x 32` at `(76,77)`, first detail row at `(78,119)`, and second detail row at `(59,146)`;
- supplied alternate template: `226 x 226`; source icon `36 x 36` at `(95,24)`, title at `(77,68)`, detail rows at `(78,108)` and `(60,133)`;
- expect illustration cropping to vary across outer-display sizes. Keep important illustration content within the visible circular safe region and verify on the actual device mask; never scale or distort text/icons merely to preserve a decorative crop.

Do not transfer the circular outer-display layout to an unfolded rectangular inner display.

## Mandatory verification

For every Live View visual or prototype state:

- identify the exact form: `336 x 72 vp` base/collapsed card, responsive expanded phone card, `80 x 28 vp` default capsule, `128 x 28 vp` expanded capsule, lock-screen form, or circular outer-display treatment;
- for an expanded phone card, verify its complete responsive frame, regions, 20 vp radius, and material against [expanded-live-view-card.md](expanded-live-view-card.md); for other forms, verify geometry against this reference;
- verify capsule device placement against the actual camera/cutout and status-bar fixed content, not the documentation artboard;
- verify the default/expanded capsule choice from measured available status-bar width;
- verify capsule and card are not simultaneously shown for the same activity in one context;
- verify the current core guide still controls eligibility, text limits, color behavior, lifecycle, privacy, and interaction;
- reject any implementation that approximates these system-owned forms with a generic notification, generic pill, Dynamic Island imitation, or manually guessed placement.

Observable acceptance criterion: “The selected Live View form matches its controlling source; an expanded phone card uses the responsive Pura X View-derived rules, other forms retain their valid Sketch geometry, local regions and content anchors remain within bounds, the capsule aligns to the actual cutout/status-bar host without colliding with fixed status content, and only the context-appropriate form is visible.”
