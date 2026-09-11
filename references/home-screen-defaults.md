# Default Phone Home Screens and System Chrome

Use this reference whenever a phone home screen, launcher, desktop, status bar, or navigation bar appears in a UX requirement, mockup, flow, keyframe, generated image, presentation visual, or prototype preview.

## Mapped home-screen masters

| Device and state | Operational PNG | Compact lossless source | Supplied master pixels |
|---|---|---|---:|
| Pura X Max, unfolded portrait | `assets/default-homescreens/pura-x-max-unfolded-portrait.png` | `assets/default-homescreens/pura-x-max-unfolded-portrait.lossless.webp` | 2194 x 3101 px |
| Pura X View, front portrait | `assets/default-homescreens/pura-x-view-front.png` | `assets/default-homescreens/pura-x-view-front.lossless.webp` | 2376 x 4018 px |
| Pura 90 Pro Max, portrait | `assets/default-homescreens/pura-90-pro-max-portrait.png` | `assets/default-homescreens/pura-90-pro-max-portrait.lossless.webp` | 1831 x 4032 px |

- Use the mapped PNG itself whenever one of these three devices displays its default home screen. Do not redesign, regenerate, substitute, crop, reflow, recolor, relabel, rearrange, or remove its wallpaper, clock/date/weather, widgets, icons, labels, page indicator, dock, status information, or navigation treatment.
- If the operational PNG is not present in a compact skill installation, materialize it from the mapped lossless WebP with `python scripts/materialize_home_screen.py --device DEVICE --output OUTPUT.png`. The helper verifies the decoded RGB pixel hash against the supplied PNG before writing. This storage optimization changes neither dimensions nor visible pixels and is not permission to use a visually similar substitute.
- Preserve the source aspect ratio. When the phone-screen composition requires the device's documented preview resolution, create one proportional copy at that resolution before bezel compositing; do not stretch or crop the master and do not alter its internal layout.
- Keep the original master untouched. Place the scaled screen copy beneath the mapped bezel using the alpha-aware compositing workflow in [device-preview-frames.md](device-preview-frames.md).
- For another phone model without a mapped master, adapt the supplied masters' icon artwork, labels, widget hierarchy, grid, spacing, clock/date/weather treatment, page indicator, dock, wallpaper relationship, and system-chrome design to that phone's documented canvas. Do not present a mapped PNG as the exact home screen of a different device.

## Default status bar

- Show **08:08** as the default phone time in every static phone UX output unless the user or scenario explicitly requires another time. Keep a scenario-critical time when changing it to 08:08 would make the depicted state false.
- Place the right-side status cluster at the right end of the status bar and follow `assets/system-chrome/status-bar-right-default-reference.png`.
- Match the reference's physical left-to-right order: **NearLink logo → Wi-Fi 7 logo → dual stacked 5A cellular signals → battery**. Equivalently, from the screen's right edge inward, the order is battery → dual 5A → Wi-Fi 7 → NearLink.
- Preserve the NearLink mark, the Wi-Fi 7 identifier/details, two stacked 5A rows with their signal dots/bars, and the battery shape with **100**. Do not replace these with generic Bluetooth/NFC, ordinary Wi-Fi, a single cellular row, a different network label, or a generic battery icon.
- Use the reference geometry and relative spacing. Select black or white foreground content only as needed to satisfy the existing local-background contrast rule; do not change the icon order or anatomy.

## Default navigation bar geometry

- Read [navigation-bar-geometry.md](navigation-bar-geometry.md) whenever the navigation bar is present.
- For logical screen width `W`, use visible-indicator width `112 vp` at `360 <= W < 600`, `W / 3 - 48 vp` at `600 <= W <= 840`, and `W / 4 - 48 vp` at `W > 840`.
- Render the visible indicator as a **6 vp-high capsule**, center it horizontally, and place its bottom edge exactly **6 vp above the visible bottom of the UX screen opening**. If a raster renderer requires a radius, 3 vp is the derived half-height, not a separate source token.
- Define a separate invisible interaction region: `35%` of `W` wide, `28 vp` high, centered horizontally, and flush with the visible screen bottom. Keep bottom content clear of this region; do not draw it as a visible bar.
- For a bezel-free screen-only output, the visible screen bottom and raw UX-canvas bottom are the same. For a bezeled output, the official bezel's center-connected alpha aperture defines the visible bottom and always controls.
- Do not substitute a standard rectangle, alter the capsule proportions, scale, stretch, shift, or omit the navigation bar for visual cleanliness. Never use the superseded `1252 x 84 px`, 42 px radius, or 16 px offset. Apply the documented absence/temporary-hide exceptions in [system-chrome-verification.md](system-chrome-verification.md).

## Verification

Reject a phone visual unless all applicable checks pass:

- the displayed time is 08:08 or a different time has an explicit scenario reason;
- the right cluster matches the reference anatomy and order, including NearLink, Wi-Fi 7, dual 5A, and battery 100;
- a present navigation indicator is a centered 6 vp-high capsule with a 6 vp bottom-edge gap, uses the correct width formula for current logical `W`, and has a separate centered `35% W x 28 vp` bottom-anchored interaction region;
- a mapped default home screen uses the correct supplied PNG without internal redesign or crop;
- another phone's adapted home screen preserves the supplied icon/widget language and layout relationships;
- system chrome remains inside the screen opening and the final phone passes bezel-seam verification.
