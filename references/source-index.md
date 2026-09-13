# Source Index and Routing

The core baseline consists of 16 PDFs supplied by the user on 2026-09-03. The supplemental system-feature set contains two PDFs supplied on 2026-09-07 and 2026-09-08. Security/privacy branding, device-bezel, and Pura X Max-like wide-foldable supplements were supplied on 2026-09-09. The editable Live View Sketch geometry template and corrected responsive navigation-bar screenshots were supplied on 2026-09-10. The Pura X View full-canvas expanded Live View reference was supplied on 2026-09-11. A WeChat conversation screenshot and subsequent correction crops were analyzed on 2026-09-12 and retained only as the textual reconstruction in `references/wechat-chat-interface.md`; the originals are intentionally excluded. Two additional Pura X View screenshots reviewed on 2026-09-12 clarify expanded Live View overlay, material-compositing, and cross-device rules; they are also intentionally excluded. Iterative Pura X View landscape hand-contact corrections, Pura X View Xiaoyi main-interface captures, and Pura X View lock-screen visual/notification captures reviewed on 2026-09-13 are retained only as generalized textual references; project imagery, private content, status-bar content, finger coordinates, and masks are intentionally excluded. Supplemental materials extend the core baseline. The navigation screenshots supersede only older navigation-indicator geometry; the Pura X View references supersede only the specifically documented visual geometry, material, and compositing values. The Xiaoyi captures establish app-owned component relationships only and are responsively derived for other phones/windows; they do not replace system chrome. Each PDF has a matching plain-text extraction with the same basename. Other supplements are represented by their routed reference files and bundled source assets.

## How to consult sources

1. Read every source text relevant to the requested surface or rule.
2. Search all source text when the task spans multiple systems.
3. Render/open the PDF pages whenever a diagram, anatomy, sample screen, crop area, or recommended/not-recommended comparison matters.
4. Treat the PDF as authoritative if extracted text loses table structure or labels.
5. Use the snapshot update date below to identify possible staleness. Do not silently replace it.

Path patterns:

- Searchable text: references/source-text/[basename].txt
- Authoritative PDF in a full installation: references/source-pdfs/[basename].pdf
- Byte-exact frozen PDF archive in a compact installation: references/source-pdfs-archive/frozen-source-pdfs.tar.xz.part-*

When an individual PDF is absent, extract the requested byte-exact source to a temporary working directory with `python scripts/extract_frozen_pdf.py --name "[basename].pdf" --output-dir OUTPUT_DIR`. Do not edit or overwrite the archive parts. The archive is a storage representation of the original supplied PDFs, not a replacement source or a weakened baseline.

## Foundation sources

| Source | Snapshot update | Read for |
|---|---|---|
| 布局基础-布局-通用设计基础 - 华为HarmonyOS开发者 | 2026-08-25 | vp/fp units, 8 vp grid, width breakpoints, grids, margins/gutters, maximum content width, safe areas, foldables, tablets, watches, device pixel/vp tables |
| 响应式应用架构-布局-通用设计基础 - 华为HarmonyOS开发者 | 2025-06-20 | bottom-to-side tab changes, split layouts, side navigation behavior, 600/840 vp architecture thresholds |
| 间隔参数-视觉风格-通用设计基础 - 华为HarmonyOS开发者 | 2026-07-10 | edge margins by device, element/text gaps, wearable/smart-screen spacing, complete spacing token table |
| 圆角参数-视觉风格-通用设计基础 - 华为HarmonyOS开发者 | 2026-08-12 | corner hierarchy, typical 4/8/16/20/32 vp usage, complete radius token table |
| 文本排版-视觉风格-通用设计基础 - 华为HarmonyOS开发者 | 2026-07-30 | display/title/subtitle/body/caption styles across phone/PC/watch, readable type, large text, Chinese/English line-break rules, custom fonts |
| 色彩-视觉风格-通用设计基础 - 华为HarmonyOS开发者 | 2026-07-21 | semantic color architecture, primary/on-primary/brand/container roles, light/dark mappings, text/icon/container/background/interaction tokens, wearable tokens |
| 沉浸光感-视觉风格-通用设计基础 - 华为HarmonyOS开发者 | 2026-06-12 | Immersive Light concept, user intensity levels, five material levels, placement-specific material guidance |
| 界面用语-通用设计基础 - 华为HarmonyOS开发者 | 2025-06-20 | tone, content design, deletion/disconnection/error/loading/update/help/onboarding patterns, punctuation, spaces, numbers, paths, Chinese/English terminology |

