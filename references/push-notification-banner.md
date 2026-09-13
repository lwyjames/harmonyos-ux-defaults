# Portrait Push Notification Banner

Use this reference for a transient Push Notification banner on any designated phone in portrait orientation. It generalizes the user-supplied Pura X View example without storing or reproducing the screenshot, its WeChat identity, its message, or its red wallpaper.

The screenshot is a supplementary visual source for geometry, placement, internal relationships, and apparent material. The supplied HarmonyOS notification guide remains authoritative for value, eligibility, templates, text limits, grouping, timing, privacy, and other presentation surfaces.

## Scope

- Apply this component to every app or service when its push is presented as a transient portrait banner.
- Do not limit the treatment to WeChat, messaging, the launcher, or Pura X View.
- Do not force this banner geometry onto notification-center cards, the default lock-screen icon/count presentation, an immersive one-line banner, persistent call/alarm UI, a Live View card/capsule, a compact outer display, or landscape. Those retain their native rules.
- The system owns the banner surface. App content supplies only permitted icon, title, detail, destination, and notification behavior.
- A banner normally disappears after 5 seconds; calls and alarms may persist according to the core notification source. If several arrive together, show only the newest banner.

## Responsive outer geometry

Let `W` and `H` be the complete visible logical phone canvas in vp. For a portrait Push Notification banner:

```text
bannerX = 16 vp
bannerY = 50 vp
bannerWidth = W - 32 vp
bannerHeight = 64 vp
cornerRadius = 16 vp
```

Both side margins are exactly `16 vp`. Measure `y=50 vp` from the complete visible UX canvas, not from the bezel canvas, camera, status-bar bottom, application title, wallpaper feature, or a manually estimated aperture. The mapped official bezel still controls the visible aperture during final compositing.

Do not scale the `64 vp` height or `16 vp` radius with screen width. Width alone is responsive. Calculate all logical edges first, convert the complete frame through the designated device's documented screen mapping, and round each final raster edge once. Do not reuse one device's pixel frame on another device.

Reference results:

| Portrait phone | Logical canvas | Banner frame (vp) |
|---|---:|---:|
| Pura X View | `440 x 744` | `(16,50,408,64)` |
| Pura 90 Pro Max | `374 x 823` | `(16,50,342,64)` |
| Pura X Max unfolded | `665 x 940` | `(16,50,633,64)` |

On Pura X View's `1320 x 2232 px` mapping, the once-rounded banner frame is `(48,150,1224,192) px` and its radius is `48 px`. This is a reference result, not a reusable fixed raster size.

## Internal layout

Let `Cw = W - 32 vp` be the local banner width, and let `Tw` be the measured one-line timestamp width.

```text
App/service icon:       (x=12, y=16, width=32, height=32) vp
Title frame:            x=56, y=12, height=20 vp
Timestamp frame:        right=12, y=12, height=20 vp, intrinsic width Tw
Title max width:        Cw - 56 - 12 - Tw - 8 vp
Detail frame:           (x=56, y=34, width=Cw-68, height=20) vp
Bottom affordance:      (x=Cw/2-24, y=54, width=48, height=4) vp
```

- Use the system-resolved app or service icon. Preserve its native artwork and color inside the `32 x 32 vp` frame; use an `8 vp` tile radius only when the source icon is a rounded-square tile. Do not substitute an invented logo or reuse WeChat for another app.
- The title is the sender, event, or concise function summary—not merely the application name. It is one line and follows the core limit of at most 15 Chinese or 22 English characters.
- The detail is the useful notification content. In this compact banner variant it is one line with end ellipsis. Longer content remains available in the corresponding full notification surface, whose core limit is up to three lines and 57 Chinese or 84 English characters.
- Keep `8 vp` between the title and timestamp collision envelopes. Truncate the title before allowing either text to overlap.
- Align title and detail to `x=56 vp`; do not center them in the card. Keep the timestamp trailing-aligned `12 vp` from the card edge.
- The centered bottom affordance is system-owned. It is not a progress indicator, navigation bar, or app action.
- Do not render the affordance as fixed opaque white or write a translucent-white RGBA value into a flattened RGB output without alpha compositing. Sample the completed local banner material directly behind the affordance, preserve its hue, reduce its chroma, and raise its lightness before compositing the affordance translucently. The screenshot-reconstructed project default is `affordanceTint = mix(localMaterial, localWhite, 65%)` rendered at `60%` source opacity, which produces approximately `39%` effective lightening over the local material. This is a project reconstruction, not an official recovered token. If contrast adaptation is required, preserve the wallpaper relationship and subtle tertiary hierarchy rather than switching to pure white.
- Use HarmonyOS Sans through the external font resolver. Recommended roles are `Body_L` (`16 fp`, Medium) for title, `Body_M` (`14 fp`, Regular) for detail, and `Body_S` (`12 fp`, Regular) for time. Preserve fp scaling; at larger accessibility sizes, use the native expanded notification surface rather than clipping or distorting this compact banner.

## Wallpaper-responsive material

The screenshot is flattened and cannot reveal the original system blur radius or source-layer alpha. Therefore distinguish verified appearance from project reconstruction:

1. Freeze the complete sharp app, home-screen, or other eligible underlay before adding the banner.
2. Copy only the pixels beneath the banner, add kernel padding outside the sample rectangle, and apply a color-preserving `ULTRA_THIN` top-floating-system material or native equivalent.
3. Crop the blurred result to the banner frame and apply the final `16 vp` rounded mask after filtering.
4. Apply a neutral-dark overlay at **32% opacity**. This is the screenshot-reconstructed project default, not an extracted official token.
5. Add a thin neutral-light perimeter outline at **24% opacity**, visually subordinate to content. Use at most `1 vp`; prefer a hairline at the raster scale.
6. Render the native icon and text independently above the material in a `100%`-opacity root group. Use inverse semantic hierarchy: primary title at full strength and detail/time at secondary strength. Render the bottom affordance as its own wallpaper-responsive translucent sublayer using the local-material derivation above; never reduce the whole banner group's opacity.

The apparent card hue must arise from the actual wallpaper or app pixels beneath it. Never sample one red, pink, blue, green, or other hue from the example and bake it into every banner. Never use overall parent opacity to create translucency, because that also weakens the icon and text. Do not add an opaque gray replacement, unrelated gradient, white haze, bloom, or broad exterior shadow.

Require at least `4.5:1` text contrast for body-sized text. If the native system material adapts its appearance for a difficult light or high-variance underlay, preserve the component-private semantic behavior and record the adaptation instead of recoloring the app icon or reducing text opacity below readability.

## Layering and background preservation

Construct the normal card-free phone screen first and freeze every system/app/home coordinate. Composite the banner over that frozen screen.

- Do not move, delete, reflow, dim, recolor, or pre-blur the wallpaper, launcher icons, app title, feed, chat, or other underlying content to create clearance.
- Do not derive any underlying position from `bannerY`, `bannerHeight`, or `bannerBottom`.
- Blur, tint, outline, and any antialiasing must end at the rounded boundary. Outside the rounded banner plus a one-pixel antialias ring, the banner-present screen must be pixel-identical to the banner-free base.
- Keep the HarmonyOS status bar, physical camera/cutout, navigation indicator, and official bezel unchanged. The banner starts at `y=50 vp` and must not cover or displace the status bar.
- The example screenshot's `08:19` time, status icons, status capsule, battery value, and wallpaper are scenario content, not new system-chrome defaults. Continue to apply the skill's existing status-bar and static-time rules.
- Different system events may coexist only when their native rules permit. Never duplicate the same event as both a Push Notification and Live View.

## Deterministic geometry helper

Use `scripts/push_notification_banner_geometry.py` to calculate logical and once-rounded raster geometry. Supply the designated phone's documented logical and pixel canvases; `--time-width-vp` defaults to the `32 vp` check value used for “刚刚” but should be replaced by the actual measured one-line timestamp width.

```bash
python scripts/push_notification_banner_geometry.py \
  --width-vp 440 --height-vp 744 \
  --pixel-width 1320 --pixel-height 2232 \
  --time-width-vp 32
```

## Interaction and accessibility

- Tapping anywhere on the banner opens the corresponding detail destination.
- Preserve notification privacy and lock-screen preview settings. Do not expose hidden content merely because a mockup shows a banner.
- Support screen readers with application/source, contextual title, detail, time, and destination semantics in reading order.
- Respect reduced motion. Entrance/exit motion must not move the underlying screen.
- Do not use this notification as an advertisement, mini widget, or forced commercial top placement.

## Verification

For every portrait push banner, verify:

```text
bannerX = 16 vp
bannerY = 50 vp
bannerWidth = canvasWidth - 32 vp
bannerHeight = 64 vp
cornerRadius = 16 vp
```

Also confirm:

- left and right margins are both `16 vp`;
- the `32 vp` source icon, `x=56 vp` text anchor, trailing `12 vp` time inset, and centered `48 x 4 vp` affordance are present;
- the bottom affordance remains visibly related to the local banner/wallpaper hue, is translucently alpha-composited, and is not fixed or flattened as pure white;
- title, timestamp, and detail do not collide, clip, or wrap in the compact banner;
- logical geometry is completed before raster conversion and final raster edges are rounded only once;
- another phone never reuses the Pura X View `1224 x 192 px` result;
- the actual local underlay drives the softened hue and luminance;
- the reconstructed neutral-dark overlay is `32%` and the neutral-light outline is `24%`;
- the icon/text root remains at `100%` opacity and body text meets `4.5:1` contrast;
- no fixed red/pink/other source hue is baked into the material;
- no blur, tint, outline, shadow, or changed pixel escapes the rounded banner plus one-pixel antialias allowance;
- the banner overlays rather than pushes or clears the underlying UI;
- status bar, cutout, navigation indicator, mapped home screen, and bezel remain unchanged;
- the banner remains inside the official mapped screen aperture and clears system-owned status content;
- no duplicate Live View or other representation of the same event appears.

Acceptance criterion:

> On any designated portrait phone with logical width `W`, a transient Push Notification banner occupies `(16,50,W-32,64) vp` with `16 vp` radius. It uses the system app/service icon, contextual one-line title, one-line detail, trailing time, and centered bottom affordance. Its apparent hue comes from locally blurred underlying pixels beneath a reconstructed 32% neutral-dark overlay and 24% neutral-light outline; all effects are clipped to the rounded banner, and the sharp underlying screen remains pixel-identical everywhere else.
