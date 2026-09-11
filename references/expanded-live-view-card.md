# Expanded Phone Live View Card

Use this reference for every expanded 实况窗/Live View card on a phone. The user-supplied Pura X View full-canvas reference is authoritative for expanded phone-card geometry, placement, radius, material, opacity, and internal relationships. These rules supersede conflicting expanded-card values from the older Sketch template only.

Do not apply this reference to the `336 x 72 vp` base/collapsed card, status-bar capsules, compact circular outer-display layouts, lock-screen immersive cards, non-phone surfaces, or Live View eligibility, lifecycle, privacy, interaction, and text limits.

## Source and precedence

- Visual source: `assets/live-view/01-16952.jpg`, supplied 2026-09-11.
- Source SHA-256: `8ad9860ef6678ec2e22e05a0a27a14dac56e4c251858eaa32a1bb31cf29a2320`.
- Stored JPEG dimensions: `1211 x 2048 px`. It is a proportional delivery copy of the documented Pura X View `1320 x 2232 px` screen. Use the logical/raster formulas below, not the stored JPEG dimensions, for measurement.
- Treat the reference's wallpaper, app icons, card content, `12:09` time, and status indicators as contextual examples only. They do not override the skill's exact home-screen assets, default `08:08` time, status-cluster specification, navigation geometry, or bezel rules.
- When an older Live View reference gives a conflicting expanded phone-card size, placement, radius, fill opacity, outline, or fixed local coordinate, this reference controls.

## Responsive outer frame

Let `W` be the designated phone's complete visible logical canvas width in vp. Define:

```text
Cw = W - 32 vp
Ch = Cw x 6 / 17
card = (x=16, y=50, width=Cw, height=Ch) vp
cornerRadius = 20 vp
```

- Preserve the exact `17:6` width-to-height ratio.
- Keep the left and right margins at exactly `16 vp` and the top coordinate at exactly `50 vp`.
- Measure from the complete visible logical screen canvas, not the outer bezel canvas, status-bar bottom, camera cutout, documentation artboard, or a guessed screen mask.
- Calculate all logical values before conversion. Do not round `Cw`, `Ch`, or local-region values prematurely. Convert the complete frame to the designated raster canvas, then round each final pixel edge once to the nearest whole pixel.
- The official mapped bezel continues to define the visible aperture during final compositing. Keep the card inside that aperture and clear of status content, camera cutouts, and other system-owned regions. If the mandatory frame collides on a newly mapped device, reject the layout and request a device-specific override rather than silently moving or resizing it.

### Calculation checks

| Logical canvas width `W` | Card width `Cw` | Card height `Ch` |
|---:|---:|---:|
| `374 vp` | `342 vp` | `2052/17 vp` = `120.705882... vp` |
| `440 vp` | `408 vp` | `144 vp` |
| `665 vp` | `633 vp` | `3798/17 vp` = `223.411764... vp` |

These are calculation checks, not additional fixed component sizes. Never stretch or reuse a Pura X View `408 x 144 vp` or `1224 x 432 px` card on another phone.

### Pura X View result

For `440 x 744 vp` mapped to `1320 x 2232 px` at `3 px/vp`:

```text
logical frame = (16, 50, 408, 144) vp
raster frame  = (48, 150, 1224, 432) px
```

Treat this as the calculated Pura X View result only.

## Responsive local regions

Use component-local coordinates with `(0,0)` at the expanded card's upper-left:

```text
Fixed region:
(x=12, y=10, width=Cw-80, height=52) vp

Optional auxiliary region:
(x=Cw-56, y=14, width=44, height=44) vp

Extension region:
(x=12, y=72, width=Cw-24, height=Ch-84) vp
```

Retain these anchors and relationships:

- application icon: `32 x 32 vp` at `(12,20)`;
- primary text: starts at `x=56`; retain the established `y=14` top anchor when the content template permits;
- secondary text: starts at `x=56`; retain the established `y=40` top anchor when the content template permits;
- icon-to-text gap: `12 vp`;
- left and trailing card insets: `12 vp`;
- auxiliary region: right aligned by formula, never by a universal fixed x-coordinate.

For Pura X View, the formulas resolve to fixed region `(12,10,328,52)`, auxiliary region `(352,14,44,44)`, and extension region `(12,72,384,60)` vp. Do not copy those resolved values to another canvas.

If `Ch - 84` leaves less extension space on a narrower phone, simplify or remove optional extension content. Never clip text, icons, or progress, and never distort typography, icon geometry, or the outer aspect ratio.

## Material and opacity

- Blur the wallpaper or screen content beneath the expanded card. Retain the verified backdrop-blur value `50` from the older template when an explicit design-tool value is required; do not invent another blur-radius token.
- Apply a neutral dark overlay at exactly `48%` opacity.
- Add a thin neutral perimeter outline at exactly `25%` opacity. No numeric outline thickness is supplied; use the current system component or a visually thin perimeter without inventing a fixed token.
- Keep the outline subordinate to card content.
- Do not bake sampled red, pink, green, or other wallpaper-derived colors into the material. Let the underlying wallpaper affect the apparent surface naturally through translucency.
- Keep text, source icons, progress indicators, and semantic accent colors independent from the material opacity.
- Do not use the older expanded-card black-at-82% material or its 16 vp radius. The older values may remain only where explicitly scoped to the unaffected base/collapsed card.
- Do not infer a saturation adjustment for the expanded phone card from the older template; this source supplies no new saturation requirement.

## Deterministic calculation

Use `scripts/expanded_live_view_geometry.py` for every expanded phone card. Supply the logical canvas and, for raster output, the documented pixel canvas. The helper preserves exact logical fractions and rounds raster edges once.

```bash
python scripts/expanded_live_view_geometry.py \
  --width-vp 440 --height-vp 744 \
  --width-px 1320 --height-px 2232
```

## Mandatory verification

For every expanded phone Live View card, verify independently:

1. `cardWidth = W - 32 vp` and `cardHeight = cardWidth x 6 / 17`.
2. Card frame is `(16, 50, cardWidth, cardHeight) vp`, both side margins are 16 vp, aspect ratio is exactly 17:6, and radius is 20 vp.
3. Logical geometry was calculated without premature rounding; raster edges were converted and rounded once.
4. Fixed, optional auxiliary, and extension regions use the responsive formulas; no resolved x-coordinate or width from another phone was reused.
5. The surface blurs the actual content below it, uses a 48% neutral dark overlay and 25% neutral outline, and contains no wallpaper-sampled baked tint.
6. Text, icons, progress, and semantic accents remain independently legible and are not faded by the material opacity.
7. Optional extension content adapts without clipping or distortion.
8. The card stays inside the mapped aperture and does not collide with status content, the camera, or other system-owned regions.
9. The bezel, status bar, navigation indicator, base/collapsed card, capsules, circular outer-display form, and unrelated Live View rules remain unchanged.
10. No active rule requires a universal `336 x 144 vp` or `408 x 144 vp` expanded phone card, 16 vp expanded-card radius, fixed 312 vp extension width, fixed auxiliary x-coordinate, or black-at-82% expanded-card material.

Acceptance criterion:

> For a phone canvas with logical width `W`, the expanded Live Activity card occupies the frame `(16, 50, W-32, (W-32)x6/17) vp`. It preserves a 17:6 aspect ratio, 16 vp side margins, a 50 vp top coordinate, a fixed 20 vp corner radius, blurred underlying content, a 48% neutral dark overlay, and a 25% neutral outline. The `408 x 144 vp` frame is used only when the canvas width is 440 vp, and no contradictory fixed-size legacy specification remains active.
