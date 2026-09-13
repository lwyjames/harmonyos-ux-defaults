# HarmonyOS UX Default Quick Reference

Use this summary to orient the work. Consult the routed source text and PDF before relying on a detailed rule or value.

## Contents

1. Default interpretation
2. Responsive layout
3. Spacing and radii
4. Typography and UI language
5. Color and Immersive Light
6. System chrome
7. Multi-window
8. Flash Control Ball and Window
9. Sharing and Tap-to-Share
10. Notifications and Live View
11. Service cards
12. Security and privacy branding
13. Delivery checklist

## 1. Default interpretation

- Default platform when unspecified: HarmonyOS NEXT.
- Default phone preview frame: Pura X Max unfolded portrait, 1828 x 2584 px, 665 x 940 vp.
- Default image delivery: lightweight preview, not native size. Use the tool's lightweight/standard setting; when a pixel target is required, keep the longest edge at or below 1600 px. Native pixels remain the geometry source. Generate a native-size file only when the user explicitly requests native/original resolution, a high-resolution final, print/final-delivery quality, or exact dimensions.
- Default bezel asset: `assets/device-bezels/pura-x-max-unfolded-portrait.png`.
- Default static phone time: **08:08**, unless the depicted scenario explicitly requires another time.
- Default present navigation indicator: a horizontally centered **6 vp-high capsule** with its bottom edge **6 vp above the bezel-derived visible screen bottom**. For logical width `W`, use width `112 vp` at `360 <= W < 600`, `W / 3 - 48 vp` at `600 <= W <= 840`, and `W / 4 - 48 vp` at `W > 840`. Keep the separate invisible `35% W x 28 vp` bottom-anchored interaction region.
- Default status-bar right cluster: follow `assets/system-chrome/status-bar-right-default-reference.png`; physical left-to-right order is NearLink, Wi-Fi 7, dual stacked 5A, battery 100.
- Mandatory visual-output rule: include the corresponding designated bezel around every phone screen by default. Omit it only when the user explicitly requests a bezel-free, screen-only, raw-canvas, or implementation-only output.
- Mandatory compositing rule: the mapped official bezel PNG alone defines all four aperture boundaries, corner curves, antialiasing, camera/hinge/frame geometry, and exterior transparency. Never replace it with a guessed rounded rectangle, radius, generic mask, hard-coded aperture, or generated bezel.
- Implementation units: vp for geometry and fp for type. Do not implement from preview pixels.
- Default screen language: Simplified Chinese.
- Default font binary for Simplified Chinese and mixed Chinese/Latin HarmonyOS UI: checksum-verified external `HarmonyOS_Sans_SC.ttf` (HarmonyOS Sans SC / 鸿蒙黑体). Keep font binaries outside the skill and follow [harmonyos-sans-font-assets.md](harmonyos-sans-font-assets.md). Use another platform font only when that platform is explicit.
- Default system patterns: native HarmonyOS components, share sheet, notifications, Live View, service cards, status bar, navigation bar, and multi-window behavior.
- Use the mapped user-supplied bezel for each designated device. Preserve its camera, frame, hinge, corner, and hardware geometry. If no mapped bezel exists, show the front camera as a single round dot.
- Pura X View portrait uses the corrected mapped camera: one `22 vp` circular optical module centered at `(220,27) vp`, with no square backing or duplicate dot. Read [lock-screen-visual-defaults.md](lock-screen-visual-defaults.md).
- For HarmonyOS security/privacy UX, use the supplied official 鸿蒙星盾安全 shield whenever a branded security/privacy emblem is shown; never substitute a generic or invented shield.

### Phone preview frames and bezels

| Device and state | Preview pixels | Logical canvas | Bezel asset | Default home-screen master |
|---|---:|---:|---|---|
| Pura X Max, unfolded portrait — default | 1828 x 2584 px | 665 x 940 vp | `assets/device-bezels/pura-x-max-unfolded-portrait.png` | `assets/default-homescreens/pura-x-max-unfolded-portrait.png` |
| Pura X Max, unfolded landscape | 2584 x 1828 px | 940 x 665 vp | portrait asset rotated 90 degrees clockwise; camera at upper-right | adapt only when explicitly required |
| Pura X View, front portrait | 1320 x 2232 px | 440 x 744 vp | `assets/device-bezels/pura-x-view-front.png` | `assets/default-homescreens/pura-x-view-front.png` |
| Pura X View, front landscape | 2232 x 1320 px | 744 x 440 vp | portrait asset rotated 90 degrees counterclockwise; camera on left side | adapt only when explicitly required |
| Pura 90 Pro Max, portrait | 1308 x 2880 px | 374 x 823 vp | `assets/device-bezels/pura-90-pro-max-portrait.png` | `assets/default-homescreens/pura-90-pro-max-portrait.png` |

- Read [device-preview-frames.md](device-preview-frames.md) before composing a phone mockup or prototype.
- Read [home-screen-defaults.md](home-screen-defaults.md) whenever a home screen, status bar, or navigation bar appears. Use each mapped home-screen PNG exactly; for another phone, adapt its icon/widget/layout language to the documented canvas.
- Apply the mapped bezel to every phone shown in multi-screen flows and presentation layouts, not only to the primary or first screen.
- The Pura X Max portrait dimensions are the portrait rotation of the baseline's Pura X Max unfolded entry, 2584 x 1828 px and 940 x 665 vp.
- For Pura X Max unfolded landscape, rotate the untouched official portrait bezel exactly 90 degrees clockwise so the front-facing camera lands at the upper-right. Render the UI separately at 2584 x 1828 px, derive the aperture from the rotated alpha channel, and composite the bezel last. Never rotate a completed portrait composite.
- For Pura X View landscape, render a fresh 2232 x 1320 px / 744 x 440 vp screen, rotate the untouched official portrait bezel exactly 90 degrees counterclockwise so the front-facing camera is on the left side, re-derive its alpha aperture, and composite it last. Never use a generated generic phone or rotate a completed portrait composite.
- The corrected Pura X View bezel is the source for both orientations. Preserve its 22 vp circular camera and reject any rectangular camera backing before or after rotation.
- The PNG asset's own outer canvas dimensions are not the device screen resolution. Fit the UI to the logical screen opening, then overlay the bezel without distorting it.
- Keep the app-screen and bezel source layers separate. Render the screen fully opaque at the documented resolution/aspect ratio and preserve its visible coordinate mapping.
- Create hidden overscan without moving or scaling the visible UI: extrude the first/last screen rows upward/downward, first/last columns leftward/rightward, and four corner pixels diagonally beneath the inner lip.
- Calculate top, bottom, left, and right overscan independently from the actual alpha transition plus a small data-derived hidden margin. Do not use one bleed constant for every device.
- Never resize, stretch, crop, redraw, or generatively recreate the bezel, and never resize a native final composite after the bezel is applied. For the default lightweight preview only, use one uniform proportional scale for the whole composition or consistently for all layers before compositing; never resize layers independently.
- Do not rotate a bezel except for the mapped Pura X Max unfolded-landscape and Pura X View front-landscape transforms. Rotate the untouched official source exactly 90 degrees clockwise for Pura X Max and exactly 90 degrees counterclockwise for Pura X View; apply no other transform.
- For any phone-in-hand/person/environment visual, finish and validate the mapped device master first, then composite separately generated scene and hand layers around it. This is mandatory for every current or future phone model, fold state, form factor, and both portrait and landscape orientations; Pura X View is only one example. Hands may occlude the frozen master through an explicit mask but may never regenerate, warp, resize, or reshape it. If the fit fails, revise the hands—not the device. If the named model/orientation lacks a verified bezel mapping, establish or request it rather than substituting a generic phone.
- When a hand or finger touches, approaches, holds, or occludes the device, read [phone-in-hand-contact-compositing.md](phone-in-hand-contact-compositing.md). Plan the grip from the exact device, classify every visible boundary segment as `foreground_occlusion`, `behind_device`, `physical_contact`, or `natural_clearance`, and preserve separate rear-hand/device/foreground-hand layers. Contact seams, bezel-through-skin, rear fingers covering the frame, clipped nails, and regressions outside a local edit region are rejection conditions.
- Derive aperture/exterior separation from the bezel alpha channel: isolate the center-connected opening from border-connected exterior transparency, preserve the antialiased boundary, allow screen overscan beneath the inner lip, and clip all screen content out of the exterior component.
- Use `scripts/composite_validate_bezel.py` for deterministic raster compositing. Require full-opacity underlay for every partially or fully transparent inner-aperture pixel and zero uncovered pixels in all four edge and four corner diagnostics.
- For Pura X/Pura X Max-like wide foldables, resolve inner/unfolded versus outer/compact display state before applying display-specific rules. Read [wide-foldable-pura-x-max.md](wide-foldable-pura-x-max.md).

