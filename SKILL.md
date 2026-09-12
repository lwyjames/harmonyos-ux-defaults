---
name: apply-harmonyos-ux-defaults
description: Apply the user's global HarmonyOS UX baseline, Pura X Max-like wide-foldable rules, mandatory mapped phone bezels, and official security/privacy branding to UX requirements, flows, screen designs, wireframes, mockups, image prompts, clickable or frontend prototypes, service cards, notifications, Live View, Picture-in-Picture, Flash Control Ball/Window, sharing, messaging and WeChat conversation screens, multi-device experiences, and handoff packages. Invoke automatically when a UX or prototype task lacks a different platform specification, and whenever HarmonyOS or Huawei devices, security/privacy, anti-fraud, secure preview, permission recall, phone OS UX, system surfaces, video continuity, cross-app floating controls, mobile apps, wide foldables, compact outer displays, Pura X/Pura X Max-like ratios, foldables, tablets, PCs, watches, cockpit displays, or cross-device continuity are involved. Also use when reviewing a design for compliance with the user's default UX standard.
---

# Apply HarmonyOS UX Defaults

Use the supplied HarmonyOS developer design documentation as the user's default UX baseline. Treat it as a working specification, not visual inspiration.

## Resolve precedence

Apply rules in this order:

1. Follow the user's explicit instruction in the current request.
2. Preserve approved project-specific decisions, source-of-truth manifests, supplied screenshots, and named target-platform conventions.
3. Apply this HarmonyOS baseline.
4. Use general UX judgment only where the baseline is silent.

Do not let a generic rule overwrite a locked project decision. If the user explicitly targets iOS, Material Design, Windows, web, automotive, or another design system, use that system for platform-specific chrome and components; retain compatible cross-platform principles such as responsiveness, clear hierarchy, native interaction, accessibility, and state continuity. If the platform is unspecified, default to HarmonyOS.

## Start every task

1. Identify the target device, window state, orientation, system surface, input modes, and expected deliverable.
2. Read [quick-reference.md](references/quick-reference.md) in full.
3. Whenever the deliverable renders text, read [harmonyos-sans-font-assets.md](references/harmonyos-sans-font-assets.md). Resolve the locale-appropriate external font with `scripts/resolve_harmonyos_fonts.py` before final high-fidelity rendering. On Windows, prefer the configured external font directory. In ChatGPT Work/cloud, use the exact account asset `HarmonyOS+Sans.zip` when available, materialize and extract it only into temporary task storage, and checksum-verify it. Do not create a font-only dependent skill and do not silently substitute a different font.
4. For every screen or prototype that includes system chrome, read [system-chrome-verification.md](references/system-chrome-verification.md). When the navigation bar is present, also read [navigation-bar-geometry.md](references/navigation-bar-geometry.md). Resolve status-bar and navigation-bar behavior per state before positioning app-owned content.
5. For phone mockups, prototypes, or rendered screens, read [device-preview-frames.md](references/device-preview-frames.md) and use the mapped bezel asset.
6. Whenever a phone home screen, launcher, desktop, status bar, or navigation bar appears, read [home-screen-defaults.md](references/home-screen-defaults.md) and apply its exact mapped assets and raster-chrome requirements.
7. Whenever a request explicitly shows WeChat, asks for a WeChat conversation, or uses a WeChat chat as the background beneath a system surface, read [wechat-chat-interface.md](references/wechat-chat-interface.md). Apply it only to the app-owned chat layer; ignore the reference screenshot's status bar and keep HarmonyOS system chrome authoritative. Never bundle or reproduce the source screenshot or its private content.
8. For a Pura X/Pura X Max-like wide foldable, a similarly proportioned compact screen, an outer-screen experience, or a fold/unfold transition, read [wide-foldable-pura-x-max.md](references/wide-foldable-pura-x-max.md). Apply its outer-screen rules only to the outer/compact display state, not automatically to Pura X Max unfolded portrait.
9. Use [source-index.md](references/source-index.md) to select every relevant extracted source text. Read the selected text completely before making detailed design decisions.
10. For any 实况窗/Live View card, capsule, expanded capsule, or compact circular outer-display treatment, read [live-view-sketch-spec.md](references/live-view-sketch-spec.md). For every expanded phone Live View card, also read [expanded-live-view-card.md](references/expanded-live-view-card.md); its responsive geometry, placement, radius, material, and internal-region rules supersede conflicting expanded-card values from the older Sketch template without changing other Live View forms or behavior.
11. Open or render the matching source PDF when diagrams, component anatomy, examples, crop behavior, safe areas, or visual relationships affect the answer. The PDF controls over extracted text when extraction loses layout.
12. State any consequential assumption. Do not invent a HarmonyOS component, token, behavior, or numerical value when the sources are silent.
13. Before emitting an exact value that is not in the quick reference, locate it in the selected source text, the Live View Sketch reference, or the relevant PDF figure. If it cannot be verified, omit it or label it as a project recommendation rather than a HarmonyOS requirement.

