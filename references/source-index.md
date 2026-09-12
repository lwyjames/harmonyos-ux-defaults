# Source Index and Routing

The core baseline consists of 16 PDFs supplied by the user on 2026-09-03. The supplemental system-feature set contains two PDFs supplied on 2026-09-07 and 2026-09-08. Security/privacy branding, device-bezel, and Pura X Max-like wide-foldable supplements were supplied on 2026-09-09. The editable Live View Sketch geometry template and corrected responsive navigation-bar screenshots were supplied on 2026-09-10. The Pura X View full-canvas expanded Live View reference was supplied on 2026-09-11. A WeChat conversation screenshot was analyzed on 2026-09-12 and retained only as the textual reconstruction in `references/wechat-chat-interface.md`; the original screenshot is intentionally excluded. Supplemental materials extend the core baseline. The navigation screenshots supersede only older navigation-indicator geometry; the Pura X View reference supersedes only conflicting expanded phone-card geometry, placement, radius, material, and local-region values. Each PDF has a matching plain-text extraction with the same basename. Other supplements are represented by their routed reference files and bundled source assets.

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

## Supplemental Live View design source

| Source | Added | Read/use for |
|---|---|---|
| `references/live-view-sketch-spec.md`, extracted from the user-supplied `HarmonyOS 实况通知样式模板0411.sketch` | 2026-09-10 | Unaffected 336 x 72 vp base/collapsed card, 80 x 28 / 128 x 28 vp capsule states, cutout-aware capsule placement, base/collapsed-card material simulation, and 224 x 224 circular outer-display treatment. Its conflicting expanded phone-card values are superseded. |
| `references/expanded-live-view-card.md`; `assets/live-view/01-16952.jpg` | 2026-09-11 | Authoritative expanded phone-card `17:6` responsive frame, 16 vp side margins, 50 vp top coordinate, 20 vp radius, 48% neutral dark overlay, 25% neutral outline, responsive local regions, Pura X View calculation, and cross-device verification. |

## Supplemental navigation-bar geometry source

| Source | Added | Read/use for |
|---|---|---|
| `references/navigation-bar-geometry.md`, transcribed from the two user-supplied corrected geometry screenshots | 2026-09-10 | Responsive visible-indicator width by logical screen width, 6 vp visible height, 6 vp bottom-edge gap, separate `35% W x 28 vp` bottom interaction region, logical-to-raster mapping, and rejection of the superseded fixed-pixel mockup geometry. |

## Supplemental WeChat chat-interface source

| Source | Added | Read/use for |
|---|---|---|
| `references/wechat-chat-interface.md`, reconstructed from a user-supplied screenshot that is intentionally not bundled | 2026-09-12 | WeChat/chat app-bar, conversation field, incoming/outgoing bubble hierarchy, time separators, avatars, composer, overlay behavior, privacy-safe fictional content, and the light navigation-region appearance. Ignore the source status bar. The observed `#F6F6F6` substrate / `#E3E3E3` indicator relationship is modeled as approximately 8% neutral black for ordinary light app surfaces and extended cross-application through `references/navigation-bar-geometry.md`. |

## Supplemental wide-foldable source

| Source | Snapshot update | Read for |
|---|---|---|
| 阔折叠-折叠屏-针对多设备设计 - 华为HarmonyOS开发者 | 2026-06-12 | Pura X/Pura X Max-like wide-foldable inner/outer continuity, compact outer-display system chrome and multi-window limits, Picture-in-Picture continuation, architecture preservation, size-triggered immersive browsing, outer-display components, and image/video/live/comment/login adaptations. Use with `references/wide-foldable-pura-x-max.md`. |

## Common routing combinations

- Any phone screen: layout + spacing + radius + typography + color + UI language + status bar + navigation bar; use `references/system-chrome-verification.md` before delivery and `references/navigation-bar-geometry.md` whenever the indicator is visible.
- WeChat conversation or WeChat background beneath a system surface: phone set + `references/wechat-chat-interface.md`; ignore the screenshot status bar, preserve HarmonyOS system chrome, use fictional content, and do not bundle the screenshot.
- Foldable/tablet/PC screen: phone set + responsive architecture + multi-window.
- Pura X/Pura X Max-like wide foldable, similarly proportioned compact screen, outer display, or fold/unfold flow: phone set + responsive architecture + multi-window + wide-foldable source; add Picture-in-Picture for qualifying video continuity. Resolve the exact inner/unfolded versus outer/compact display state before applying outer-display restrictions.
- Share flow: phone set + sharing; add Tap-to-Share when devices touch.
- Notification: color + typography + UI language + notification; add Live View only if eligibility is proven.
- Live View: notification + Live View + status bar + color + UI language + `references/live-view-sketch-spec.md`; add `references/expanded-live-view-card.md` for every expanded phone card.
- Service card/widget: layout + spacing + radius + typography + color + UI language + service cards.
- Any HarmonyOS security/privacy, anti-fraud, secure-preview, permission-recall, sensitive-operation, or safety-education surface: route the normal sources for that surface + security/privacy branding; use the official shield whenever a branded security/privacy emblem is shown.
- Video playback, live video, video call, or video-conference continuity outside the source app: phone set + Picture-in-Picture + multi-window.
- Flash Control Ball or lightweight cross-app monitoring/action: phone set + Flash Control Ball/Window; add multi-window when comparing it with a system floating window or specifying window-mode continuity.
- High-fidelity translucent overlay: color + Immersive Light + safe-area/system-chrome source for its location.
- Developer handoff: all sources that govern any visible surface or state in the prototype.