## 2. Responsive layout

### Core behavior

- Design mobile-first from the smallest supported window.
- Avoid fixed-pixel layouts. Use flow, flex, grids, media queries, width/height breakpoints, and adaptive composition.
- Preserve layout integrity across rotation, resizing, split screen, floating windows, system font changes, display-mode changes, and fold states.
- Query device type, window width/height, orientation, and fold state. Fold state includes fold direction, hinge position, open/closed state, and hover posture.
- Keep critical content away from cutouts, rounded corners, gesture areas, the keyboard, and fold hinges.
- In small or crowded windows, center primary content and preserve the minimum complete task before secondary features.

### Horizontal breakpoints and window grid

| Window width | Columns | Default grid |
|---|---:|---|
| 0 <= width < 600 vp | 4 | margin 16 vp; gutter 8 vp (general) or 16 vp (loose) |
| 600 <= width < 840 vp | 8 | margin 24 vp; gutter 12 vp |
| width >= 840 vp | 12 | margin 32 vp; gutter 16 vp or 20 vp |

- Maximum grid content width: 2220 vp. Additional width becomes symmetric outer whitespace.
- Base layout grid: 8 vp. Small icons and fine controls may align to 4 vp.
- At width >= 600 vp, a parent-child hierarchy may become a split layout. Default ratio 4:6; 5:5 or 6:4 when the scenario requires it.
- At width >= 840 vp, bottom tabs may move to side tabs.
- Use a side navigation bar at >= 840 vp only when it expands hierarchy, destinations, or high-frequency actions. If only location changes, use side tabs.
- A side navigation bar is shown by default and may collapse. Fixed display requires minimum window width >= 840 vp.

### Device edge margins

| Device | Horizontal | Top | Bottom |
|---|---:|---:|---:|
| Phone | 16 vp | 36 vp | 28 vp |
| Foldable | 24 vp | 36 vp | 28 vp |
| Tablet | 32 vp | 36 vp | 28 vp |
| Smart screen | 48 vp | 27 vp | 27 vp |
| Wearable | 26 vp | 20 vp | 20 vp |
| PC | 40 vp | source does not prescribe | source does not prescribe |
| Cockpit | 48 vp | source does not prescribe | source does not prescribe |

Treat these as baseline screen-edge spacing, then also respect actual system safe-area insets.

### Pura X Max-like wide-foldable adaptation

- Apply this supplement to Pura X/Pura X Max-like wide foldables and other devices with a comparably broad unfolded/book-like proportion or compact outer display. Screen role and fold state control the rule; similar ratio alone does not turn an unfolded inner display into an outer display.
- Across fold, unfold, and orientation changes, keep images, video, dialogs, and controls aligned, complete, sharp, and interactive. Preserve text and icon sizes between inner and outer displays.
- On the compact outer display, hide the status bar, navigation bar, and their reserved vertical space. Outer display does not support split-screen or floating-window mode; the focused inner window becomes outer-display full screen and other windows move to background.
- Picture-in-Picture is supported on the outer display and continues without interruption when folding from the inner display.
- Preserve the inner app's title/content/optional-bottom architecture. Make overflow scroll, compress or transform fixed arrangements without clipping, and use scroll/click immersion where the source's size conditions and content type qualify.
- Outer-display adaptations: large title becomes small title; search field becomes an icon in the title row; index becomes segmented; prefer system popups with total height at most 90% of the screen; half-modal content scrolls and may extend to 8 vp below the window top.
- Keep top immersive banners and single-detail images at no more than 60% of screen/window height. Long-video frozen top region may shrink proportionally to 40% of screen height. Live comments/barrage stay at no more than 50% of window height; comments start at least 40% of screen height.
- Never crop short-video/live imagery: horizontal 16:9, 21:9, and 4:3 video fills width with adaptive height; vertical 9:16 fills the vertical content area with adaptive width. Outer full-screen video keeps the current orientation rather than rotating.

## 3. Spacing and radii

### Spacing

- Prefer the system spacing token scale and 4/8 vp rhythm. Do not introduce arbitrary values without a documented reason.
- Phone-family defaults:
  - between cards: 12 vp;
  - larger element separation with clear boundaries: 16 vp;
  - normal element separation without clear boundaries: 8 vp;
  - primary/secondary text vertical gap: 2 vp;
  - primary/secondary text horizontal gap: 8 vp.
- Smart-screen element gaps: large 24 vp, normal 12 vp, small vertical 8 vp.
- Smart-screen text hierarchy gaps: 32, 24, 16, 8, 4 vp.
- System padding tokens cover 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 32, 34, 36, 38, 40, 42, 44, 46, 50, 52, 54, 56, 58, 60, 64, 66, 68, 70, and 72 vp.

### Corner radii

Use one radius for elements of the same type and increase radius with visual/functional layer:

| Radius | Typical use |
|---:|---|
| 4 vp | labels, badges, small status marks |
| 8 vp | images, icons, small containers, list modules |
| 16 vp | notification cards, standard cards, content containers |
| 20 vp | buttons, menus, tabs, frequent controls |
| 32 vp | half-modal sheets, popovers, large top-layer surfaces |

Available system radius values include 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 32, and 36 vp.

## 4. Typography and UI language

Before final text rendering, run `scripts/resolve_harmonyos_fonts.py` for the deliverable's language profile and pass the returned absolute path to the renderer. Use `sc` by default, `tc` for Traditional Chinese, `latin` for Latin-only UI, and the corresponding explicit profile for condensed, italic, or Arabic text. Do not silently substitute another family in a final high-fidelity output; if the font asset is unavailable, request the original package or label a low-fidelity wireframe as `typography approximate`.

