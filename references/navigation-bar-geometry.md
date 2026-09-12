# Navigation Bar Geometry and Placement

Use this reference whenever the HarmonyOS system navigation indicator is visible. It transcribes the corrected responsive geometry supplied by the user on 2026-09-10 and supersedes only the earlier fixed-pixel indicator geometry and placement.

## Coordinate system

- Let `W` and `H` be the current device screen-opening width and height in vp/dp. A split pane or app window does not redefine `W`; the system indicator remains anchored to the device screen. States without a system navigation indicator do not use this geometry.
- Define all indicator and interaction-region geometry in logical units first. Convert the final coordinates to raster pixels using the documented screen-to-pixel scale for the selected device.
- In a bezeled raster mockup, map logical screen `(0, 0, W, H)` to the mapped bezel's center-connected visible screen aperture. The bezel-derived visible screen bottom, not an occluded outer canvas row, is `H`.
- In a bezel-free screen-only canvas, the raw canvas bottom is the visible screen bottom.

## Visible indicator

The visible indicator is a horizontally centered capsule:

| Current logical screen width `W` | Indicator width |
|---|---:|
| `360 <= W < 600` | `112 vp` |
| `600 <= W <= 840` | `W / 3 - 48 vp` |
| `W > 840` | `W / 4 - 48 vp` |

- Height: `6 vp`.
- Bottom-edge gap: `6 vp` above the visible screen bottom.
- Frame: `x = (W - indicatorWidth) / 2`, `y = H - 12 vp`, `width = indicatorWidth`, `height = 6 vp`.
- The indicator centerline is therefore `9 vp` above the visible screen bottom.
- Use a capsule/pill with fully rounded ends. If the renderer requires an explicit radius, `3 vp` is the geometric half-height derived from the 6 vp capsule; it is not a separate source token.
- The newer 6 vp multi-device figure controls over the 5 vp legacy example shown alongside it.
- The 2026-09-10 geometry figures define no color or opacity value. The later user-approved light-app treatment below is a project convention inferred from a separate 2026-09-12 screenshot; keep the provenance distinct.

The corrected rules replace the earlier `1252 x 84 px` capsule, `42 px` radius, and `16 px` bottom offset. Never retain or scale those obsolete values.

## Visual treatment and translucency

For ordinary light application surfaces, use the 2026-09-12 screenshot-derived project default:

- Continue the app's bottom surface behind the navigation region instead of inserting an unrelated solid strip.
- When that substrate is a quiet near-white surface, render the system indicator as neutral black at approximately 8% opacity: `rgba(0, 0, 0, 0.08)`.
- The supplied flattened JPEG measured approximately `#F6F6F6` for the navigation substrate and `#E3E3E3` for the indicator. The alpha model reproduces that relationship within JPEG and antialiasing tolerance.
- Implement the indicator as a translucent neutral semantic layer, not as a universally baked `#E3E3E3` fill. This allows the app surface to remain visually continuous.
- Do not use an app accent, brand green, sampled wallpaper hue, outline, shadow, or separate capsule background.

The screenshot contains only a light, low-variance bottom surface. Therefore:

- `8%` black is a **project default inferred from the screenshot**, not a Huawei or WeChat official token and not a universal dark-mode value.
- On dark, colored, image, video, or high-variance backgrounds, do not reuse 8% black. Use the native system-owned indicator when available; otherwise select the neutral light/dark semantic foreground through system inversion/adaptation and verify that it remains visible while subordinate to app content.
- If the native HarmonyOS runtime supplies the indicator color/alpha, its rendered system output controls over this static-mockup approximation.
- For mockups, sample the actual local substrate under and around the indicator. Reject an indicator that disappears, becomes an opaque decorative bar, or creates an unrelated bottom band.

## Invisible interaction region

Keep the gesture interaction region separate from the visible indicator:

- Width: `35%` of `W`.
- Height: `28 vp`.
- Bottom anchoring: flush to the visible screen bottom.
- Frame: `x = 0.325W`, `y = H - 28 vp`, `width = 0.35W`, `height = 28 vp`.
- Do not draw a 28 vp-high capsule, scrim, or background solely to represent this region.
- App-owned fixed actions, final scroll content, bottom scrollbars, and modal actions must clear the interaction region when navigation is present. The 28 vp clearance concerns the interaction region, not the 6 vp visible indicator.

## Responsive and raster handling

- Apply the width rule from the current device screen-opening width after orientation, fold state, and screen-role resolution. Do not choose a formula from the device model name alone or from one split pane's width.
- Treat the source range as defined from `W = 360 vp` upward. For a narrower undocumented surface, use the native system component/insets or request a project-specific rule; do not extrapolate a fixed value.
- Preserve the logical UI coordinates when compositing beneath a bezel. The indicator is part of the screen layer and follows the same alpha-derived aperture mapping and hidden overscan workflow as the rest of the UI.
- Do not resize the finished bezeled composite. Perform any logical-to-raster conversion before final bezel compositing.
- Use `python scripts/navigation_bar_geometry.py --width-vp W --height-vp H` to calculate the logical frames. Add `--width-px` and `--height-px` to report raster coordinates for a documented screen canvas.

## Verification

For every state where the navigation indicator is visible:

1. Confirm exactly one indicator appears inside the screen opening.
2. Measure the logical height as 6 vp and the bottom-edge gap as 6 vp.
3. Recalculate the width from the current logical `W` and confirm horizontal centering.
4. Confirm the interaction region is independently centered, bottom-anchored, `0.35W` wide, and 28 vp high.
5. Confirm the visible indicator was not enlarged, shifted, stretched, or used as the interaction-region bound.
6. Confirm bottom content clears the 28 vp region and that hidden/absent navigation states do not retain wasted padding.
7. For a bezeled output, measure from the bezel-derived visible bottom of the center-connected aperture and confirm the full bar remains visible above the inner lip.
8. Reject any output that uses the superseded fixed-pixel geometry or chooses the wrong responsive width branch.
9. On an ordinary light app surface, confirm the background continues behind the navigation region and the indicator uses the neutral `rgba(0, 0, 0, 0.08)` project default; on other backgrounds, confirm semantic inversion/adaptation was used instead of blindly applying that light-surface alpha.

Acceptance criterion:

> The visible navigation indicator is a centered 6 vp-high capsule whose bottom edge is 6 vp above the visible screen bottom, whose width matches the current logical-width formula, and whose separate invisible interaction region is centered, bottom-anchored, 35% of screen width, and 28 vp high. Its neutral translucent appearance integrates with the local app surface: use the 8%-black project default on ordinary light surfaces and system semantic inversion/adaptation elsewhere.
