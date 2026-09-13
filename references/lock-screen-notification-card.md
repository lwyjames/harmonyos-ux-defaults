# Lock-Screen Notification Card

Use this reference when an ordinary notification is shown as an expanded/detail card on a phone lock screen. It reconstructs reusable relationships from the user-supplied Pura X View lock-screen notification screenshot reviewed on 2026-09-13. The source screenshot, its WeChat identity, sender, message, and wallpaper are intentionally not bundled or reproduced. Measurements and material values below are screenshot-derived project specifications, not claimed official HarmonyOS tokens.

## Scope and precedence

- This is the expanded/detail **lock-screen notification card**. It is not the transient top Push Notification banner, notification-center row, Live View card, service card, call/alarm surface, or the lock screen's default collapsed icon-and-count presentation.
- Continue to follow the core notification source for eligibility, grouping, lifecycle, actions, privacy, and user settings. In particular, the lock screen normally exposes only notifications belonging to the current locked session, and the user's lock-screen preview setting controls whether message detail may be shown.
- Read [lock-screen-visual-defaults.md](lock-screen-visual-defaults.md) for the lock-screen camera, clock, status anchors, lower shortcuts, and navigation treatment. Adding this card is an overlay operation: it must not move, scale, dim, blur, or recolor those underlying elements outside the card mask.
- Read [push-notification-banner.md](push-notification-banner.md) only when the same design also needs the separate transient top banner. Do not copy that banner's top coordinate or bottom affordance into this component.

## Coordinate basis

- Resolve geometry in the complete visible logical screen canvas before bezel compositing.
- Let `W` and `H` be the current portrait logical width and height in vp.
- Let `S_top` be the resolved top edge of the lower lock-screen shortcut containers. For the standard portrait lock-screen relationship in [lock-screen-visual-defaults.md](lock-screen-visual-defaults.md), `S_top = H - 99 vp`.
- Apply verified cutout, corner, and system safe insets before raster conversion. Round final raster edges once; do not independently round `x`, `y`, width, and height and then accumulate the error.

## Responsive outer geometry

Use these screenshot-derived project defaults:

```text
M = max(16 vp, verified leading safe inset, verified trailing safe inset)
cardX = M
cardWidth = W - 2M
cardHeight = 64 vp
cardRadius = 16 vp
cardBottom = S_top - 27 vp
cardY = cardBottom - 64 vp
```

With the standard shortcut relationship, this simplifies to:

```text
cardY = H - 190 vp
cardBottom = H - 126 vp
```

- Preserve the `27 vp` vertical gap between the card bottom and the lower shortcut top. If a device-specific safe area moves both shortcuts upward, move the card upward by the same amount.
- If lower shortcuts are intentionally absent, retain the standard `H - 126 vp` card-bottom anchor unless that model's verified safe area requires a larger bottom clearance.
- Keep the card horizontally centered. Never stretch it into the bezel, use presentation-canvas edges, or copy a Pura X View raster box onto another model.
- One compact card is `64 vp` high. A multi-notification list or expanded stack requires the native notification-list rules; do not silently increase this single-card height or cover the shortcuts.

### Derived portrait examples

| Device/state | Logical canvas | Card frame |
|---|---:|---:|
| Pura X View front portrait | `440 x 744 vp` | `(16,554,408,64) vp` |
| Pura 90 Pro Max portrait | `374 x 823 vp` | `(16,633,342,64) vp` |
| Pura X Max unfolded portrait | `665 x 940 vp` | `(16,750,633,64) vp` |

These rows demonstrate the formula. Device-specific safe insets may increase `M` or lift the card and shortcuts together; the Pura X View pixel coordinates are never universal.

Use `scripts/lock_screen_notification_geometry.py` to calculate logical and once-rounded raster frames. For example:

```bash
python scripts/lock_screen_notification_geometry.py \
  --width-vp 440 --height-vp 744 \
  --pixel-width 1320 --pixel-height 2232
```

## Internal anatomy

All coordinates below are relative to the card frame `(0,0,Cw,64)`:

| Element | Frame / rule |
|---|---|
| App/service logo | `(12,16,32,32) vp`; preserve the resolved native app icon artwork and native tile radius |
| Title | leading `56 vp`, top `12 vp`, height `20 vp`; one line, `Body_L` about `16 fp`, Medium |
| Timestamp | trailing `12 vp`, top `12 vp`, height `20 vp`; intrinsic width, `Body_S` about `12 fp`, Regular |
| Detail/content | leading `56 vp`, top `34 vp`, trailing `12 vp`, height `20 vp`; one line, `Body_M` about `14 fp`, Regular |