### Phone type roles

| Role token | Weight | Size |
|---|---|---:|
| Display_L / M / S | Light | 56 / 48 / 38 fp |
| Title_L / M / S | Bold | 30 / 24 / 20 fp |
| Subtitle_L / M / S | Medium | 18 / 16 / 14 fp |
| Body_L | Medium | 16 fp |
| Body_M / S | Regular | 14 / 12 fp |
| Caption_L / M | Medium | 12 / 10 fp |

- Support system large-font settings. Use fp and test wrapping, truncation, and layout reflow.
- Keep font family and weight usage consistent. Use the fewest type styles necessary to express hierarchy.
- Preserve Chinese punctuation rules, avoid orphan characters, and avoid breaking words in short English UI text.

### Chinese UI copy

- Speak like a knowledgeable, respectful friend: friendly, calm, clear, and direct.
- Address the user with “您/您的” by default; omit it when the actor is already clear. Use “你” only in rare advertising, philosophical, or voice contexts.
- Put necessary, decision-supporting information first. Remove repeated or nonessential context.
- Prefer short sentences and familiar words. Avoid overly formal, mechanical, cute, flippant, technical, or ornate language.
- Avoid trend slang, competitor disparagement, exaggerated marketing, and exclamation marks except rare important warnings, congratulations, or encouragement.
- Explain errors as result/cause/solution according to what is known. Always give a useful next action when one exists.
- Onboarding title: no more than 10 Chinese characters. Supporting text: ideally <= 22 characters, never more than 44.
- No final period for phrase lists, URLs, settings secondary text, onboarding secondary text, and Toasts. Use periods for procedural steps and sentence-level lists.
- Add half-width spaces around English terms and numbers in Chinese, and before measurement units. Do not add spaces around %, currency symbols, math operators, “-”, “>”, or “/”.
- Write setting paths as: 前往“设置”>“应用”>“应用管理”… with one confirmed destination per pair of quotation marks.
- Use Arabic numerals.

### Xiaoyi AI assistant

- Read [xiaoyi-assistant-interface.md](xiaoyi-assistant-interface.md) for the full-screen Xiaoyi/小艺 phone conversation surface. The two source captures are Pura X View references only; ignore their complete status bars and never bundle or reproduce their private content.
- Use three independent layers: a pinned material app bar, one scrolling mixed-content transcript, and a pinned bottom capability/composer stack. User messages are right-aligned asymmetric light-blue shapes: a single-line message is `44 vp` high with `(22,0,22,22) vp` top-left/top-right/bottom-right/bottom-left radii, so the upper-right corner is square and the other three are rounded. Xiaoyi responses remain unboxed and left-aligned. Show concise observable task status and native result cards only when the response requires them; never expose hidden reasoning or raw tool logs.
- Resolve the applicable device-edge margin as `E` (`16 vp` ordinary phone, `24 vp` foldable, `32 vp` tablet-class), conversation inset as `T=E+8 vp`, and active conversation-column width as `K`. Compute result width as `K-2T`, user-bubble maximum as `min(360 vp,K-2T)`, and composer as `(E,*,K-2E,48) vp` with `24 vp` radius.
- Pura X View portrait resolves to result width `392 vp` and composer width `408 vp`; Pura 90 Pro Max portrait resolves to `326/342 vp`; Pura X Max unfolded portrait resolves to `601/617 vp`. These are calculation checks, not fixed reusable sizes.
- Keep portrait phones single-column. In landscape/short-height windows, collapse optional chips before impairing the composer and move colliding low-priority app-bar actions to overflow. At `W>=840 vp`, center a readable grid-aligned conversation column; introduce a second pane only for a real hierarchy. Never scale the complete Pura X View page.
- Treat the screenshot's shell controls as normative, not examples. Use glass transparency for every menu/action/chip/composer surface; the top-right sequence is sparkling telephone (small upper star, large lower star), muted speaker, then four small equal solid dots in a centered `2 x 2` grid. The bottom chip sequence and detailed icons are fixed: `深度思考` (intersecting atom/orbits, central dot, one upper-right sparkle), `小艺Work` (circular face/wave emblem), `解锁新小艺` (open circle, tilted `NEW`, lower-left four-point mark), and `修图` (outlined landscape/photo with upper-right sparkle). End the row with a separate `40 vp` glass circle containing three unequal filled four-point sparkles arranged medium upper-left, largest center/lower, smallest lower-right.
- Do not add a standalone bottom-right down-arrow, down-chevron, or scroll-to-latest control; the three-sparkle circle is the only separate circular control at the end of the capability row. Keep the `10 fp` “内容由 AI 生成” notice centered with its visible glyph bottom `4 vp` above the navigation-indicator top. Clip all material blur/tint to the owning app bar, chip, card, composer, or floating control and preserve sharp transcript pixels outside those masks.

## 5. Color and Immersive Light

### Semantic color

- Use semantic tokens rather than raw colors in design and code handoff.
- Token layers: base tokens -> semantic tokens -> component-private tokens.
- Brand and system highlights derive from brand; text/icon hierarchy derives from primary; inverse text/icons use on_primary; component fills use container-related tokens.
- Default brand: Light #FF0A59F7; Dark #FF317AF7.
- Warning: Light #FFE84026; Dark #FFD94838.
- Alert: Light #FFED6F21; Dark #FFDB6B42.
- Confirm: Light #FF64BB5C; Dark #FF5BA854.
- Text/icon tiers use primary, secondary, tertiary, and fourth semantic tokens. Highlight text/icons follow brand.
- Background tokens must be opaque; use semantic background levels to separate windows and layers.
- Support both light and dark mapping. Do not assume the same raw value in both modes.
- Preserve at least the source baseline contrast of 3:1 and raise it when text accessibility requires stronger contrast.
- Define hover, pressed, focus, disabled, selected, active, and click states with interaction tokens.

### Immersive Light

- Use the system Immersive Light material to separate floating controls from overlapping content, not as decoration on every surface.
- Respect the user's three intensity settings: strong, balanced (default), and weak. Define one material level; the system maps it to the chosen intensity.
- Available material hierarchy: Ultra Thin through Ultra Thick.
- Top floating controls: ULTRA_THIN, with gradient blur.
- Bottom floating controls: THIN, with gradient color mask.
- Transient controls that can appear anywhere: THICK.
- Half-modal sheets and large popovers: ULTRA_THICK.
- Protect readability on complex content and in both light/dark contexts.

## 6. System chrome

### Status bar

