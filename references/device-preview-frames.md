# Device Preview Frames and Bezels

Use this reference whenever producing a phone UX requirement, wireframe, high-fidelity mockup, generated visual, clickable prototype, or developer handoff.

## Default

Unless the current request specifies another device, state, orientation, or frame:

- Target **Pura X Max, unfolded portrait**.
- Use a preview canvas of **1828 x 2584 px**.
- Use a logical layout canvas of **665 x 940 vp**.
- Overlay `assets/device-bezels/pura-x-max-unfolded-portrait.png` as the standard bezel.
- When a default home screen is required, use `assets/default-homescreens/pura-x-max-unfolded-portrait.png` as the exact visual master.

Include the corresponding bezel in every visual UX output that shows a phone. Apply it to every phone screen in a single-screen mockup, multi-step flow, comparison, keyframe set, generated image, presentation visual, or prototype preview. Do not omit it merely to simplify the composition. Omit it only when the user explicitly requests a bezel-free, screen-only, raw-canvas, or implementation-only asset.

The portrait dimensions are the rotated form of the core baseline's Pura X Max unfolded entry: 2584 x 1828 px and 940 x 665 vp.

This default is the **inner/unfolded portrait** presentation. When a request concerns the compact outer display, a fold/unfold transition, or another Pura X Max-like screen ratio, also read [wide-foldable-pura-x-max.md](wide-foldable-pura-x-max.md) and apply its rules by screen role and fold state. Do not transfer outer-display status-bar, navigation-bar, or multi-window restrictions onto this unfolded portrait default.

## Device mapping

| Device and state | Preview pixels | Logical canvas | Standard bezel asset | Exact default home-screen master |
|---|---:|---:|---|---|
| Pura X Max, unfolded portrait | 1828 x 2584 px | 665 x 940 vp | `assets/device-bezels/pura-x-max-unfolded-portrait.png` | `assets/default-homescreens/pura-x-max-unfolded-portrait.png` |
| Pura X Max, unfolded landscape | 2584 x 1828 px | 940 x 665 vp | same asset, rotated 90 degrees clockwise; camera at upper-right | adapt the portrait master only when a landscape home state is explicitly required |
| Pura X View, front portrait | 1320 x 2232 px | 440 x 744 vp | `assets/device-bezels/pura-x-view-front.png` | `assets/default-homescreens/pura-x-view-front.png` |
| Pura 90 Pro Max, portrait | 1308 x 2880 px | 374 x 823 vp | `assets/device-bezels/pura-90-pro-max-portrait.png` | `assets/default-homescreens/pura-90-pro-max-portrait.png` |

The Pura X View dimensions are a user-supplied supplement. The Pura 90 Pro Max dimensions remain from the existing baseline.

The supplied home-screen PNGs are immutable visual masters. Read [home-screen-defaults.md](home-screen-defaults.md) before showing a launcher/home state. Preserve each master's aspect ratio and internal pixels/layout; create only a proportional screen-resolution copy when the mapped bezel workflow requires it.

### Pura X Max landscape orientation

- Start from `assets/device-bezels/pura-x-max-unfolded-portrait.png` and rotate that untouched source **90 degrees clockwise**. Because the portrait camera is at upper-left, this places the front-facing camera at the required **upper-right** in landscape.
- Rotation is the only permitted transform: do not mirror, resize, stretch, crop, redraw, or generatively recreate the bezel. Its rotated native canvas is the portrait asset's exact width/height swap.
- Render the application/system UI independently on the 2584 x 1828 px landscape screen canvas. Then derive the inner aperture and four-direction overscan from the rotated bezel alpha channel and composite the rotated bezel last.
- Never rotate a completed portrait phone composite or a portrait UI screenshot into landscape. Doing so rotates the UI, system chrome, antialiasing relationship, and navigation placement incorrectly.
- Re-run all eight-region seam diagnostics after rotation. Verify the camera remains upper-right and no duplicate camera cutout is added.

## Composition rules

1. Keep the app UI and official bezel as separate source layers. Render the app/system UI as a fully opaque screen image at the listed preview resolution and aspect ratio while specifying implementation geometry in vp and type in fp.
2. Treat the mapped official bezel PNG as the sole source of truth for its inner screen aperture, corner curve, antialiasing, camera position, frame/hinge details, colors, and transparency.
3. Never approximate the screen opening with a manually drawn rounded rectangle, guessed corner radius, generic device mask, or hard-coded geometry unless the bezel package explicitly provides those exact values.
4. Map the documented screen to the detected inner-aperture bounds with one proportional transform only. Do not stretch it. Do not shift, stretch, or rescale the visible UI to create seam coverage; preserve its screen-coordinate mapping.
5. Create hidden overscan by edge-pixel extrusion: extend the first visible row upward, last row downward, first column leftward, last column rightward, and each corner pixel diagonally into its hidden corner area.
6. Read the official bezel alpha channel and calculate upper, bottom, left, and right overscan independently. Cover the complete antialias transition on each side plus a small data-derived safety margin beneath the opaque lip. Do not use one universal hard-coded bleed value for every asset.
7. For every partially or fully transparent pixel in the center-connected inner aperture, require fully opaque screen content underneath. Allow the overscan beneath opaque and partially transparent inner-lip pixels.
8. Separate the center-connected inner-screen aperture from border-connected exterior transparency using connected-region analysis or an equivalent alpha-aware method. Clip screen content out of the exterior component so the official outer-device transparency is preserved.
9. Place the official bezel above the app-screen layer as the final layer at the bezel PNG's native pixel dimensions. Do not resize, stretch, crop, mirror, recolor, redraw, retouch, substitute, or generatively recreate it. Do not resize the completed composite after applying the bezel. For Pura X Max unfolded landscape only, apply the specified 90-degree clockwise rotation to the untouched bezel before all alpha analysis and compositing.
10. Do not add a second camera cutout or generic round-dot camera when the mapped bezel already contains one.
11. If the request explicitly names a different device or supplies a project-locked official frame, follow that instruction instead and document the override; apply the same native-size, alpha-geometry, directional overscan, extrusion, and verification requirements to that frame.
12. When the system navigation indicator is visible, calculate it in the logical screen layer from [navigation-bar-geometry.md](navigation-bar-geometry.md). Map its 6 vp bottom-edge gap to the bezel-derived visible bottom of the center-connected aperture before the bezel is applied; never position it from the outer PNG canvas edge.