- The title identifies the sender, conversation, event, or function required by the notification. It is not forced to repeat the app name.
- Reserve `8 vp` between the title's maximum trailing edge and the timestamp. Calculate `titleMaxWidth = Cw - 56 - 12 - timestampWidth - 8` and truncate with an ellipsis when needed.
- Align title and detail on the same `x=56 vp` text axis. Keep the timestamp optically aligned to the title row.
- For the compact `64 vp` card, keep detail to one line and ellipsize overflow. Do not shrink type below the semantic role, wrap into the shortcut area, or increase card height without entering a native expanded/list state.
- There is **no centered bottom handle/affordance** in this lock-screen card. That handle belongs to the separate transient top-banner pattern.
- App logo, title, detail, and timestamp are content layers at full group opacity. Do not reduce the entire notification group opacity to obtain translucency.

## Wallpaper-responsive material

The flattened screenshot cannot reveal the original system blur radius or source alpha exactly. Use the following as a reproducible project reconstruction:

1. Freeze the complete, sharp lock-screen base.
2. Copy only the pixels beneath the card, including offscreen filter padding sufficient for the blur kernel.
3. Apply a color-preserving thin glass blur to that copy. Preserve the wallpaper's broad local hue and luminance while removing identifiable detail.
4. Derive a high-lightness, reduced-chroma tint from the local wallpaper under the card. Composite that tint at `28%` source opacity by default; adapt only within `22–34%` when contrast testing requires it, and record the chosen value.
5. Add a neutral-light outline at `40%` source opacity and no more than `1 vp` thickness.
6. Clip the blurred copy, tint, and outline to the final `16 vp` rounded mask after filtering. Allow only the natural one-pixel antialias transition at the perimeter.
7. Draw title at full semantic foreground strength; render detail and timestamp with secondary emphasis, approximately `72%` of the foreground color when a system semantic token is unavailable.

The wallpaper supplies the family of the card color: red wallpaper may yield restrained rose glass, blue wallpaper cool blue-gray glass, and a neutral wallpaper neutral glass. Never prescribe the reference's red/pink hue, fixed opaque white, fixed gray, or an unrelated accent as the universal card color.

Do not add exterior haze, glow, broad drop shadow, full-screen blur, or a parent opacity that fades the logo and text. If a small elevation edge is needed for contrast, it must be visually local and must not modify underlying pixels outside the rounded mask.

## Privacy, behavior, and accessibility

- Respect the system's **锁定时显示预览** setting and app-level lock-screen notification setting. When preview is disabled, keep the native app identity/state but redact or replace sensitive title/detail according to system behavior; never expose private message content in a mockup merely to fill the layout.
- Use fictional, privacy-safe copy and non-identifying logo treatments in exploratory mockups unless the user supplies authorized brand content.
- Tapping the card opens the exact notification destination after the required authentication/unlock path. Do not invent custom gestures or place unrelated action buttons in this compact card.
- Preserve screen-reader order as logo/app identity, title, detail, then time; expose the card as one coherent notification target unless the native notification template explicitly provides actions.
- Keep text legible against the locally derived material in light and dark wallpapers. Adjust tint lightness and semantic foreground before changing geometry.

## Layering and verification

Generate an A/B pair during deterministic validation:

1. Render the normal lock screen without the notification and freeze it.
2. Composite the notification card above the frozen image.
3. Compare both outputs outside the card's rounded mask plus one antialias pixel.

Reject the result if any of the following is true:

- Pura X View does not resolve to `(16,554,408,64) vp`, or another model copied its raster coordinates instead of applying the responsive formula;
- the card does not preserve a `27 vp` gap above the lower shortcut containers, collides with them, or pushes them downward;
- logo, title, detail, or timestamp violates the internal alignment table, or a transient-banner bottom handle appears;
- the card uses a fixed pink/red/white/gray fill unrelated to its local wallpaper, loses all local hue, or makes text/logo translucent with the material;
- blur, tint, desaturation, shadow, or haze changes any lock-screen pixel outside the rounded card boundary plus one antialias pixel;
- the clock, wallpaper, shortcuts, navigation indicator, status content, camera, or bezel is moved or regenerated when the card is added;
- sensitive preview content is visible when the lock-screen preview setting is off.

Observable acceptance criterion:

> On Pura X View portrait, a single expanded/detail lock-screen notification is a centered `408 x 64 vp` wallpaper-responsive glass card at `(16,554) vp`, with a native `32 vp` logo, aligned title/detail, trailing time, `16 vp` radius, and a `27 vp` gap above the fixed lower shortcuts. Other portrait phones derive the same relationships from `W`, `H`, safe insets, and shortcut position. The base lock screen remains pixel-identical outside the card mask, and private content follows the system preview setting.