- Default static phone time to **08:08** unless a scenario-specific time is necessary for accuracy.
- At the right end, reproduce the supplied reference cluster. Physical left-to-right order: NearLink → Wi-Fi 7 → two stacked 5A cellular rows → battery 100; from the screen's right edge inward, use the reverse sequence.
- Preserve the reference symbols, two-line cellular construction, battery number, and relative spacing; use black or white foreground only as required by local contrast.
- Status bar background is transparent by default; extend the page background through it for an integrated appearance.
- Choose black or white status content based on the local background.
- Maintain at least a 1.9 contrast ratio between status-bar content and its local page background.
- Avoid a sharp left/right contrast split behind status items.
- Keep time, connectivity, battery, and other status content clear of the device cutout and rounded top corners.
- On Pura X View portrait, anchor the left status item at `x=32 vp`, the battery's trailing edge at `x=408 vp`, and both groups on the camera's `y=27 vp` optical centerline; their screenshot-scale top visible bound is approximately `17 vp`. Preserve the required 08:08/default right-cluster anatomy; the lock-screen reference supplies placement only.
- Hide only for justified full-screen immersive experiences. Provide a simple gesture to reveal it.
- Phone landscape temporarily hides the status bar by default.
- Split-screen hides the system status bar. A Pura X/Pura X Max-like compact outer display also hides it and releases its vertical space; do not transfer this outer-display rule to the unfolded inner display.

### Lock screen

- Read [lock-screen-visual-defaults.md](lock-screen-visual-defaults.md).
- Derive the large clock tint from the local wallpaper colors, lighten/desaturate it for legibility, and use `78%` reconstructed opacity by default; adjust only within `72–84%` when contrast requires it. Do not default to unrelated opaque white.
- On Pura X View portrait, use two `48 vp` circular lower-shortcut containers at `(16,645)` and `(376,645) vp`. Their bottom edge is `23 vp` above the `28 vp` navigation interaction region. The left glyph is a centered `22 vp` hollow annulus with `4 vp` ring thickness; the right is a centered approximately `16 x 13 vp` camera glyph.
- Build each shortcut from its local wallpaper tint: optional surface about `12%`, thin outline about `68%`, and glyph about `92%` opacity. Keep the wallpaper visible through the circle and prohibit external blur, glow, or broad shadow.
- On other portrait phones, preserve the `48 vp` circular morphology, centers `40 vp` from visible side edges, and the same bottom-system-region relationship unless the verified device safe area requires both controls to move symmetrically.

### Navigation bar

- **Default presence rule:** visibly include the HarmonyOS system navigation bar in every normal full-screen phone app frame, including Pura X Max unfolded portrait. If the state is not clearly one of the documented exceptions, show it.
- Read [navigation-bar-geometry.md](navigation-bar-geometry.md). For logical screen width `W`, use visible-indicator width `112 vp` at `360 <= W < 600`, `W / 3 - 48 vp` at `600 <= W <= 840`, and `W / 4 - 48 vp` at `W > 840`.
- Render the visible indicator as a 6 vp-high capsule, center it horizontally, and position its bottom edge 6 vp above the visible bottom of the screen opening. In a bezeled raster output, use the mapped bezel's center-connected alpha aperture to find that boundary; do not measure from the capsule centerline or from screen rows hidden beneath the bottom bezel.
- Keep a separate invisible interaction region centered at the bottom: width `35%` of `W`, height `28 vp`, bottom edge flush with the visible screen bottom. Do not render this as a 28 vp-high bar or alter the visible UI scale to create it.
- On an ordinary light app surface, continue the app's bottom surface through the navigation region and use the screenshot-derived project default `rgba(0, 0, 0, 0.08)` for the indicator. A substrate near `#F6F6F6` should flatten near `#E3E3E3`. Do not bake that gray as a universal fill. On dark, colored, image, or high-variance backgrounds, use the native system appearance or semantic inversion/adaptation and verify visibility; do not reuse 8% black blindly.
- The earlier `1252 x 84 px`, 42 px radius, and 16 px offset are superseded and must not appear in new outputs. Runtime code must use HarmonyOS system navigation and reported insets rather than hard-coded raster pixels.
- The system navigation bar is software chrome inside the screen opening. A device bezel, app bottom tab bar, toolbar, or floating action control does not replace it.
- Do not omit the bar merely to make a mockup cleaner or to gain vertical space. Omission requires an explicit user override, a floating window, Picture-in-Picture, Pura X/Pura X Max-like compact outer display, the post-timeout hidden phase of a qualifying immersive state, or the defined default for a single static game mockup with no stated phase.
- Navigation-bar adaptation is mandatory for apps, WebView content, and third-party frameworks.
- Provide an immersive background and keep bottom controls clear of the 28 vp interaction region.
- Scrollable content may flow behind the navigation region, but the final content and actions must lift above it.
- A bottom scrollbar must not overlap the navigation bar.
- Lift fixed and floating bottom controls above the navigation bar.
- In half-modals, scroll content may extend behind the navigation area, but bottom actions must remain unobscured. The system navigation bar is above the modal layer.
- Split screen: bottom window or both left/right windows adapt; floating windows and picture-in-picture do not display a navigation bar and must not retain wasted bottom inset.
- In top/bottom split screen, do not over-lift the upper window's bottom controls; only the lower window adapts to the device navigation bar.
- In normal landscape, the navigation bar remains visible and must be adapted; bottom app controls are usually hidden. A Pura X/Pura X Max-like compact outer display is a narrower exception that hides the navigation bar and releases its space.
- Immersive full-screen: navigation bar shows initially and auto-hides after 2 seconds of inactivity; a bottom swipe reveals it. Games require anti-accidental-touch behavior in which navigation takes effect on the second upward swipe.
- For a single static **game** mockup with no phase specified, omit the navigation indicator and represent the post-timeout hidden phase. This is a static-delivery convention only: the actual game still shows the bar initially, hides it after 2 seconds of inactivity, and reveals it on a bottom swipe. For other single static immersive mockups with no phase specified, show the initial/default visible bar. For a sequence, show the visible initial/revealed phase and the post-timeout hidden phase when that transition matters.
- On wide-screen immersive content, fill the available width/height rather than leaving unused bands because of the navigation bar.
- Short video: fill the vertical display and lift bottom controls above the navigation area.
- Read [system-chrome-verification.md](system-chrome-verification.md) before finalizing or reviewing any rendered screen.

### WeChat conversation reference

- Read [wechat-chat-interface.md](wechat-chat-interface.md) when the task explicitly shows WeChat, asks for a WeChat conversation screen, or uses WeChat as the background beneath a system surface.
- Apply the reference only to the app-owned chat layer. Ignore its source screenshot's status bar; HarmonyOS status-bar, navigation geometry, device-bezel, and cutout rules remain authoritative.
- Start the `44 vp` conversation bar below the resolved status region. Use a standalone back chevron in a `48 x 44 vp` leading slot with no `微信` label; center the contact title `22 vp` below the status-region bottom and keep it clear of the punch hole and status/app-bar seam.
- Use a quiet light-neutral conversation field, centered low-emphasis time separators, white incoming bubbles with left avatars, soft green outgoing bubbles with right avatars, and a fixed light composer above the system navigation region.
- In the keyboard-hidden full-screen state, use a `56 vp` composer controls band at `y = H - 84 vp`, with a centered `40 vp` input field, directly adjoining the separate `28 vp` bottom interaction region. Reject an oversized or upward-floating input area.
- Use a `32 vp` trailing add circle whose outer right edge is `12 vp` from the visible logical screen edge (`addCenterX=W-28`). Do not leave an extra visible gutter after the add button.
- Never reproduce the screenshot's contact, avatars, private messages, numbers, or stickers. The screenshot is not an asset and must not be bundled.
- Build the normal card-free WeChat screen first, including messages that naturally begin below its app bar; freeze every title, time, avatar, bubble, and scroll coordinate, then add the Live View above it. In an established chat, at least one earlier separator/message remains behind the expanded card. Reject a clean buffer or first message positioned from `cardBottom + gap`.
- A Live View card or other system overlay covers the frozen conversation without reflowing or pushing it downward unless the requested interaction explicitly changes layout. For expanded phone cards, apply the universal cross-application overlay and occlusion rules below; in WeChat, the covered app-owned region is the complete conversation title bar.