## System-feature sources

| Source | Snapshot update | Read for |
|---|---|---|
| 状态栏-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2025-06-20 | transparent/immersive status-bar background, black/white status content, 1.9 local contrast threshold, cutout avoidance, conflicting background prevention, and hide/reveal behavior |
| 导航条-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2025-08-14 | default navigation-bar presence in non-full-screen app windows, mandatory app/WebView/third-party adaptation, immersive background, 28 vp bottom lift, scroll-end and scrollbar behavior, fixed/floating controls, keyboard, modal layering, split/floating/Picture-in-Picture differences, landscape, immersive initial visibility and auto-hide, game gesture protection, and short-video behavior |
| 多窗口交互-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2026-03-11 | floating/split/PiP selection, drag-handle safe area, continuity, audio focus, window ratios, navigation/layout adaptation, task split |
| 分享-系统能力-系统特性&能力 - 华为HarmonyOS开发者 | 2026-01-07 | latest system share sheet, four system regions, content preview templates, ratios/cropping, method ordering, detail page, system actions |
| 碰一碰-系统能力-系统特性&能力 - 华为HarmonyOS开发者 | 2026-04-13 | supported device pairs/content, system-owned regions, five card templates, image/file/link ratios, crop-safe preview selection |
| 通知-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2025-10-30 | notification value and anti-abuse rules, anatomy, groups, templates, center/lock/banner/badge/status presentations, text limits |
| 实况窗-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2026-06-04 | eligibility, lifecycle, capsule/card/lock-screen forms, templates, interaction, privacy, emphasis color, text and asset limits |
| 服务卡片-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2026-02-10 | service-card purpose, discovery, interaction, editing, refresh, sizes, preview/output radii, layout, color, type, touch areas, snapshots, placeholders, lock screen, interactive out-of-bounds effects, multi-device adaptation |

## Supplemental system-feature sources

| Source | Snapshot update | Read for |
|---|---|---|
| 闪控球和闪控窗-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2026-08-19 | Flash Control Ball/Window positioning, qualifying scenarios, creation and opening behavior, global/per-app quantity limits, minimize/delete interactions, ball templates and device sizes, regular/Mini window states and responsive size rules, and distinction from a system floating window |
| 画中画-系统特性-系统特性&能力 - 华为HarmonyOS开发者 | 2025-06-20 | Picture-in-Picture eligibility, fixed/back/home entry patterns, auto-start setting dependency, proportional resize gestures, edge minimization and recovery, system control-panel behavior, scenario-specific buttons, default placement, portrait/landscape proportions, and device/fold-state size rules |

## Supplemental branding source

| Source | Added | Read/use for |
|---|---|---|
| `references/security-privacy-branding.md`; `assets/branding/harmonyos-shield-security-logo-official.ai`; matching `.svg` and `-transparent.png` convenience assets | 2026-09-09 | Mandatory HarmonyOS security/privacy shield selection, asset priority, prohibited substitutions and modifications, standard colors, transparency, clear-space and placement rules, dark-surface treatment, and delivery verification. Treat the `.ai` file as authoritative. |

## Supplemental device preview source