## Global defaults

- Default unspecified mobile OS work to HarmonyOS NEXT visual and interaction language.
- Use Simplified Chinese for user-facing screen copy unless the user requests another language. Write specifications and handoffs in the language requested by the user.
- Use the checksum-verified external `HarmonyOS_Sans_SC.ttf` as the default font binary for Simplified Chinese and mixed Chinese/Latin HarmonyOS UI. Select the locale-appropriate supplied HarmonyOS Sans file for other languages and treatments. Keep all font binaries outside this skill, never modify or subset them, and never silently substitute another font in a final high-fidelity output. Follow [harmonyos-sans-font-assets.md](references/harmonyos-sans-font-assets.md).
- For every unspecified UX design requirement that needs a phone, default to Pura X Max unfolded portrait at 1828 x 2584 px and 665 x 940 vp. Use `assets/device-bezels/pura-x-max-unfolded-portrait.png` as its bezel. A current-request device, state, orientation, or bezel instruction overrides this default.
- For Pura X Max unfolded landscape, use 2584 x 1828 px and 940 x 665 vp. Rotate the official portrait bezel **90 degrees clockwise** before compositing so its front-facing camera is at the upper-right corner. Rotate only the untouched bezel source; render the UI separately in landscape and re-run alpha-derived aperture compositing. Never rotate a finished portrait composite.
- Treat Pura X Max unfolded portrait as an inner/unfolded state. Do not hide its status/navigation bars or remove its multi-window support solely because the new wide-foldable supplement contains outer-screen rules. Resolve the screen role, fold state, and current window dimensions first.
- Include the corresponding designated phone bezel around every phone screen in every visual UX output by default. This applies to wireframes, high-fidelity mockups, screen-flow panels, keyframes, generated images, presentation visuals, and prototype previews. Omit the bezel only when the user explicitly requests a bezel-free, screen-only, raw-canvas, or implementation-only asset.
- Visibly render the HarmonyOS system navigation bar inside every normal full-screen phone app frame by default, including the default Pura X Max unfolded portrait frame. Do not omit it for visual cleanliness, extra content space, or because a hardware bezel is present. Omit it only when the user explicitly requests otherwise or the documented state is a floating window, Picture-in-Picture, Pura X/Pura X Max-like compact outer display, or the hidden phase of a qualifying immersive experience.
- In every phone canvas where the navigation bar is present, render the visible indicator as a horizontally centered **6 vp-high capsule** whose bottom edge is **6 vp above the visible bottom of the screen opening**. Let `W` be the current logical screen width: use width `112 vp` for `360 <= W < 600`, `W / 3 - 48 vp` for `600 <= W <= 840`, and `W / 4 - 48 vp` for `W > 840`. Derive the visible screen bottom from the mapped bezel's center-connected alpha aperture in a bezeled raster output. Keep the separate invisible, bottom-anchored interaction region at `35%` of `W` by `28 vp`; app-owned bottom content must clear this region. Do not reuse the superseded fixed `1252 x 84 px`, 42 px radius, or 16 px offset.
- For ordinary light app surfaces, continue the app's bottom surface behind the navigation region and render the indicator with the screenshot-derived project default `rgba(0, 0, 0, 0.08)`. On a surface near `#F6F6F6`, the expected flattened result is near `#E3E3E3`. Treat this as a neutral translucent system-chrome convention, not an official recovered token or an opaque fixed gray. For dark, colored, image, or high-variance backgrounds, use system semantic inversion/adaptation and verify visibility rather than reusing 8% black. Follow [navigation-bar-geometry.md](references/navigation-bar-geometry.md).
- Default static phone time to **08:08** unless the user or scenario requires another time. At the status bar's right end, follow `assets/system-chrome/status-bar-right-default-reference.png`: left-to-right NearLink, Wi-Fi 7, dual stacked 5A signals, and battery 100.
- For the Pura X Max unfolded portrait, Pura X View front, and Pura 90 Pro Max portrait default home screens, use their exact mapped PNGs in `assets/default-homescreens/`. For other phones, preserve the masters' icon/widget design and layout language while adapting to the documented canvas.
- Treat pixel dimensions as mockup canvases, never as fixed implementation geometry. Annotate logical layout in vp/fp.
- Treat the mapped official bezel PNG as the sole source of truth for screen-opening geometry, corner curves, antialiasing, camera position, frame/hinge details, and transparency. Never approximate its aperture with a manually drawn rounded rectangle, guessed radius, generic device mask, or hard-coded geometry unless the bezel package explicitly supplies those exact values.
- Render the app UI as a separate, fully opaque screen layer at the documented screen resolution and aspect ratio. Preserve its visible screen coordinates: never shift, stretch, or rescale the visible UI merely to cover a bezel seam.
- Place the screen layer beneath the official bezel and create hidden overscan by extruding its first/last rows, first/last columns, and four corner pixels beneath the upper, bottom, left, right, and diagonal corner lips. Derive each side's overscan independently from that bezel's alpha transition band plus a small hidden safety margin; never apply one universal bleed value to every asset.
- Derive the interior aperture and exterior transparent component programmatically from the official bezel alpha channel. Every partially or fully transparent inner-aperture pixel must have fully opaque screen content beneath it, while no screen content may enter the exterior transparent component. Never substitute a generic rounded-rectangle mask.
- Composite the unmodified official bezel as the final top layer at native pixel dimensions. Do not resize, stretch, crop, recolor, redraw, or generatively recreate it, and do not resize the completed composite after the bezel is applied. The only standard orientation transform is the exact 90-degree clockwise source-bezel rotation required for Pura X Max unfolded landscape.
- When no mapped or supplied bezel exists, depict the front-facing camera as one simple round dot rather than a notch or Dynamic Island.
- Prefer HarmonyOS system components and native system flows, including Picture-in-Picture and Flash Control Ball/Window when the use case qualifies, over custom imitations.
- Use system semantic tokens rather than isolated raw color values. Define both light and dark behavior.
- Use responsive, mobile-first layout. Do not stretch one fixed phone composition across other windows.
- Preserve safe areas, status/navigation behavior, hinge avoidance, keyboard space, large text, and multi-window continuity.
- Keep the user's primary task unobstructed. Decorative motion, immersive materials, AI, cards, notifications, and system surfaces remain subordinate to utility and system priority.