## 7. Multi-window

- Choose by task duration:
  - floating window: temporary secondary task;
  - split screen: sustained parallel tasks;
  - picture-in-picture: supported video/live call/navigation-like continuity.
- Preserve state and continuity across window-mode changes, rotation, font/display changes, and resize. Do not restart or lose task context.
- Reserve the top drag-handle area in floating and split windows. Hide the system status bar in split windows.
- Keep foreground video/game behavior active while another visible window is used, subject to platform policies.
- Resolve audio focus according to user expectation: pause or duck prior media when a new audible task starts.
- Prefer in-app entry points for natural task floating-window or task split-screen activation.
- Phone/folded foldable: at most one floating window. Tablet/unfolded foldable: at most two.
- Phone and foldable floating windows scale proportionally; tablet windows support continuous resizing.
- A tablet 3:2 landscape floating window retains suitable side/bottom navigation and split layout; portrait floating windows return to bottom navigation and single-column content.
- In top/bottom split, keep title, bottom tabs, and core actions complete.

### Picture-in-Picture (画中画)

- Use Picture-in-Picture only to preserve video or video-communication continuity while the user uses another app. Supported scenarios in this source are video playback, live video, video calls, and video conferencing.
- Choose an appropriate entry:
  - fixed in-app control: the user taps a dedicated Picture-in-Picture button;
  - app back: returning to the preceding app level starts Picture-in-Picture, but only when “自动开启画中画” is enabled in system settings;
  - return home: leaving the app for the desktop starts Picture-in-Picture, but only when the same system setting is enabled.
- Start at the system-defined minimum size. On phone, foldable, and tablet, place it at the upper right by default; on a 2-in-1 device, place it at the upper left.
- Resize proportionally by double-tapping to enlarge, dragging the lower-left or lower-right corner, or pinching in/out between the minimum and maximum sizes.
- Drag the window to a screen edge to minimize it into the side floating bar without interrupting the task. Tap the side bar to restore it.
- Use the system-provided control panel. The system owns the display area, control count, functions, and scenario templates; configure only supported controls.
- Show the control panel when the small window starts, hide it after 3 seconds without interaction, and reveal it with a single tap. On a 2-in-1 device, pointer hover also reveals it.

| Scenario | Window controls | Required content control | Optional content controls |
|---|---|---|---|
| Video playback | Close, restore | Play/pause | Previous + next, or fast-forward + rewind; configure only one pair |
| Live video | Close, restore | None | Speaker mute, play/pause |
| Video call | Close and restore appear after any optional control is configured | None | Microphone toggle, hang up, camera toggle, speaker mute |
| Video conference | Close and restore appear after any optional control is configured | None | Microphone toggle, hang up, camera toggle, speaker mute |

- For a video call with no optional controls, show no buttons and restore the app when the user taps anywhere in the Picture-in-Picture window.
- Select either the system-defined portrait or landscape proportion; the system adapts the size from that selected proportion.

| Device state | Portrait default | Portrait maximum | Landscape default | Landscape maximum |
|---|---|---|---|---|
| Phone / folded foldable | Window short edge = 30% of screen short edge | Width = 3 grid columns | Window short edge = 30% of screen short edge | Width = 4 grid columns |
| Unfolded foldable | Window short edge = 30% of folded-state screen short edge | Width = 3 grid columns | Window short edge = 30% of folded-state screen short edge | Width = 5 grid columns |
| Tablet | Window size = 30% of default floating-window size | Width = 4 grid columns | Width = 30% of screen short edge | Width = 5 grid columns |

## 8. Flash Control Ball and Window

### Choose the correct surface

- Use Flash Control Ball (闪控球) to show a small amount of key information and provide a one-tap action outside the app that opens the corresponding app page. Typical scenarios include order grabbing, bookkeeping, and price comparison.
- Use Flash Control Window (闪控窗) to show more key information and support frequent, lightweight cross-app actions or real-time monitoring. Typical scenarios include market monitoring and game streaming.
- Do not confuse Flash Control Window with a system floating window. Flash Control Window carries one app function or partial information and permits only task-related actions; a system floating window can carry the app's full functionality and navigate among app functions.
- Creation is user-initiated from a designated entry inside the app. Tapping either surface returns to the corresponding page in the source app.

### Flash Control Ball

- The system supports at most two balls in total and at most one per app.
- Minimize by dragging the ball into the side bar.
- Delete by dragging one or multiple balls together to the bottom trash target, or by using the long-press menu.
- Select one of four system templates: static layout, plain-text dynamic layout, primary/secondary-text dynamic layout, or emphasized-text dynamic layout.
- Width changes by content tier while height remains fixed:

| Device | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---:|---:|---:|---:|
| Phone portrait/landscape, dual-fold unfolded, tri-fold unfolded | 70 x 40 vp | 80 x 40 vp | 90 x 40 vp | 98 x 40 vp |
| Tablet/PC | 104 x 60 vp | 114 x 60 vp | 124 x 60 vp | 132 x 60 vp |

- These dimensions include the external material base. The internal base has 4 vp left/right inset on phone-family devices and 6 vp on tablet/PC.

### Flash Control Window

- The system displays at most one Flash Control Window. When an app supports both window and ball, allow switching between them.
- Minimize by dragging the window into the side bar or using its minimize button. Delete by dragging it to the bottom trash target or using its close button.
- Provide regular and Mini states. The regular template contains a title bar, drag region, and content region. If both states are supported, place the state-switch control in the app-owned content region.
- Regular-state height is always 75% of the chosen window width. Width must remain within the device-specific interval:

| Device/state | Minimum width | Maximum width |
|---|---:|---:|
| Phone portrait | 30% of screen width | 90% of screen width |
| Phone landscape | 30% of the phone's portrait screen width | 45% of current screen width |
| Dual-fold unfolded | 30% of folded portrait screen width | 55% of current screen width |
| Tri-fold unfolded | 30% of folded portrait screen width | 50% of current screen width |
| Tablet/PC | 10% of screen width | 50% of screen width |

- Mini-state height is fixed at 32 vp; its width follows the regular-state width rules.

## 9. Sharing and Tap-to-Share

### System share

- Invoke the latest native share control through the standard share icon or “分享” action.
- The system sheet owns four regions: content preview, recommendations, sharing methods, and system actions.
- Apps may provide permitted preview content. They may not customize recommendations, sharing-method ordering, or system actions.
- Large-card image/video preview: supply a thumbnail. Best ratio is 1:1 to 1:4; out-of-range content is cropped.
- Selection-style image preview: 3:4 preferred.
- Link + image choice: link thumbnail 1:1 preferred; image 3:4 preferred.
- Horizontal card: use for documents/folders, links, special app formats, or mixed files; provide main/secondary text and a meaningful thumbnail.
- Share-detail pages contain only minimal content required to finish sharing, such as recipient or destination selection.
- Default method area displays 12 methods plus “全部”. Huawei Share stays pinned first; dynamic ordering is system-owned.