| Source | Added | Read/use for |
|---|---|---|
| `references/device-preview-frames.md`; three mapped PNG assets under `assets/device-bezels/` | 2026-09-09 | Default Pura X Max unfolded portrait canvas and bezel, Pura X View dimensions and front bezel, Pura 90 Pro Max bezel, exact device-to-asset routing, and bezel compositing rules. |
| `references/phone-in-hand-contact-compositing.md`, generalized from iterative user-reviewed hand/device contact corrections without bundling the project screenshots | 2026-09-13 | Device-derived grip planning, per-boundary contact maps, rear/device/foreground layer order, finger and thumb occlusion, matte-edge quality, bilateral comparison, local-edit regression locking, contrast-background inspection, and the Pura X View landscape regression case. |
| `references/lock-screen-visual-defaults.md`, reconstructed from the user-supplied Pura X View lock-screen screenshot without bundling it | 2026-09-13 | Pura X View 22 vp circular camera at `(220,27) vp`, 32 vp portrait status-edge anchors, wallpaper-derived translucent clock color, and symmetric lower lock-screen shortcut geometry/material. |
| `references/lock-screen-notification-card.md`, reconstructed from the user-supplied Pura X View lock-screen notification screenshot without bundling it | 2026-09-13 | Ordinary expanded/detail lock-screen notification frame `(16,554,408,64) vp` on Pura X View, responsive width and lower-shortcut anchoring on other portrait phones, logo/title/detail/time anatomy, wallpaper-derived thin glass, privacy-preview behavior, and strict outside-mask invariance. |

## Supplemental Live View design source

| Source | Added | Read/use for |
|---|---|---|
| `references/live-view-sketch-spec.md`, extracted from the user-supplied `HarmonyOS 实况通知样式模板0411.sketch` | 2026-09-10 | Unaffected 336 x 72 vp base/collapsed card, 80 x 28 / 128 x 28 vp capsule states, cutout-aware capsule placement, base/collapsed-card material simulation, and 224 x 224 circular outer-display treatment. Its conflicting expanded phone-card values are superseded. |
| `references/expanded-live-view-card.md`; `assets/live-view/01-16952.jpg`; two supplemental Pura X View screenshots plus user-confirmed no-reflow, material-response, and blur-boundary corrections reviewed on 2026-09-12 but not bundled | 2026-09-11 / 2026-09-12 | Authoritative expanded phone-card `17:6` responsive frame, 16 vp side margins, 50 vp top coordinate, 20 vp radius, 100%-opacity root group, actual-underlay color-preserving offscreen blur clipped after filtering, 48% neutral-dark overlay layer, 25% neutral outline, responsive local regions, universal cross-application overlay/occlusion, base-layer invariance, and zero-change exterior raster validation. Build/freeze the normal app first; app-owned coordinates and scroll state remain unchanged when the card is added. Broad underlay color remains locally perceptible without recognizable detail; uniform-gray, external blur bleed, broad shadow, haze, glow, or extra desaturation treatments are invalid. The Pura X View screenshots are reference results, not reusable pixel geometry. |
| `references/push-notification-banner.md`, reconstructed textually from the user-supplied Pura X View portrait Push Notification screenshot | 2026-09-13 | Cross-application portrait push-banner frame `(16,50,W-32,64) vp`, 16 vp radius, responsive icon/title/detail/time/affordance layout, actual-underlay color-preserving blur, reconstructed 32% neutral-dark overlay and 24% neutral-light outline, overlay-without-reflow behavior, and cross-device verification. The screenshot itself is intentionally excluded. |

## Supplemental navigation-bar geometry source

| Source | Added | Read/use for |
|---|---|---|
| `references/navigation-bar-geometry.md`, transcribed from the two user-supplied corrected geometry screenshots | 2026-09-10 | Responsive visible-indicator width by logical screen width, 6 vp visible height, 6 vp bottom-edge gap, separate `35% W x 28 vp` bottom interaction region, logical-to-raster mapping, and rejection of the superseded fixed-pixel mockup geometry. |

## Supplemental WeChat chat-interface source

| Source | Added | Read/use for |
|---|---|---|
| `references/wechat-chat-interface.md`, reconstructed from user-supplied screenshots that are intentionally not bundled | 2026-09-12 | WeChat/chat app-bar, conversation field, incoming/outgoing bubble hierarchy, time separators, avatars, cross-device composer geometry including the 12 vp trailing add-control inset, privacy-safe fictional content, and the light navigation-region appearance. Ignore the source status bar. Expanded-card material/occlusion is routed to the universal `references/expanded-live-view-card.md`; it is not a WeChat-only behavior. |

## Supplemental Xiaoyi AI-assistant source

