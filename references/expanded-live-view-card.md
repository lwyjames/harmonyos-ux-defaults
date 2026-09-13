# Expanded Phone Live View Card

Use this reference for every expanded 实况窗/Live View card on a phone, regardless of the underlying application, wallpaper, content type, or Live View scenario. The user-supplied Pura X View full-canvas reference is authoritative for expanded phone-card geometry, placement, radius, material, opacity, and internal relationships. Two additional Pura X View screenshots supplied on 2026-09-12 clarify cross-application overlay, perceptual occlusion, and material-compositing behavior. These rules supersede conflicting expanded-card values from the older Sketch template only.

Do not apply this reference to the `336 x 72 vp` base/collapsed card, status-bar capsules, compact circular outer-display layouts, lock-screen immersive cards, non-phone surfaces, or Live View eligibility, lifecycle, privacy, interaction, and text limits.

## Source and precedence

- Visual source: `assets/live-view/01-16952.jpg`, supplied 2026-09-11.
- Source SHA-256: `8ad9860ef6678ec2e22e05a0a27a14dac56e4c251858eaa32a1bb31cf29a2320`.
- Stored JPEG dimensions: `1211 x 2048 px`. It is a proportional delivery copy of the documented Pura X View `1320 x 2232 px` screen. Use the logical/raster formulas below, not the stored JPEG dimensions, for measurement.
- Treat the reference's wallpaper, app icons, card content, `12:09` time, and status indicators as contextual examples only. They do not override the skill's exact home-screen assets, default `08:08` time, status-cluster specification, navigation geometry, or bezel rules.
- When an older Live View reference gives a conflicting expanded phone-card size, placement, radius, fill opacity, outline, or fixed local coordinate, this reference controls.
- Supplemental visual checks: two user-supplied Pura X View screenshots reviewed on 2026-09-12, one showing an expanded media Live View above a WeChat conversation and one showing an AI-generated match-queue comparison. They are not bundled as assets. Use them to verify general expanded-card stacking, effective visual density, and cross-device inference; their WeChat content is contextual rather than a scope limit.

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

## Cross-application overlay and occlusion

- Apply the same expanded-card stacking and material behavior over **every** eligible underlying scene: messaging, home screen, productivity, travel, media, game, delivery, ride-hailing, meeting, or another application. WeChat is one verification example, not a special-case trigger.
- Build the underlying app screen **first**, exactly as it would appear with no expanded Live View present. It must be a complete, valid standalone state with its normal app bar, first content block, scroll position, list/message anchors, and bottom controls.
- Freeze the complete app-owned layer before adding the card. Composite the expanded card last as a system-owned top overlay. Every app-owned element must retain identical logical coordinates, dimensions, order, and scroll position before and after the overlay: `deltaX=0`, `deltaY=0`, and no reflow.
- Never use `cardY`, `cardHeight`, `cardBottom`, or a derived card clearance as an input to the underlying app's layout, scroll offset, first-content position, safe-area padding, spacer, or list inset. Do not push, resize, or reflow the app bar, page title, tabs, toolbar, message list, or other underlying content to reserve space for the card.
- Keep the HarmonyOS status bar visible and authoritative. The expanded card occupies its required `y=50 vp` frame beneath the status region and visually occludes the app-owned top/title region that falls behind it.
- No underlying back control, title, badge, overflow action, tab label, icon, divider, or body text may peek around the card's covered title band or remain recognizable through the material. The app state may remain logically present underneath for continuity, but it must be perceptually occluded by the card's blur and full-strength material composition.
- Do not manufacture a clean empty band immediately below the card or start the first app content at `cardBottom + gap`. A first visible item may happen to appear below the card only when the base app's independently constructed coordinates prove that placement; covered earlier content remains in place beneath the card.
- For an established scrolling or messaging scene, retain at least one normally positioned earlier content element in the card footprint. The overlay may hide it completely or let only a naturally intersecting lower edge emerge below the card, but the content must not be deleted or relocated merely to make the card readable.
- Preserve base-layer evidence for mockups and handoffs: a card-free app frame, separate app/card layers, or an anchor table comparing key app coordinates before and after compositing. Reject delivery unless the comparison proves zero movement.
- These are logical layout and compositing rules. On every other phone model, calculate the card and underlying title relationship in vp from that device's documented canvas, convert once to its raster mapping, and verify the result inside its official bezel. Never copy the Pura X View screenshot's raster coordinates, crop, or physical pixel gaps.
- A scene-specific exception requires an explicit current-user instruction or a separately authoritative system rule. Do not weaken opacity, expose the underlying title bar, or reflow the app merely because the underlying app is not WeChat.

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