### Tap-to-Share (碰一碰)

- Current supported pairs in the supplied baseline: phone-to-phone and phone-to-PC.
- Supported content includes images, video, web/network content, contacts, links, files, Wi-Fi, and personal hotspot as applicable.
- The system owns the wormhole, peer information, and action area. The app selects/provides content for one of the prescribed card templates.
- Image/video previews adapt within 4:1 to 1:4 and crop beyond that range.
- File/Wi-Fi/hotspot card is fixed at 4:3.
- Link preview preferred ratios: 4:3, 1:1, or 16:9. Keep the subject clear and important content away from the lower crop area.

## 10. Notifications and Live View

### Notifications

- Send timely, useful information. Do not duplicate the same content, use notifications as ads/widgets, create complex custom layouts, or force top placement for commercial reasons.
- Use native templates. Single notification includes system app/service icon, title, time, and up to 3 lines of detail.
- Title summarizes the event or function; do not use only the app/service name.
- Tap the whole notification to open the corresponding detail.
- Group multiple notifications from one section. Collapsed group shows the latest three; +N appears above three.
- Image previews should be square, high-quality, content-related, and not repeat the app icon.
- Banner lasts 5 seconds; exceptions such as calls/alarms may persist. Non-immersive banner shows 3 lines; immersive banner shows 1 line.
- Notification title: <= 15 Chinese characters or 22 English characters, one line.
- Detail: <= 57 Chinese characters or 84 English characters, up to 3 lines.
- Desktop badge is numeric and displays at most 99+.
- For every transient Push Notification on a designated phone in portrait orientation, read [push-notification-banner.md](push-notification-banner.md). Use frame `(16,50,W-32,64) vp` and radius `16 vp`; Pura X View resolves to `(16,50,408,64) vp`, but its pixel result is not universal.
- Place the system-resolved `32 vp` app/service icon at local `(12,16)`, start title/detail at `x=56`, trail time by `12 vp`, and center a `48 x 4 vp` system affordance at local `y=54`. Keep the compact banner title and detail to one line each; full notification surfaces retain their native multi-line limits. The affordance is not pure white: derive a light, low-chroma tint from the completed local banner material and alpha-composite it translucently. The screenshot-reconstructed project default mixes the local material `65%` toward local white and renders that tint at `60%` source opacity (about `39%` effective lightening).
- Build the sharp underlay first and overlay the banner without reflow. Its apparent hue comes from the actual local underlay through color-preserving clipped blur; add the screenshot-reconstructed project default 32% neutral-dark overlay and 24% neutral-light hairline, with icon/text independently at full root opacity. Never bake the example's red wallpaper or WeChat identity into other notifications.
- Keep every blur/tint/outline effect inside the `16 vp` rounded mask. Outside it plus one antialias pixel, the banner-present screen must be pixel-identical to the banner-free base. Preserve status/cutout/navigation/bezel geometry and never duplicate the same event as both a Push Notification and Live View.
- For an ordinary expanded/detail notification on a portrait lock screen, read [lock-screen-notification-card.md](lock-screen-notification-card.md). This is a separate component from the transient top banner and the collapsed lock-screen icon/count state.
- Let `S_top` be the resolved top edge of the lower lock-screen shortcuts and `M=max(16 vp, verified side safe insets)`. Use frame `(M, S_top-91, W-2M, 64) vp` with radius `16 vp`, which simplifies to `(M,H-190,W-2M,64)` under the standard shortcut relationship. Pura X View resolves to `(16,554,408,64) vp`; Pura 90 Pro Max to `(16,633,342,64) vp`; Pura X Max unfolded portrait to `(16,750,633,64) vp` before device-specific safe-area adjustment.
- Inside the lock-screen card, place the native `32 vp` logo at `(12,16)`, start title/detail at `x=56`, trail the time by `12 vp`, and use one line each for title and detail. Omit the transient-banner bottom handle. The title describes the sender/event/function rather than mechanically repeating the app name.
- Construct the lock-screen card from the actual local wallpaper with clipped color-preserving thin glass, a wallpaper-derived low-chroma tint at the reconstructed `28%` default, and a subtle neutral-light outline at the reconstructed `40%` default. Keep icon/text independently opaque; never reuse the example's app, message, or red hue. Blur/tint/shadow may not change any pixel outside the rounded mask plus one antialias pixel.
- Respect the system's lock-screen preview setting. When preview is disabled, redact private title/detail content according to native behavior rather than exposing the sample or invented sensitive content.

### Live View (实况窗)