## Official security & privacy branding

For any HarmonyOS security- or privacy-related UX, prototype, mockup, keyframe, system alert, notification, launch visual, or developer handoff, read and follow [security-privacy-branding.md](references/security-privacy-branding.md).

When a branded security/privacy emblem or shield visual is required, use the official user-provided 鸿蒙星盾安全 standard-color shield asset from `assets/branding/`. Do not invent, redraw, approximate, or generatively recreate a substitute shield. Preserve the official geometry, proportions, transparency, and standard colors. Prefer placing the supplied asset directly into the composition. Use the transparent asset for raster workflows; when a dark background would reduce contrast, change the surrounding container or surface rather than recoloring the logo unless an official alternate colorway has been supplied.

## Design workflow

### 1. Select the system pattern

Determine whether the request belongs in an app page, system share sheet, notification, Live View, service card, Picture-in-Picture, Flash Control Ball/Window, multi-window mode, Tap-to-Share flow, or another system surface. Use the native pattern and its stated limits. Do not substitute a visually similar custom surface.

When Live View is selected, use the documented forms instead of a generic notification or guessed pill: `336 x 72 vp` base/collapsed card, responsive expanded phone card, `80 x 28 vp` default status-bar capsule, or `128 x 28 vp` expanded capsule when verified status-bar space permits. For an expanded phone card on logical canvas width `W`, use frame `(16, 50, W - 32, (W - 32) x 6 / 17) vp`, radius `20 vp`, blurred underlay, neutral dark overlay at 48% opacity, and a thin neutral outline at 25% opacity. Treat the capsule as system-owned: center it with a centered punch hole, place it left on side-punch/no-hole devices, and preserve collision behavior with fixed status content. Read [live-view-sketch-spec.md](references/live-view-sketch-spec.md) and [expanded-live-view-card.md](references/expanded-live-view-card.md) for exact scope, local regions, material, circular outer-display treatment, and verification.

### 2. Define responsive structure

Specify the logical vp/fp canvas, safe-area treatment, grid, margins, gutters, breakpoints, and layout transformation. Cover the states that materially affect the experience: compact/medium/expanded width, portrait/landscape, fold/unfold or hinge, split/floating window, keyboard, and large text.

