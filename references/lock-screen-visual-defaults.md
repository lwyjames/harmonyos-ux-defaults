# Lock-Screen Visual Defaults

Use this reference whenever a phone lock screen, lock-screen clock, or lower lock-screen shortcut is rendered. It reconstructs reusable relationships from the user-supplied Pura X View lock-screen reference reviewed on 2026-09-13. The source screenshot is intentionally not bundled. Measurements below are screenshot-derived project specifications, not claimed official HarmonyOS tokens.

When an ordinary notification is shown as an expanded/detail lock-screen card, also read [lock-screen-notification-card.md](lock-screen-notification-card.md). That card overlays this already-complete lock screen and must not move the clock, lower shortcuts, navigation indicator, status content, wallpaper, camera, or bezel. The separate transient top Push banner remains governed by [push-notification-banner.md](push-notification-banner.md).

## Pura X View coordinate basis

- Resolve all measurements in the complete visible `440 x 744 vp` portrait screen canvas before bezel compositing.
- Do not measure from the outer presentation canvas, metal frame, black exterior, or a resized documentation image.
- Convert the completed logical layout to the mapped `1320 x 2232 px` screen only once. For a lightweight preview, uniformly scale the complete validated composition afterward.

## Front camera

For Pura X View front portrait:

- Center: `(220,27) vp`.
- Visible outer diameter: `22 vp`.
- Shape: one perfect circle with a black outer rim, a concentric dark-glass lens, and restrained cool-blue optical highlights.
- The camera is hardware, not a software icon. It must remain above the screen layer and must not acquire a square/rectangular tile, colored backing, halo, notch, Dynamic Island, or duplicate dot.
- Use the corrected mapped `assets/device-bezels/pura-x-view-front.png`; do not redraw the camera with an image model. In landscape, rotate the complete untouched corrected bezel 90 degrees counterclockwise, so this same camera module appears on the left side.

This camera geometry is Pura X View-specific. Other models continue to use their mapped bezel/camera source rather than inheriting the `22 vp` diameter or `(220,27)` center.

## Portrait status-bar edge anchors

For the Pura X View portrait status row:

- Leading status item, including the default time when shown: left edge at `x=32 vp`.
- Trailing battery: right edge at `x=408 vp`, leaving a `32 vp` visible-screen inset.
- Align the left and right status groups optically to the camera centerline at `y=27 vp`.
- For the screenshot-scale status glyphs, the top visible bound is approximately `17 vp` from the visible screen top. Preserve the `y=27 vp` optical center when glyph height or font metrics differ rather than forcing every asset into an identical box.
- Keep both groups outside the camera's circular exclusion area and clear of rounded corners.
- Preserve the existing default time and right-cluster rules: `08:08` when time is not scenario-specific; NearLink, Wi-Fi 7, dual stacked 5A signals, and battery 100 in the required order. The lock-screen screenshot contributes placement, not replacement values or icon anatomy.
- On another model, retain its verified cutout and safe-area mapping; adapt the same balanced edge relationship rather than copying Pura X View coordinates blindly.

## Wallpaper-derived clock material

Do not render the large lock-screen clock as unrelated opaque white by default.

1. Sample two or three representative hues from the wallpaper around and behind the clock. Favor the local upper and lower clock regions instead of averaging the entire wallpaper.
2. Raise lightness and reduce chroma enough for legibility while retaining recognizable wallpaper hue. A multicolor wallpaper may produce a restrained vertical gradient or line-specific tint, as in a cooler upper time line and warmer lower time line.
3. Apply the reconstructed project default of `78%` clock-layer opacity. Because the supplied screenshot is flattened, the original source alpha cannot be recovered exactly; allow `72–84%` only when local contrast testing requires adjustment.
4. Keep the numeral shapes clean and the wallpaper sharp outside the glyphs. Do not blur the full lock screen, add a white plate, use neon glow, or introduce a color absent from the wallpaper.
5. If the sampled tint becomes unreadable, first adjust its lightness or use a subtle local contrast treatment. Use opaque white only as an explicitly justified accessibility fallback.

The clock's color material relationship is portable to other phone models and wallpapers; its exact Pura X View placement or typography is not a universal geometry token.

## Lower shortcuts

For the `440 x 744 vp` Pura X View portrait lock screen:

| Element | Frame / geometry |
|---|---|
| Left shortcut container | `(16,645,48,48) vp` |
| Right shortcut container | `(376,645,48,48) vp` |
| Container centers | `(40,669) vp` and `(400,669) vp` |
| Bottom relationship | container bottom is `51 vp` above the visible screen bottom, or `23 vp` above the top of the `28 vp` bottom interaction region |
| Left glyph | centered hollow annulus, `22 vp` outer diameter, `4 vp` ring thickness |
| Right glyph | centered simplified camera, approximately `16 x 13 vp`, with rounded body, small top housing, and circular lens knockout |

Material construction:

- Use a `48 vp` circular container with a thin `1 vp` outline. Never use a rounded square, opaque disk, label, or unrelated icon tile.
- Sample the wallpaper locally beneath each shortcut. Build a high-lightness, low-chroma tint from that local color; the left and right tints may differ subtly when the wallpaper differs.
- Use the wallpaper-derived tint at approximately `12%` opacity for the optional circular surface, `68%` for the outline, and `92%` for the glyph. These are screenshot-reconstructed project defaults, not official recovered tokens.
- Keep the wallpaper visibly continuous through the circle. Do not blur or dim a larger surrounding patch and do not add a broad shadow or glow.
- Preserve symmetric side placement. On another portrait phone, keep `48 vp` containers centered `40 vp` from the visible side edges and keep their bottom edges `23 vp` above the bottom interaction region when present; move both inward or upward together only when that model's verified corner or gesture safe area requires it.
- When the navigation indicator is absent, retain a `51 vp` bottom inset unless the device-specific lock-screen safe area requires more.

## Verification

Reject the lock-screen render if any of the following is true:

- Pura X View camera center or diameter differs from `(220,27)` / `22 vp`, the lens becomes a flat dot, or any square background is visible;
- Pura X View portrait status content ignores the `32 vp` side anchors, crowds the approximately `17 vp` top bound, or is not optically centered around `y=27 vp`;
- the status supplement replaces the required default time/right-cluster anatomy instead of only positioning it;
- the clock is opaque white without a justified fallback, uses colors absent from the wallpaper, or loses legibility;
- shortcut containers are not `48 vp` circles, are asymmetric, collide with the bottom interaction region, or use solid unrelated colors;
- the left annulus or right camera glyph is malformed, mislabeled, blurred, or generatively substituted;
- a wallpaper-derived treatment changes or blurs pixels outside the clock glyphs or shortcut circles.

Observable acceptance criterion:

> A Pura X View lock screen uses a single 22 vp circular camera centered at `(220,27) vp`, 32 vp portrait status-edge anchors, a translucent wallpaper-derived clock palette, and two symmetric 48 vp circular shortcuts whose tint and opacity remain visibly related to the local wallpaper. The camera has no rectangular backing, the status anatomy remains authoritative, and no material effect leaks beyond its intended glyph or circle.