- Sample the **actual frozen app content at the card's final coordinates**, clip it to the card shape, and blur that underlay. Retain the verified backdrop-blur value `50` from the older template when an explicit design-tool value is required; do not invent another blur-radius token.
- For raster compositing, capture enough offscreen source padding for the blur kernel, blur that offscreen copy, crop it back to the exact card rectangle, and **apply the final 20 vp rounded alpha mask after the blur**. Composite the result only through that mask. Never blur an already-masked layer and let the kernel expand its alpha, and never apply blur/backdrop filters to the app root, page, screen, card parent, or final composite.
- Use this bottom-to-top compositing order: frozen app/wallpaper underlay -> clipped backdrop blur that preserves coarse hue and luminance -> neutral-dark overlay at `48%` -> thin neutral outline at `25%` -> independently rendered card content. Keep the root/card group at `100%` opacity.
- Backdrop blur removes spatial detail; it must not erase the underlay's broad color and luminance structure. A large saturated area beneath the card must remain perceptible as a softened local hue variation, while its text, avatar, icon, boundary, or control details become unrecognizable. Neutral underlay areas remain neutral.
- Apply a neutral dark overlay at exactly `48%` opacity.
- Keep the expanded-card root/container/compositing group at `100%` opacity. The `48%` value belongs only to the neutral-dark overlay layer above the blurred underlay; it is not the opacity of the complete card, its blur result, or its content group.
- Add a thin neutral perimeter outline at exactly `25%` opacity. No numeric outline thickness is supplied; use the current system component or a visually thin perimeter without inventing a fixed token.
- Keep the outline subordinate to card content.
- Do not bake sampled red, pink, green, or other wallpaper/app-derived colors into the material. Local tint must arise dynamically from the real underlay through the blur and translucency; never paint a decorative color gradient to imitate it.
- Do not add another uniform gray fill, extra neutral overlay, white haze/frost layer, global desaturation, color-replacement pass, or reduced parent-group opacity. Reject a nearly uniform gray card when the frozen underlay contains large high-contrast or saturated regions that should create visible local variation.
- Do not change the required `48%` neutral-dark overlay to make the underlay more visible. Correct missing color influence by fixing the underlay sample, layer order, clipping, or excessive color suppression.
- All blur, gray influence, and underlay-derived color must terminate at the rounded-card alpha boundary. Outside the rounded mask, the card-present app layer must remain the original sharp card-free pixels. Allow at most a one-raster-pixel antialias transition around the calculated boundary; reject blur bleed, global softening, exterior haze, bloom, glow, or a color plume beyond it.
- Default to **no external drop shadow** for the expanded phone card because none is numerically verified by this source. Add one only when a later authoritative source explicitly requires it; keep it as an independently composited, very tight alpha projection and never blur or resample the underlying app to produce it. A broad soft shadow, fog field, or ambient glow is invalid.
- Keep text, source icons, progress indicators, and semantic accent colors independent from the material opacity.
- The blurred underlay may influence the apparent hue, but recognizable underlying text, navigation controls, titles, icons, or dividers must not remain legible through the surface. Match the denser effective appearance of the verified expanded-card reference rather than producing a washed-out translucent panel.
- Do not use the older expanded-card black-at-82% material or its 16 vp radius. The older values may remain only where explicitly scoped to the unaffected base/collapsed card.
- Do not apply the older template's saturation adjustment to the expanded phone card. The required behavior is underlay-color preservation through the blur, not a fixed saturation multiplier.

## Deterministic calculation

Use `scripts/expanded_live_view_geometry.py` for every expanded phone card. Supply the logical canvas and, for raster output, the documented pixel canvas. The helper preserves exact logical fractions and rounds raster edges once.

For a raster mockup, preserve a card-free base frame and run `scripts/validate_live_view_blur_boundary.py` against the card-present frame. Supply the once-rounded raster card frame and 20 vp radius converted with the same documented device mapping. The default permits only a one-pixel antialias ring and requires zero changed pixels everywhere else outside the rounded mask.