- Read [live-view-sketch-spec.md](live-view-sketch-spec.md) for unaffected forms and [expanded-live-view-card.md](expanded-live-view-card.md) for every expanded phone card. The Pura X View full-canvas reference supersedes conflicting expanded-card geometry, placement, radius, material, and local-region values only; it does not override eligibility, lifecycle, privacy, text, color, or interaction rules.
- Use only for a time-sensitive, bounded, changing, user-expected, high-value ongoing activity.
- Do not use for static permission status, standby state, distant future reminders, weather snippets, movie tickets, advertising, or forced prominence.
- Define an explicit start and end. Auto-clear shortly after completion.
- Avoid duplicating the same event as a normal notification.
- Redact private information and keep emphasis color consistent across capsule/card/lock-screen forms.
- Only one form of the same activity appears in a given context. No status-bar capsule when its landing page is foreground; notification center/lock screen do not duplicate the status capsule.
- Capsule holds the smallest glanceable content. Prefer two text segments: main 1-3 Chinese characters, secondary 1-6.
- Card structure: required fixed region; optional auxiliary and extension regions. Auxiliary region is 44 x 44 vp; a system-style action may occupy up to 44 x 70 vp.
- Base/collapsed card: `336 x 72 vp` with radius `16 vp` when no extension is present. Do not apply this fixed width or radius to an expanded phone card.
- Expanded phone card: for logical canvas width `W`, calculate `Cw=W-32` and `Ch=Cw x 6/17`; use frame `(16,50,Cw,Ch) vp` and radius `20 vp`. Calculate in logical units without premature rounding, convert to the designated raster mapping, and round final pixel edges once.
- Expanded phone-card overlay behavior is universal across eligible apps and scenarios: build a complete normal app state first, freeze its layout and scroll position, then composite the card above it. Every app-owned element must keep `deltaX=0` and `deltaY=0`; no app value may depend on `cardY`, `cardHeight`, `cardBottom`, or a card-clearance spacer. Leave the HarmonyOS status bar visible and perceptually occlude the app-owned top/title region beneath the card. Do not create an empty band or start content at `cardBottom + gap`; normally preceding content remains in place under the card. Pura X View screenshots are reference results, not reusable pixel coordinates for another model.
- Expanded local regions: fixed `(12,10,Cw-80,52)`, optional auxiliary `(Cw-56,14,44,44)`, extension `(12,72,Cw-24,Ch-84)` vp. Keep the 32 x 32 vp app icon at `(12,20)`, primary/secondary text starting at `x=56`, 12 vp icon-to-text gap, and 12 vp trailing inset. Adapt optional extension content rather than clipping when height is limited.
- Measured capsule states: default `80 x 28`, expanded `128 x 28`, both with Sketch fixed radius 16. Icon slot is `(2,2,24,24)`, visible icon is `(5,5,18,18)`, first text slot is `(29,6,45,16)`, and expanded second text slot is `(80,6,45,16)`.
- Place the system-owned capsule by device hardware: centered with a centered punch hole; left on side-punch/no-hole devices. Use default on ordinary portrait phones and expanded only when the actual landscape/foldable/tablet status-bar host has verified space. Never copy documentation-artboard coordinates into a device mockup.
- Expanded phone-card material in every eligible scene and on every mapped phone uses this bottom-to-top stack: actual frozen underlay -> clipped backdrop blur that preserves broad hue/luminance -> neutral-dark **overlay layer** at 48% -> thin neutral outline at 25% -> independent full-strength content, all inside a 100%-opacity root group. Large saturated underlay regions must create softened local color variation while all text/icons/boundaries beneath remain unrecognizable. Never replace the response with uniform gray, bake sampled colors or a decorative gradient into the material, add a second gray/neutral fill or white haze, globally desaturate/replace color, reduce parent opacity, or alter the required 48% overlay to expose more color. The verified backdrop blur 50 may remain when an explicit design-tool value is needed. The older white-60%/black-82% and radius-16 template treatment is scoped to the unaffected base/collapsed card only.
- Calculate expanded-card blur on an offscreen underlay copy with kernel padding, crop it to the card rectangle, then apply the final 20 vp rounded alpha mask **after** filtering. Never blur a pre-masked layer in a way that expands alpha, or place blur/backdrop filters on the app root, screen, card parent, or completed composite. Blur/tint/gray must stop at the rounded boundary. Default to no external shadow; reject broad shadow, haze, bloom, glow, or any softened area outside the card.
- For raster delivery, compare the card-present frame with its same-size card-free base using `scripts/validate_live_view_blur_boundary.py`. Outside the rounded card plus a one-pixel antialias ring, require zero changed pixels and unchanged sharpness.
- Compact circular outer-display template: 224 x 224 circular design canvas. Keep important illustration content inside the actual circular safe area and verify cropping on the target mask; do not apply it to unfolded rectangular displays.
- Choose the template that matches the task: base, progress visualization, emphasized text, left/right text, sports score, or navigation.
- Progress supports 2-5 nodes. Use one consistent application emphasis color.
- Card fixed-region text limits:
  - without auxiliary: main 16 Chinese / 23 English; secondary 19 Chinese / 28 English;
  - with auxiliary: main 13 Chinese / 18 English; secondary 15 Chinese / 22 English.

## 11. Service cards

- A service card presents timely, core, useful information and lightweight direct action. It is not a shortcut grid, mini app, ad, or traffic entry.
- Small cards show 1-2 information points. Larger sizes may add relevant detail and interaction; do not merely enlarge the same layout.
- Recommend shipping a 2 x 2 small card for broad compatibility.
- Do not infer a universal outer card width/height from the grid name. Use the actual host grid, target device, or official component resource; otherwise specify responsive behavior without an invented dimension.
- Default to one whole-card hotspot. If multiple hotspots are essential, separate them clearly and give each a pressed response.
- Do not use long press, drag, multi-touch, repeated tap, horizontal swipe, or multi-step flows inside a card. Avoid vertical scrolling unless truly necessary.
- A card tap enters the exact matching app/service content. Do not open a popover or half-modal from within the card.
- Return behavior should respect “where the user came from”: the global back gesture returns to the card; in-page back traverses app hierarchy.
- Card name: ideally 2-7 Chinese characters, maximum 30. Description maximum 255.
- Card editing uses the system template and no more than two page levels. Do not place an ad hoc “编辑” affordance directly on the card.
- Passive refresh timing uses 30-minute increments; choose a cadence that matches real user need and power cost.
- Use small element change, number slide, fade, or directional replacement to avoid abrupt refresh.
- Card deliverables use a straight-edged rectangle. The host applies runtime corner clipping.
- Design-preview radii: 18 vp for 1 x 2 and 2 x 2; 22 vp for 2 x 4 and 4 x 4.
- Keep content at least 12 vp from card edges.
- Default desktop colors: Light #FFFFFF; Dark #2E3033 when not using system blur. Lock-screen cards are monochrome with transparency/blur and no hue.
- Typical 1 x 2 text: title 14 fp, secondary 12 fp, numeric 20 fp.
- Typical 2 x 2 text: title 14/18 fp, secondary 12/14 fp, numeric 32/40 fp.
- Card font scaling is capped below 1.3x; type larger than 20 fp and lock-screen card text do not respond to large-font/elder mode in this baseline. Selectively scale key text and verify usability.
- Card interactive visual >= 24 vp; touch region >= 40 vp.
- Recommended round button visual: 32 x 32 vp for 1 x 2, 30 x 30 vp for 2 x 2. Capsule button height 36 vp; text 14 fp Medium.
- Snapshot must match a real representative card state, have square corners, include light/dark variants, and contain no advertising.
- Provide offline/loading placeholders. Placeholder colors: tier 1 = 10% black Light / 40% white Dark; tier 2 = 5% black Light / 20% white Dark. Radius 4 vp when height > 10 vp, otherwise 2 vp.
- Interactive out-of-bounds card effects are desktop-only and optional:
  - stable state: top <= 16 vp, left/right/bottom <= 8 vp;
  - transition state: all sides preferably <= 56 vp;
  - return interaction-triggered effects to default within 1 second;
  - non-desktop contexts must show the regular in-bounds card.

## 12. Security and privacy branding

- Read `references/security-privacy-branding.md` for every HarmonyOS security/privacy design, prototype, image-generation prompt, system alert, notification, launch visual, and developer handoff.
- Apply the official shield to HarmonyOS anti-fraud, secure-preview, permission-recall, privacy-protection, risk-warning, sensitive-operation, and related safety-education experiences whenever a branded emblem is present.
- Asset priority: original `.ai` source, then SVG, then transparent PNG. Place the supplied artwork directly; do not redraw or generatively recreate it.
- Preserve the full shield aspect ratio, silhouette, split at the top and bottom, central blue bar, clear space, and transparency.
- Standard artwork uses black shield geometry and a `#1F69FF` center mark. Treat the `.ai` source as authoritative for exact geometry and color.
- Do not stretch, rotate, skew, add perspective or shadows, crop the shield, alter its stroke or spacing, or add decorative shapes inside it.
- Do not add a colored icon tile behind the shield unless another HarmonyOS specification explicitly requires that container.
- On dark or complex backgrounds, improve the surrounding surface or use a light/neutral container rather than recoloring the logo. Use another colorway only when an official alternate asset is supplied.
- Convey urgency through copy, hierarchy, and native system alert styling—not by recoloring the official shield red or orange.

## 13. Delivery checklist