### 3. Resolve system chrome

Before placing app-owned top or bottom controls, decide the status bar and navigation bar for every relevant state. Record whether each bar is visible, temporarily hidden, absent, or system-owned; define the content/background extension, status-content color, cutout avoidance, bottom interaction region, scroll-end behavior, modal layering, and reveal gesture. If no qualifying exception is identified, set the navigation bar to **visible** and calculate its responsive logical geometry from [navigation-bar-geometry.md](references/navigation-bar-geometry.md): 6 vp visible height, 6 vp bottom-edge gap, centered responsive width, and a separate bottom-anchored `35% W x 28 vp` invisible interaction region. Default static time to 08:08 and render the reference NearLink/Wi-Fi 7/dual-5A/battery-100 cluster at the right. For a single static immersive mockup with no phase specified, show the initial/default visible state; for a multi-frame immersive sequence, show both the initial/revealed state and the post-timeout hidden state when relevant. Use [system-chrome-verification.md](references/system-chrome-verification.md) as the required state matrix and acceptance checklist. Do not apply a single fixed inset to normal, split, floating, Picture-in-Picture, immersive, landscape, keyboard, and compact outer-display states.

### 4. Apply visual tokens

Use the HarmonyOS typography roles, semantic colors, spacing levels, and hierarchical corner radii. Resolve the locale-appropriate checksum-verified external HarmonyOS Sans file before rendering text, and use its exact path rather than an unverified family lookup. Use Immersive Light only where an overlaying control needs separation from content and select its material level by placement.

### 5. Define interaction and system states

Show default, pressed, selected, disabled, loading, empty, offline, error, permission-denied, interruption, and recovery states when relevant. Preserve task state across rotation, resizing, folding, window-mode changes, exit, restart, and notification dismissal when the flow requires continuity.

### 6. Write UI copy

Use concise, respectful, action-oriented Chinese. Lead with user value or the actionable result. Use native terminology and the source punctuation/spacing rules. Avoid technical jargon, inflated marketing language, repeated context, and unnecessary exclamation marks.

### 7. Composite the device bezel

For every rendered phone, retain separate app-screen and official-bezel source layers. Render the screen fully opaque at the documented resolution and aspect ratio. Preserve its visible coordinates, then create hidden overscan by extruding the first/last rows and columns plus the four corner pixels beneath all four bezel lips and corners. Calculate top, bottom, left, and right overscan independently from the mapped bezel's alpha channel. Separate the center-connected opening from exterior transparency, clip the underlay against the exterior component, and composite the untouched bezel last at native size.

Use `scripts/composite_validate_bezel.py` for deterministic raster compositing and validation. Do not substitute a manual rounded rectangle or generative repair. Read [device-preview-frames.md](references/device-preview-frames.md) for the required command, diagnostics, and interpretation.

### 8. Verify before delivery

Check:

- platform pattern and system surface are correct;
- every phone screen in every visual output is enclosed by the corresponding designated bezel unless the user explicitly requested a bezel-free or screen-only deliverable;
- the mapped official bezel remains pixel-identical in dimensions and proportions, and no manually estimated rounded-rectangle or generic aperture mask controls the screen opening;
- the app-screen source is fully opaque at the documented resolution/aspect ratio, its visible coordinates remain unchanged, and its edge pixels are extruded into independently calculated upper, bottom, left, right, and diagonal hidden overscan;
- every rendered phone passes bezel-seam inspection at 400% zoom or an equivalent pixel-level check across the complete upper, bottom, left, and right inner edges, all four corners, and every straight-edge/corner transition on white, black, and a saturated diagnostic background;
- automated validation reports zero uncovered pixels separately for the upper edge, bottom edge, left edge, right edge, upper-left corner, upper-right corner, bottom-left corner, and bottom-right corner; every inner-aperture pixel with official-bezel alpha below full opacity has fully opaque screen content beneath it;
- the final exterior transparency matches the official bezel silhouette, with zero screen pixels in the exterior transparent component;
- there is no white or background-colored seam, transparent gap, one-pixel hairline, exposed mask edge, incorrect corner curvature, missing-underlay halo, straight-edge/corner discontinuity, or screen-content leakage outside the device silhouette;
- **Acceptance criterion:** “The active screen continuously meets the official bezel’s antialiased inner boundary across the complete upper, bottom, left, and right edges and all four corners. Every partially or fully transparent inner-aperture pixel has opaque screen content beneath it, every directional uncovered-pixel count is zero, and no screen content leaks outside the official device silhouette.”
- any bezel-seam failure causes rejection and recompositing from the original app-screen layer and official bezel; never retouch individual edges/corners or repair them generatively;
- no content or primary control is clipped, obscured, or placed in a hardware/gesture/hinge exclusion area;
- layout responds at relevant breakpoints instead of merely scaling;
- semantic colors work in light/dark mode with readable contrast;
- type hierarchy uses fp and supports system text scaling;
- the final high-fidelity renderer uses the locale-appropriate external HarmonyOS Sans file whose size and SHA-256 pass `scripts/resolve_harmonyos_fonts.py`; no synthetic style, modified font, or silent fallback is present;
- spacing and radii use defined tokens or justified exceptions;
- every frame/state records whether the status bar and navigation bar are visible, temporarily hidden, absent, or system-owned, with the correct reason;
- every normal full-screen phone app frame visibly contains exactly one HarmonyOS system navigation indicator inside the screen opening; a hardware bezel or app bottom tab/toolbar does not count as the system navigation bar;
- every present navigation indicator is a 6 vp-high capsule, is horizontally centered, has its bottom edge—not its centerline—6 vp above the bezel-derived visible screen bottom, and uses the correct responsive width for the current logical `W`;
- every present navigation state has a separate invisible `35% W x 28 vp` bottom-anchored interaction region; the visible indicator is never enlarged to that region and app-owned bottom content clears it;
- every omitted navigation bar is justified by an explicit user override or a documented absent/hidden state; if the state is ambiguous, reject the omission and show the bar;
- every static phone frame shows 08:08 unless a different time is explicitly required by the scenario, and every right-side status cluster follows the supplied reference order/anatomy: NearLink, Wi-Fi 7, dual stacked 5A, and battery 100;
- every mapped-device default home screen uses the exact corresponding PNG without redesign, crop, reflow, relabeling, or content substitution; other phone models preserve the supplied icon/widget design and layout language;
- status content avoids the camera/cutout, uses black or white content appropriate to the local background, maintains at least the source-specified 1.9 contrast ratio, and remains readable across the full status region without a conflicting left/right background split;
- when the navigation bar is present, its background is visually integrated and bottom controls clear the 28 vp interaction region; scroll-end content, WebView content, scrollbars, fixed/floating actions, keyboards, half-modals, and popups remain unobscured;
- split-screen, floating-window, Picture-in-Picture, landscape, immersive, game, short-video, and compact outer-display states follow their specific status/navigation behavior instead of inheriting the normal full-screen inset;
- immersive status/navigation bars have a simple reveal gesture; navigation auto-hide timing and game anti-accidental-touch behavior are represented when relevant;
- a single static immersive mockup shows the initial/default visible navigation bar unless explicitly labeled as the post-timeout hidden phase; a multi-frame immersive flow includes the visible and hidden phases needed to communicate the transition;
- Pura X/Pura X Max-like wide-foldable work distinguishes inner/unfolded and outer/compact display states, preserves functional continuity across folding, and applies compact outer-screen limits only in their stated scope;
- every Pura X Max unfolded landscape frame uses the official bezel rotated 90 degrees clockwise with its camera at the upper-right, while the landscape UI is freshly composited beneath the rotated alpha aperture;
- Picture-in-Picture is reserved for supported video and video-communication continuity, uses the system control template, and follows its entry, placement, and sizing rules;
- Flash Control Ball/Window is used only for qualifying lightweight cross-app information or task interactions and follows its system-owned limits;
- every HarmonyOS security/privacy emblem uses the supplied official shield asset without altered geometry, colors, crop, or decorative effects;
- all interactive elements have clear visual feedback and adequate touch targets;
- Chinese copy obeys length, terminology, punctuation, and spacing conventions;
- accessibility, interruption, offline, failure, and recovery are addressed when relevant;
- developer handoff distinguishes fixed values, responsive rules, system-owned areas, app-owned areas, and supplied assets.
- every exact measurement and text limit is source-verified; inferred design choices are labeled as recommendations.
- every Live View deliverable names the exact form and passes the measured geometry/state/placement checks in `references/live-view-sketch-spec.md`; every expanded phone card also passes `references/expanded-live-view-card.md`, including responsive `17:6` geometry, 16 vp side margins, 50 vp top coordinate, 20 vp radius, 48% neutral dark overlay, 25% neutral outline, responsive local regions, and one-time raster rounding; reject generic pills, fixed expanded-card sizes, documentation-artboard coordinates used as device coordinates, fixed-status collisions, and duplicate capsule/card presentation.