| Source | Added | Read/use for |
|---|---|---|
| `references/xiaoyi-assistant-interface.md`, reconstructed from user-supplied Pura X View screenshots and magnified component crops that are intentionally not bundled | 2026-09-13 | Xiaoyi's pinned glass app bar, mixed assistant transcript, asymmetric square-upper-right user messages, unboxed answers, task status, result cards, and responsive derivation. The reference's glass-button stack, call-star hierarchy, four-small-dot more control, detailed four-chip icon anatomy, trailing three-sparkle control, explicit exclusion of a standalone bottom-right down-arrow, and 4 vp AI-notice/navigation gap are normative requirements rather than examples. Ignore the captures' complete status bars and retain existing HarmonyOS system chrome. |

## Supplemental wide-foldable source

| Source | Snapshot update | Read for |
|---|---|---|
| 阔折叠-折叠屏-针对多设备设计 - 华为HarmonyOS开发者 | 2026-06-12 | Pura X/Pura X Max-like wide-foldable inner/outer continuity, compact outer-display system chrome and multi-window limits, Picture-in-Picture continuation, architecture preservation, size-triggered immersive browsing, outer-display components, and image/video/live/comment/login adaptations. Use with `references/wide-foldable-pura-x-max.md`. |

## Common routing combinations

- Any phone screen: layout + spacing + radius + typography + color + UI language + status bar + navigation bar; use `references/system-chrome-verification.md` before delivery and `references/navigation-bar-geometry.md` whenever the indicator is visible.
- Any phone lock screen: phone set + `references/lock-screen-visual-defaults.md`; add `references/lock-screen-notification-card.md` for an ordinary expanded/detail notification, and add Live View or service-card sources only when those distinct surfaces are actually present.
- Any phone held, touched, approached, or occluded by a hand/finger: phone set + `references/device-preview-frames.md` + `references/phone-in-hand-contact-compositing.md`; establish the frozen device master and contact map before hand generation or masking.
- WeChat conversation or WeChat background beneath a system surface: phone set + `references/wechat-chat-interface.md`; ignore the screenshot status bar, preserve HarmonyOS system chrome, use fictional content, and do not bundle the screenshot.
- Xiaoyi/小艺 full-screen phone assistant: phone set + `references/xiaoyi-assistant-interface.md`; resolve device class, orientation, `E`, `T`, and active column `K`, ignore the captures' status bars, preserve HarmonyOS system chrome, use privacy-safe content, and do not bundle the screenshots.
- Foldable/tablet/PC screen: phone set + responsive architecture + multi-window.
- Pura X/Pura X Max-like wide foldable, similarly proportioned compact screen, outer display, or fold/unfold flow: phone set + responsive architecture + multi-window + wide-foldable source; add Picture-in-Picture for qualifying video continuity. Resolve the exact inner/unfolded versus outer/compact display state before applying outer-display restrictions.
- Share flow: phone set + sharing; add Tap-to-Share when devices touch.
- Transient portrait Push Notification banner: color + typography + UI language + notification + `references/push-notification-banner.md`; add Live View only if eligibility is proven, and never duplicate the same event in both forms.
- Expanded/detail lock-screen notification card: color + typography + UI language + notification + `references/lock-screen-visual-defaults.md` + `references/lock-screen-notification-card.md`; keep the collapsed icon/count state, transient banner, notification center, calls/alarms, Live View, and service cards in their native scopes.
- Other notification surfaces: color + typography + UI language + notification; keep notification-center, immersive, call/alarm, badge, and status-icon behavior in their native scope.
- Live View: notification + Live View + status bar + color + UI language + `references/live-view-sketch-spec.md`; add `references/expanded-live-view-card.md` for every expanded phone card.
- Service card/widget: layout + spacing + radius + typography + color + UI language + service cards.
- Any HarmonyOS security/privacy, anti-fraud, secure-preview, permission-recall, sensitive-operation, or safety-education surface: route the normal sources for that surface + security/privacy branding; use the official shield whenever a branded security/privacy emblem is shown.
- Video playback, live video, video call, or video-conference continuity outside the source app: phone set + Picture-in-Picture + multi-window.
- Flash Control Ball or lightweight cross-app monitoring/action: phone set + Flash Control Ball/Window; add multi-window when comparing it with a system floating window or specifying window-mode continuity.
- High-fidelity translucent overlay: color + Immersive Light + safe-area/system-chrome source for its location.
- Developer handoff: all sources that govern any visible surface or state in the prototype.