```bash
python scripts/expanded_live_view_geometry.py \
  --width-vp 440 --height-vp 744 \
  --width-px 1320 --height-px 2232

python scripts/validate_live_view_blur_boundary.py \
  card-free.png card-present.png \
  --card-x-px 48 --card-y-px 150 \
  --card-width-px 1224 --card-height-px 432 \
  --radius-px 60
```

## Mandatory verification

For every expanded phone Live View card, verify independently:

1. `cardWidth = W - 32 vp` and `cardHeight = cardWidth x 6 / 17`.
2. Card frame is `(16, 50, cardWidth, cardHeight) vp`, both side margins are 16 vp, aspect ratio is exactly 17:6, and radius is 20 vp.
3. Logical geometry was calculated without premature rounding; raster edges were converted and rounded once.
4. Fixed, optional auxiliary, and extension regions use the responsive formulas; no resolved x-coordinate or width from another phone was reused.
5. The surface uses the actual frozen content below it and follows the required layer order: underlay -> clipped color-preserving blur -> 48% neutral-dark overlay -> 25% neutral outline -> full-strength content, with the root/card group at 100% opacity.
6. Large saturated or high-contrast underlay regions create perceptible softened local hue/luminance variation inside the card; neutral regions remain neutral. The result is not a uniform gray substitute, a baked decorative tint, or an extra desaturated/hazy treatment.
7. The required 48% overlay is unchanged. No second gray fill, extra neutral overlay, white haze, global desaturation, color replacement, or reduced parent opacity suppresses the underlay's broad color influence.
8. Text, icons, progress, and semantic accents remain independently legible and are not faded by the material opacity.
9. Underlying app titles, navigation controls, icons, text, avatars, boundaries, and dividers are not recognizable through the blurred material despite the retained broad color variation.
10. Blur was calculated on an offscreen copy and clipped with the final rounded mask after filtering. No blur or backdrop filter exists on the app/screen root, card parent, or completed composite.
11. A card-free/card-present raster comparison has identical canvas dimensions and reports zero changed pixels outside the rounded card plus the allowed one-pixel antialias ring. Every uncovered app element remains equally sharp.
12. No unverified broad drop shadow, haze, bloom, glow, or color plume crosses the card boundary. Any explicitly sourced shadow is an independent tight alpha layer and never results from blurring the app.
13. The card is above the underlying app without reflow; it preserves the HarmonyOS status bar while perceptually occluding the app-owned title region beneath it in every underlying-app scenario.
14. A card-free base frame or equivalent layer/anchor evidence proves every app-owned element has `deltaX=0` and `deltaY=0` after overlay compositing.
15. No app layout value depends on `cardY`, `cardHeight`, `cardBottom`, or a card-clearance spacer; no artificial empty band begins or ends at the card boundary.
16. In an established list, feed, or conversation, normally preceding content remains beneath the card rather than being deleted or moved below it.
17. Optional extension content adapts without clipping or distortion.
18. The card stays inside the mapped aperture and does not collide with status content, the camera, or other system-owned regions.
19. The bezel, status bar, navigation indicator, base/collapsed card, capsules, circular outer-display form, and unrelated Live View rules remain unchanged.
20. No active rule requires a universal `336 x 144 vp` or `408 x 144 vp` expanded phone card, 16 vp expanded-card radius, fixed 312 vp extension width, fixed auxiliary x-coordinate, or black-at-82% expanded-card material.

Acceptance criterion:

> For a phone canvas with logical width `W`, first build and freeze the normal card-free app state, then composite the expanded Live Activity card at `(16, 50, W-32, (W-32)x6/17) vp` without changing any app-owned coordinate or scroll position. It preserves a 17:6 aspect ratio, 16 vp side margins, a 50 vp top coordinate, a fixed 20 vp corner radius, and the ordered material stack: actual frozen underlay, color-preserving offscreen blur clipped after filtering, 48% neutral-dark overlay, 25% neutral outline, and full-strength content inside a 100%-opacity root group. Broad underlay hue/luminance variation remains perceptible but all underlying detail is unrecognizable. Blur, tint, gray influence, haze, and shadow do not escape the rounded boundary; outside the allowed one-pixel antialias ring, the card-present raster is pixel-identical to the sharp card-free app. Normally preceding content remains underneath rather than being moved to `cardBottom + gap`. The `408 x 144 vp` frame is used only when the canvas width is 440 vp, and no contradictory fixed-size, reflowing, flattened-gray, or blur-leaking legacy specification remains active.