## Prototype and handoff requirements

For clickable prototypes and implementation packages, include:

- target devices, pixel preview frames, and vp/fp mapping;
- separate app-screen and official-bezel source layers, the bezel's native pixel dimensions, documented screen ratio, per-side alpha-derived overscan/extrusion treatment, connected-component method, and validation report with eight regional uncovered-pixel counts;
- screen/state inventory and interaction map;
- breakpoint and window-mode behavior;
- safe-area, keyboard, and hinge rules plus a per-state status/navigation bar matrix identifying system-owned versus app-owned regions, visibility, background treatment, insets, layering, reveal behavior, and acceptance evidence;
- the responsive 6 vp-high capsule navigation indicator, its 6 vp bottom-edge gap, width formula for the current logical screen width, separate `35% W x 28 vp` bottom interaction region, default 08:08 time, right-side status-cluster reference, and exact mapped home-screen asset whenever applicable;
- for every expanded phone Live View card, the logical `W`, unrounded responsive card and region calculations, vp-to-pixel mapping, final once-rounded raster frame, material/outline specification, and collision verification;
- component/token mapping and any justified custom component;
- the exact HarmonyOS Sans filename, resolved external path or deployment requirement, validated checksum state, variable weight, fp size, and license notice requirement;
- system-owned versus app-owned behavior;
- animation intent plus reduced-motion behavior;
- light/dark, large-text, screen-reader, muted/no-haptic, offline, error, interruption, and recovery states where relevant;
- acceptance criteria expressed as observable behavior;
- explicit notes where a demo intentionally differs from production behavior.

Never encode time-based demo transitions when the user has requested manual progression. Never silently change approved state order, screen content, or platform behavior.

## Source handling

The 16 core bundled PDFs are the authoritative frozen baseline supplied on 2026-09-03. Later materials explicitly classified by the user as supplementary extend that baseline without replacing it; the Flash Control Ball/Window source was added on 2026-09-07, the Picture-in-Picture source on 2026-09-08, the security/privacy branding, device-bezel, Pura X Max-like wide-foldable, default-home-screen, and initial raster system-chrome supplements on 2026-09-09, the editable Live View Sketch geometry template plus corrected responsive navigation-bar screenshots on 2026-09-10, the Pura X View expanded Live View full-canvas reference plus the HarmonyOS Sans font package on 2026-09-11, and the textual WeChat chat-interface reconstruction plus screenshot-derived light navigation treatment on 2026-09-12. The WeChat screenshot itself is intentionally excluded from the skill and repository; its status bar is out of scope, and its personal content must never be reproduced. The font package is authoritative for binary filenames, internal family names, variable-weight ranges, glyph files, hashes, and license; keep those binaries external to this skill and resolve them through [harmonyos-sans-font-assets.md](references/harmonyos-sans-font-assets.md). The corrected navigation screenshots supersede only the earlier fixed-pixel navigation-indicator geometry and placement. The Pura X View full-canvas reference supersedes conflicting expanded **phone-card** geometry, placement, corner radius, material, and internal-region values from the older Sketch template; it does not change the base/collapsed card, status-bar capsules, compact circular outer-display treatment, Live View behavior, navigation bar, or device bezel. The PDF text files are search-friendly derivatives. A compact installation may store the byte-exact PDFs as multipart `references/source-pdfs-archive/frozen-source-pdfs.tar.xz.part-*`; use `scripts/extract_frozen_pdf.py` to recover an authoritative PDF without altering it. For Live View, keep the current guide authoritative for eligibility, lifecycle, text limits, privacy, colors, and interaction; use `references/live-view-sketch-spec.md` for unaffected forms and `references/expanded-live-view-card.md` for expanded phone cards. For the security/privacy shield, the supplied `.ai` artwork is authoritative over its SVG and PNG convenience exports. For device presentation, the supplied bezel mapping and assets control over generic phone-frame conventions. The mapped home-screen PNGs—or PNGs materialized with verified identical RGB pixels from their lossless WebP storage masters—control over generic launcher layouts for their named devices, and the supplied status crop controls the default right-side status-cluster anatomy/order. If a supplementary source appears to conflict with the core baseline, preserve the core rule, flag the difference, and ask for direction unless the user has defined a narrower precedence. When future official documentation may have changed, do not silently replace any supplied source. If the user explicitly asks for current official guidance, verify against Huawei's official developer documentation, report material differences, and update this skill only when requested.