## Deterministic helper

Use `scripts/composite_validate_bezel.py` for raster phone outputs. Example:

```bash
python scripts/composite_validate_bezel.py \
  --device pura-x-max-unfolded-portrait \
  --screen screen.png \
  --output device-composite.png \
  --report bezel-validation.json \
  --diagnostics-dir bezel-diagnostics
```

For Pura X Max unfolded landscape, pass `--device pura-x-max-unfolded-landscape`; the helper rotates the official source bezel 90 degrees clockwise before deriving its aperture.

The helper requires Pillow, NumPy, and SciPy. It rejects a source screen that is not exactly the mapped documented resolution or is not fully opaque. It identifies the center-connected aperture and border-connected exterior component from alpha, calculates each directional overscan independently, performs edge/corner extrusion without moving the visible UI, clips exterior leakage, composites the native bezel last, and reports pass/fail results for eight regions.

Do not treat a successful script result as a replacement for the contrasting-background visual inspection below. Preserve the generated JSON report and diagnostic sheets with the handoff evidence.

## Mandatory bezel seam verification

Perform this check on every rendered phone, including high-fidelity mockups, wireframes, screen flows, keyframes, presentation visuals, generated images, and prototype previews:

1. Inspect at 400% zoom or through an equivalent pixel-level comparison on white, black, and a saturated diagnostic background.
2. Verify the complete upper, bottom, left, and right inner edges independently; inspect all four corners and every transition between a straight edge and its corner curve.
3. Confirm there is no white or background-colored seam, transparent gap, one-pixel hairline, exposed mask boundary, incorrect curve, missing-underlay dark/light halo, edge/corner discontinuity, or screen content outside the device.
4. Run the automated alpha check for every center-connected inner-aperture pixel where official-bezel alpha is below full opacity: `underlying_screen_alpha == 255`.
5. Record uncovered-pixel counts for upper edge, bottom edge, left edge, right edge, upper-left corner, upper-right corner, bottom-left corner, and bottom-right corner. Every count must be zero.
6. Confirm the screen remains continuously flush with the antialiased inner boundary, exterior transparency matches the official silhouette, no screen content enters the exterior transparent component, and official bezel pixels/proportions remain unchanged.
7. Reject the output if any area fails. Re-composite from the untouched app-screen layer and official bezel; do not retouch an individual edge/corner or repair it generatively.

Observable acceptance criterion:

> The active screen continuously meets the official bezel’s antialiased inner boundary across the complete upper, bottom, left, and right edges and all four corners. Every partially or fully transparent inner-aperture pixel has opaque screen content beneath it, every directional uncovered-pixel count is zero, and no screen content leaks outside the official device silhouette.

## Delivery check

- Confirm that the device name, fold state, and orientation match the selected bezel.
- For Pura X Max unfolded landscape, confirm the official source bezel was rotated exactly 90 degrees clockwise, the front-facing camera is upper-right, and the UI was recomposited in landscape rather than rotating a finished portrait phone.
- Confirm that every displayed phone screen includes its corresponding bezel unless the user explicitly requested an allowed bezel-free output.
- For a mapped default home screen, confirm that the correct exact visual master was used without crop, redesign, regeneration, or internal reflow.
- Confirm that the source screen is fully opaque at the documented resolution/aspect ratio and is not stretched to the bezel asset's outer aspect ratio.
- Confirm that no content is obscured by the camera, rounded corners, hinge, frame, or gesture/system safe areas.
- When navigation is visible, confirm its logical geometry passes [navigation-bar-geometry.md](navigation-bar-geometry.md) and remains fully visible above the bezel's bottom inner lip.
- Confirm that the separate screen layer preserves its visible coordinates and uses independently calculated upper/bottom/left/right edge-pixel extrusion plus diagonal corner extrusion beneath every inner lip.
- Confirm that the aperture/exterior separation comes from the bezel alpha channel, every eight-region uncovered-pixel count is zero, and exterior leakage/mismatch counts are zero.
- Confirm that mandatory 400% inspection on white, black, and saturated backgrounds passes across the complete four edges, four corners, and edge/corner transitions, and that the observable acceptance criterion above is met.
- Include the selected preview-pixel size, logical vp canvas, and bezel filename in developer handoff.
- For a wide-foldable flow, label each frame's screen role and fold state so outer-display rules cannot be mistaken for unfolded-inner rules.