- Unless the user explicitly requested native/original resolution, a high-resolution final, print/final-delivery quality, or exact pixels, deliver only a lightweight preview. Do not also create or attach a native-size file.
- When preview dimensions must be chosen, keep the longest edge at or below 1600 px and preserve the approved aspect ratio, composition, logical geometry, device identity, bezel/cutout placement, and relative coordinates. Record one uniform preview scale for all layers.
- End a lightweight-preview response once with: “这是轻量预览版；如果您确认效果满意，我可以继续生成原生尺寸版本。” Omit this sentence only when native/original-size output was explicitly requested and delivered.
- Name the target device(s), window mode(s), orientation(s), and system surface.
- For Pura X Max unfolded landscape, verify the official bezel is rotated 90 degrees clockwise, its front camera is upper-right, the UI remains correctly oriented, and all alpha/seam checks were rerun on the rotated asset.
- For Pura X View landscape, verify the screen is 2232 x 1320 px / 744 x 440 vp, the official portrait bezel was rotated exactly 90 degrees counterclockwise before fresh alpha-aware compositing, and the front-facing camera is on the left side.
- For every Pura X View orientation, verify the corrected camera remains a clean 22 vp circle with no square backing. In portrait, also verify `(220,27) vp` camera center and the `32 vp` status-edge anchors.
- For every lock screen, verify the clock and lower shortcuts derive their hue from the actual wallpaper, use the prescribed translucent hierarchy, remain confined to their glyph/container masks, and preserve the exact shortcut morphology and bottom-system-region clearance.
- For every expanded/detail lock-screen notification, verify the responsive frame and `27 vp` shortcut gap, native `32 vp` logo, aligned title/detail/trailing time, absence of the transient-banner handle, wallpaper-derived clipped glass, lock-screen-preview privacy behavior, and zero changed base pixels outside the card mask plus one antialias pixel.
- For visuals with hands, people, or environments, verify the named phone and its exact portrait/landscape orientation came from a completed validated device master; the hand/scene layers and foreground occlusion mask remain separate, and every unoccluded device pixel and landmark is unchanged. Apply this check to all models without exception.
- For every phone-in-hand contact, verify the contact map, background → rear hand → frozen device → foreground hand layer order, device-derived grip ergonomics, complete fingertips/nails, clean matte edges, coherent left/right exposure, zero background seam at declared contact, zero foreground hand coverage on behind-device bezel segments, zero frame-through-skin, and zero unexplained differences outside the latest local edit region. Preserve genuine anatomical clearance.
- Show pixel presentation size and vp/fp implementation dimensions separately.
- Verify every applicable static phone time is 08:08 and every right-side status cluster matches the NearLink/Wi-Fi 7/dual-5A/battery-100 reference anatomy and order.
- Verify every present phone navigation indicator is a centered 6 vp-high capsule whose bottom edge—not its centerline—is 6 vp above the bezel-derived visible screen bottom and whose width matches the current logical `W`; separately verify the centered, bottom-anchored `35% W x 28 vp` interaction region and require app content to clear it.
- For every transient portrait Push Notification banner, verify `(16,50,W-32,64) vp`, radius `16 vp`, the responsive icon/title/detail/time/affordance layout, actual-underlay color response beneath the reconstructed 32% neutral-dark overlay and 24% outline, a wallpaper-responsive translucent affordance rather than fixed pure white, once-rounded raster edges, and zero changed pixels outside the rounded banner plus one antialias pixel.
- For every Xiaoyi phone interface, verify the screenshot status bar was ignored; `E`, `T=E+8 vp`, and active column `K` were resolved; all shell buttons use clipped glass material; the call button uses small-upper/large-lower sparkles, the more button uses four small solid dots, and all four chip glyphs preserve their specified anatomy; the three-sparkle circle is present and no standalone bottom-right down-arrow or scroll-to-latest control is present; user turns have a square upper-right corner and rounded other corners; the AI notice has the `4 vp` indicator gap; and the composer is `(E,*,K-2E,48) vp` above the system navigation region.
- When a mapped phone shows its default home screen, use the corresponding supplied PNG without redesign, crop, reflow, relabeling, or substitution. For another phone, preserve the supplied home-screen icon/widget design and layout language.
- For every rendered phone, verify the official bezel remains unchanged above a separate fully opaque screen layer. A native final uses the native bezel and documented screen resolution; a lightweight preview uses one uniform proportional scale for the complete composition while preserving the documented aspect ratio and geometry.
- Verify that the visible UI coordinates were not moved, stretched, or rescaled for seam coverage and that alpha-derived edge-pixel extrusion covers the upper, bottom, left, right, and all four diagonal corner lips.
- Run the deterministic helper and require zero uncovered pixels for the upper edge, bottom edge, left edge, right edge, upper-left corner, upper-right corner, bottom-left corner, and bottom-right corner. Also require zero exterior screen leakage and zero exterior-alpha mismatch.
- Inspect the complete four inner edges, four corners, and edge/corner transitions at 400% or an equivalent pixel-level comparison on white, black, and a saturated diagnostic background.
- Reject any white/background seam, transparent gap, one-pixel hairline, exposed mask boundary, incorrect curve, missing-underlay halo, edge/corner discontinuity, exterior leakage, or modified bezel pixel/proportion. Re-composite from the original layers instead of retouching an edge/corner or repairing it generatively.
- **Observable acceptance criterion:** “The active screen continuously meets the official bezel’s antialiased inner boundary across the complete upper, bottom, left, and right edges and all four corners. Every partially or fully transparent inner-aperture pixel has opaque screen content beneath it, every directional uncovered-pixel count is zero, and no screen content leaks outside the official device silhouette.”
- Include compact/medium/expanded or relevant fold/window variants.
- Mark safe areas, hinge zones, keyboard avoidance, and system-owned chrome.
- Map every recurring color, radius, spacing, and type style to a token.
- Show light/dark and meaningful interaction states.
- Include large text, screen reader, reduced motion, muted/no-haptic, interruption, offline, error, and recovery behavior when relevant.
- Use the correct native system flow for sharing, notifications, Live View, cards, and multi-window.
- For every Live View output, verify the selected base/collapsed, responsive expanded phone-card, `80 x 28 vp` capsule, `128 x 28 vp` expanded capsule, lock-screen, or circular outer-display form. For expanded phone cards, require frame `(16,50,W-32,(W-32)x6/17) vp`, radius 20 vp, responsive regions, actual-underlay color-preserving blur beneath the 48% neutral dark overlay and 25% neutral outline, spatial material response without recognizable underlying detail, post-blur rounded-mask clipping, zero changed pixels outside the one-pixel boundary allowance, once-rounded raster conversion, aperture/status collision clearance, and no fixed-size, flattened-gray, or blur-leaking legacy rule. Align capsules to the actual cutout/status-bar host and reject simultaneous capsule/card presentation for one activity in one context.
- For Picture-in-Picture, confirm scenario eligibility, auto-start setting dependency, system-owned control template, default corner, proportional resizing, minimization/recovery, and device/fold-state size limits.
- For Flash Control Ball/Window, confirm scenario eligibility, quantity limits, state transitions, system-owned controls, and device-specific dimensions.
- For HarmonyOS security/privacy work, verify the official shield asset was placed directly, remains uncropped and unmodified, and retains its standard colors and adequate contrast.
- State what is app-owned, system-owned, configurable, fixed, cropped, or automatically adapted.
- For demos, label intentional deviations from production behavior.
