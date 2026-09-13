# Xiaoyi AI Assistant Phone Interface

Use this reference for the HarmonyOS system AI assistant Xiaoyi (小艺) main conversation interface on phones. It is a textual reconstruction of two user-supplied Pura X View screenshots reviewed on 2026-09-13. The screenshots themselves, their conversation text, locations, weather, restaurant results, images, and status-bar content are intentionally excluded from the skill.

## Scope and precedence

- Apply this pattern to Xiaoyi's full-screen phone conversation surface, including ordinary answers, visible task-execution status, system/app result cards, capability shortcuts, and text/voice input.
- Do not automatically apply this page architecture to third-party chat apps, Push Notifications, Live View, lock-screen assistant affordances, a voice-call overlay, or a compact outer display. Those retain their own native rules.
- The screenshots and later magnified detail crops control the Xiaoyi app-owned visual hierarchy and relationships described here. The glass-button treatment, top-right control anatomy, four named capability chips and their icons, trailing sparkle control, absence of a standalone bottom-right down-arrow, AI-notice/navigation spacing, and asymmetric user-message shape are **normative requirements, not illustrative examples**. Existing HarmonyOS sources remain authoritative for system chrome, semantics, accessibility, responsive layout, typography, notifications, and device presentation.
- **Ignore the screenshots' complete status bar.** Do not copy their time, network, signal, battery, spacing, icons, or colors. Apply the skill's existing status-bar rules independently.
- Treat the `908 x 1536 px` screenshots as proportional review captures of a `440 x 744 vp` Pura X View logical surface. Reconstruct in vp/fp first. Never reuse the screenshot pixels, coordinates, crop, or content on another device.

## Page architecture

Build the screen in three independently controlled layers:

1. A pinned top Xiaoyi app bar beneath the system status safe area.
2. One vertically scrolling conversation/result stream.
3. A pinned bottom interaction stack containing capability shortcuts, the message composer, the AI-content notice, and the separate HarmonyOS navigation region.

The top and bottom layers may use local floating material while the transcript scrolls beneath them. Do not blur, dim, or move the complete page to obtain this effect. Clip every blur, color mask, outline, and shadow to its owning app-bar/control/bottom-stack boundary.

## Responsive derivation from the Pura X View reference

The Pura X View screenshot establishes the component relationships, not a universal full-screen scale. Resolve the current logical window and device class before laying out Xiaoyi:

- Let `W` and `H` be the current logical window width and height after orientation/window-mode resolution.
- Let `E` be the existing HarmonyOS device-edge margin: `16 vp` for an ordinary phone, `24 vp` for a foldable, and `32 vp` for a tablet-class window, then increase it symmetrically if the actual cutout, rounded corner, hinge, or safe area requires more clearance.
- Let `T = E + 8 vp` be Xiaoyi's conversation/result text inset. On the Pura X View reference, `E=16 vp` and `T=24 vp`.
- Let `K` be the active conversation-column width. In ordinary portrait phone windows below `840 vp`, use the complete window as the single-column canvas (`K=W`). At `W>=840 vp`, choose a centered span from the applicable 12-column grid that preserves a readable conversation line length; do not stretch the transcript edge to edge. A parent/child or history/conversation split is allowed only when the product hierarchy genuinely benefits from it.
- Compute component frames in the active column, then offset them by the column's centered `x`. Never scale the complete `440 x 744 vp` Pura X View composition.

Within an active column of width `K`:

```text
appBarLeading = E
conversationX = T
conversationWidth = K - 2T
resultCardWidth = K - 2T
userBubbleMaxWidth = min(360 vp, K - 2T)
composerX = E
composerWidth = K - 2E
```

Mapped portrait checks:

| Device/state | `W` | `E` | `T` | Result-card width | Composer width |
|---|---:|---:|---:|---:|---:|
| Pura 90 Pro Max portrait | `374 vp` | `16 vp` | `24 vp` | `326 vp` | `342 vp` |
| Pura X View portrait reference | `440 vp` | `16 vp` | `24 vp` | `392 vp` | `408 vp` |
| Pura X Max unfolded portrait | `665 vp` | `24 vp` | `32 vp` | `601 vp` | `617 vp` |

These are calculation checks, not reusable fixed sizes. Keep text and controls at their specified vp/fp sizes; gain or lose capacity through wrapping, reflow, scrolling, overflow, and column selection rather than global scaling.

Orientation behavior:

- Portrait phones keep the three-layer architecture and a single transcript column.
- In landscape or short-height windows, keep the app bar and composer pinned, collapse the optional capability-chip row before reducing composer usability, and let the transcript use the remaining height. Move lower-priority app-bar actions to overflow when they collide with the title or cutout.
- On a wide foldable/tablet window, keep the active conversation column readable and centered. Introduce a second pane only for a real persistent hierarchy such as history or context, never merely to fill width.
- Preserve each mapped device's own bezel, camera/cutout, status/navigation safe areas, and orientation rules. The screenshots provide no status-bar evidence for any device.

## Screenshot-reconstructed component geometry

The following are project reconstruction values in logical units, not recovered official component tokens:

| Element | Phone rule |
|---|---|
| App-bar edge inset | `E`; `16 vp` on Pura X View |
| Circular app-bar controls | `40 x 40 vp` |
| Gap between trailing controls | `8 vp` |
| Title leading coordinate | `E + 48 vp`; `64 vp` on Pura X View |
| Conversation/result side inset | `T = E + 8 vp`; `24 vp` on Pura X View |
| User-message maximum width | `min(360 vp, K - 2T)` |
| Single-line user-message height/corners | `44 vp`; radii `(22,0,22,22) vp` for top-left/top-right/bottom-right/bottom-left |
| Rich result-card width | `K - 2T` |
| Result-card radius | `16 vp` |
| Capability-chip height and gap | `36 vp` high, `8 vp` gap |
| Trailing sparkle control | `40 x 40 vp`, trailing `E`, centered on chip row |
| Composer frame | `(x=E, width=K-2E, height=48) vp` |
| Composer radius | `24 vp` |
| AI notice to navigation indicator | `4 vp` clear visual gap from notice glyph bottom to indicator top |

Do not assign a universal absolute `y` coordinate to the app bar or bottom composer. Anchor the app bar below the actual status safe area and anchor the interaction stack above the navigation/gesture region. Keyboard, window, orientation, and safe-area changes control their final vertical placement.

At phone widths below `600 vp`, retain the single-column conversation shown here. At `600–839 vp`, retain a single conversation stream but apply the selected device class's larger edge margin. At `840 vp` and above, keep readable line lengths by centering the conversation column inside the applicable HarmonyOS grid rather than stretching bubbles, cards, or paragraphs edge to edge. Retain the `40 vp` controls and `48 vp` composer height; redistribute space instead of scaling the entire Pura X View composition.

## Top Xiaoyi app bar

- Place a `40 vp` circular navigation/menu control at the leading `E` inset.
- The leading glyph is not a generic hamburger: use three horizontal strokes with the middle stroke terminating in a right-pointing triangular arrow.
- Use “小艺” as the app title, aligned after the leading control at `E + 48 vp`; on Pura X View this resolves to `64 vp`. Use the HarmonyOS `Title_M` role (`24 fp`, Bold) unless accessibility scaling requires reflow.
- On the full-screen Xiaoyi main interface, always place these three controls at the trailing side in this exact physical order, each `40 vp` with `8 vp` gaps and a final `E` trailing inset:
  1. an outline telephone handset with two unequal filled four-point sparkles at its upper-right: the upper sparkle is smaller and the lower sparkle is larger;
  2. an outline speaker with a diagonal mute slash;
  3. four small, equal, solid dots in a centered `2 x 2` arrangement. Reconstruct each dot at approximately `6 vp` diameter inside the `40 vp` control; this is a project reconstruction value from the magnified crop, not an official HarmonyOS token. Do not enlarge them into four dominant black disks, outline them as rings, or substitute a horizontal/vertical ellipsis.
- Use dark semantic glyphs inside the mandatory circular glass controls. Keep every touch target at least `40 vp`; do not replace these controls with opaque disks, bare icons, rounded squares, or generic placeholders.
- Treat the app bar as a top floating `ULTRA_THIN` material with gradient blur. Its apparent gray or color must respond to the real content scrolling beneath it. Do not paint the darkened lower edge visible in one screenshot as a fixed gray gradient or broad drop shadow.
- Keep the title readable when trailing actions are present. At large font sizes or narrow windows, move lower-priority actions into the overflow menu rather than shrinking type or overlapping controls.

## Conversation hierarchy

### User messages

- Right-align user messages to the active column's `T` trailing inset.
- Use a quiet light-blue semantic container, near-black primary text, no avatar, and no chat-tail triangle.
- The blue container is an **asymmetric Xiaoyi message shape**, not a symmetric capsule and not a generic four-corner rounded rectangle. A single-line message is `44 vp` high. In top-left/top-right/bottom-right/bottom-left order, use corner radii `(22,0,22,22) vp`: the upper-right corner is square where the top edge meets the trailing edge, while the other three corners remain fully rounded.
- For wrapped messages, retain the square upper-right corner and use `22 vp` on the other three corners; increase height to fit text without converting the shape into a capsule, speech-tail bubble, or uniformly rounded rectangle.
- Use `16 vp` horizontal padding and vertically center a single-line label. Let the asymmetric container grow only when the text cannot fit at the allowed maximum width.
- Limit width to `min(360 vp, K - 2T)` and wrap by words/Chinese punctuation. Never center the bubble.

### Xiaoyi responses

- Render Xiaoyi's ordinary response directly on the page without an assistant bubble or assistant avatar.
- Align the response to the active column's `T` inset and allow a maximum text width of `K - 2T`.
- Use `Body_L` (`16 fp`) for ordinary answer text. Use bold emphasis sparingly for decisive values, warnings, dates, or conclusions; use semantic brand-blue text for tappable links.
- Support paragraphs, headings, numbered/bulleted lists, inline emphasis, linked entities, media previews, and native result cards without changing the base left alignment.
- Keep concise centered timestamps or turn separators in tertiary text (`Body_S`, `12 fp`) only when they add chronology. Do not place a timestamp after every turn.

## Visible task status

- When Xiaoyi performs a user-visible system/app action or multi-step tool task, show a collapsible status row before the corresponding result.
- Use a leading state glyph, a concise label such as “进行中”, “已完成”, or an actionable failure state, and a trailing expand/collapse chevron. Add a quiet separator beneath the row.
- The status row describes observable task phases and outcomes only. Do not expose private chain-of-thought, hidden reasoning, credentials, raw tool logs, or internal implementation traces.
- Keep completed sections collapsed by default when the result is already visible. Expand only on user action or when required to resolve an error.

## Rich results and action cards

- Use an unboxed answer for explanation and a card only when the result is structured, actionable, stateful, or belongs to another system/app capability.
- Use a `K - 2T` card aligned to the active column's `T` inset with a `16 vp` radius and at least `16 vp` inner padding.
- Card header: source app/service icon and name at leading, with a native “更多”/chevron affordance at trailing only when a real deeper destination exists.
- Card body: emphasize the primary result, then supporting metadata. Use native controls such as switches without redrawing their anatomy.
- The example alarm card is a pattern for a confirmed system action, not a mandatory alarm widget. Adapt the card content and height to the actual result.
- For search or recommendation results, allow bold section labels, blue linked titles, metadata, and cropped media previews below the answer. Do not turn all assistant output into stacked cards.

## Bottom interaction stack

### Capability shortcuts

- Place a horizontally scrolling shortcut row above the composer with a leading `E` inset, `36 vp`-high capsule chips, and `8 vp` gaps. Do not compress chip labels to fit the row; allow horizontal overflow.
- The main interface uses exactly four capability chips, in this order. Their labels and leading icons are fixed interface anatomy, not example content:
  1. `深度思考`: a compact atom/orbit outline with intersecting elliptical paths around one solid central dot, plus one small filled four-point sparkle at its upper-right. Do not substitute a planet-with-ring, lightbulb, brain, or detached generic star.
  2. `小艺Work`: a circular outline emblem containing the Xiaoyi Work face/wave anatomy—two tiny facial marks at the left, a broad curved inner lobe descending from the upper-right, and a lower sweeping wave. Do not substitute an atom, robot head, smiley, or plain circle.
  3. `解锁新小艺`: a partially open circular outline containing clearly legible, slightly tilted `NEW`, with a small solid four-point mark at the lower-left and the opening at lower-right. Do not replace it with a filled badge, generic `NEW` pill, or sealed circle.
  4. `修图`: an outline landscape/photo frame with mountain/image detail and a small four-point sparkle at the frame's upper-right. Do not substitute a pencil, magic wand, crop brackets, or plain gallery icon.
- Preserve each icon-label pairing exactly. Do not substitute a lightbulb, generic list, pencil, magic wand, or unlabeled placeholder. Keep every label on one line; on narrower windows, horizontally scroll or partially reveal the row instead of renaming, compressing, or dropping a chip.
- Place a separate `40 vp` circular Xiaoyi sparkle action immediately after `修图`, aligned to the chip-row center and ending at trailing inset `E`. Its dark glyph is a cluster of three unequal filled four-point sparkles: the largest sits centrally and slightly lower, a medium sparkle sits upper-left, and the smallest sits lower-right. It is not a colored gradient orb, plus button, generic star outline, or two-star cluster.
- Use a bottom floating `THIN` material with a gradient color mask. Chip/container color must respond to the actual content beneath it; do not hard-code the screenshot's white, gray, blue, or restaurant-image tint.

### Composer

- Use one horizontally centered capsule at `(E, *, K-2E, 48) vp` inside the active column with `24 vp` radius.
- Place the voice-mode control at leading, the placeholder or typed text in the flexible center, and the add/attachment control at trailing. Use “发消息或按住说话” as the Xiaoyi default placeholder when both text and press-to-talk are available.
- Keep the leading and trailing controls visually balanced, at least `40 vp` touchable, and vertically centered. Do not add unexplained trailing space after the add control.
- Render the composer with a locally responsive translucent material and subtle semantic outline. Its blur and tint must end at the rounded boundary; never blur the full transcript.
- Center “内容由 AI 生成” in tertiary `Caption_M` (`10 fp`) text below the composer and above the HarmonyOS navigation region. Its visible glyph bottom must sit `4 vp` above the navigation indicator's top edge. For Pura X View (`H=744 vp`), the navigation frame is `y=732–738 vp`, so the notice's visible glyphs end at `y=728 vp`. This notice is informational, not a button.
- When the keyboard appears, move the composer with the IME inset. Collapse or hide optional shortcut chips before reducing the primary input area's usability.

### Bottom-right control exclusion

- Do not render a standalone down-arrow, down-chevron, or scroll-to-latest control above the bottom capability row. The trailing three-sparkle button is the only separate circular control at the bottom right.
- This exclusion does not remove a chevron that is structurally part of another component, such as a task-status expand/collapse affordance or a result-card destination.

## Mandatory glass control construction

Every Xiaoyi shell control visible in the reference uses glass transparency. This requirement covers the leading menu, all three top-right controls, capability chips, trailing sparkle action, and the composer surface. It also governs any additional shell button introduced in the same interface.

Build each glass control as separate full-opacity layers:

1. sample the actual local content beneath the control and blur only that offscreen sample;
2. clip the blurred result to the exact circle or capsule path;
3. apply the role-appropriate translucent neutral/white color mask (`ULTRA_THIN` for top and floating circles, `THIN` for bottom chips/composer);
4. add a fine light perimeter rim plus restrained inner specular highlight and shallow lower-edge refraction/shadow;
5. render the dark glyph and label at independent full opacity above the material.

The control must remain visibly translucent: broad underlay hue/luminance may influence it softly, while underlying detail becomes unreadable. Never use an opaque white/gray fill, one parent opacity for the complete control, a gradient-colored AI orb, a broad external glow, or blur extending beyond the control mask. Voice and add glyphs inside the composer remain visually integrated with the composer glass rather than becoming detached opaque buttons.

## Material and layering

- The conversation base uses the HarmonyOS light neutral background hierarchy. The screenshots do not establish a fixed raw background color or a dark-mode token.
- Use semantic tokens for text, blue user-message containers, brand-blue links, surfaces, outlines, and interaction states. Define dark-mode mappings rather than simply inverting screenshot RGB values.
- Top controls and the sparkle circle use `ULTRA_THIN`; bottom capability chips and composer use `THIN`, consistent with the HarmonyOS Immersive Light hierarchy. This glass construction is mandatory, not optional decoration.
- Compute material from the actual pixels beneath each floating region. A scrolled image may warm the bottom controls; plain text may leave them neutral. Preserve this local response while keeping text/icons independently legible.
- Do not use overall parent opacity for app-bar or bottom-stack groups. Render material, outline, glyphs, and text as separate layers.
- No blur, haze, or color wash may escape a component's mask. Areas outside the top app bar and bottom floating controls remain sharp.

## Behavior and accessibility

- Keep the app bar and input stack pinned while the central transcript scrolls. Content may pass behind their translucent materials, but provide enough end inset that the final answer can be scrolled fully above the composer.
- During streaming, preserve the user's reading position. Auto-follow only when the user was already at the bottom; otherwise keep the current reading position without adding a floating bottom-right jump control.
- Announce turns, task status, cards, links, switches, shortcut chips, and composer controls in logical reading order. Expose state and destination semantics.
- Preserve system font scaling. Reflow paragraphs and cards; never shrink text or clip a completed result. Move low-priority app-bar actions to overflow when needed.
- Respect reduced motion. Streaming and expand/collapse transitions must not move unrelated transcript content abruptly.
- Provide permission-denied, offline, interrupted, partial-result, and retry states without replacing a useful earlier answer.

## Verification

Reject a Xiaoyi phone interface unless all applicable checks pass:

- the screenshot status bar has been ignored and the current HarmonyOS system-chrome specification remains authoritative;
- the top app bar, central scroll stream, and bottom interaction stack are separate layers;
- the leading menu and three mandatory trailing actions use `40 vp` glass controls, `8 vp` trailing gaps, and the resolved `E` edge insets without title collision; their glyphs are respectively arrow-menu, sparkling telephone with the smaller star above the larger star, muted speaker, and centered `2 x 2` small solid-dot more; reject reversed star hierarchy, large circles, rings, or ellipsis substitutions;
- user messages are right-aligned asymmetric light-blue shapes (`44 vp` high with `(22,0,22,22) vp` radii when single line) while Xiaoyi answers remain unboxed and left-aligned; reject a rounded upper-right corner, symmetric capsule, tail, or generic uniformly rounded rectangle;
- task-status rows expose only observable progress/outcomes and never hidden reasoning;
- structured/actionable results use responsive cards rather than forcing every answer into a card;
- the capability row contains the four mandatory icon-label pairs `深度思考`, `小艺Work`, `解锁新小艺`, and `修图` in that order, preserves the detailed orbit-and-sparkle, Xiaoyi face/wave, open-NEW-circle, and sparkling-photo glyphs, scrolls horizontally without squeezed labels, and ends with the separate glass circle containing the large-center/medium-upper-left/small-lower-right three-sparkle glyph;
- no standalone bottom-right down-arrow, down-chevron, or scroll-to-latest control is present;
- the composer resolves to `(E, *, K-2E, 48) vp`, clears the IME and navigation region, and leaves no extra trailing gutter after the add control;
- the AI-content notice remains visible, centered, noninteractive, uses `10 fp`, and its visible glyph bottom is exactly `4 vp` above the navigation-indicator top;
- every shell button uses the required clipped glass stack, header/bottom material responds to real underlying content, and every blur/tint effect remains clipped to its component;
- the transcript can scroll its final content fully above the pinned composer, and auto-follow does not steal position from a user reading earlier content;
- the mapped Pura 90 Pro Max, Pura X View, and Pura X Max portrait calculation checks pass, and wider/landscape windows reflow through the HarmonyOS grid instead of stretching the Pura X View screenshot.

Acceptance criterion:

> Xiaoyi's phone main interface uses a pinned glass app bar, a single scrolling mixed-content conversation stream, and a pinned glass interaction stack. Its arrow-menu plus three fixed right controls, four fixed icon-label chips, trailing three-sparkle circle, absence of any standalone bottom-right down-arrow, and `4 vp` AI-notice/navigation gap are normative. The sparkling-call glyph uses a smaller upper star and larger lower star; the more glyph uses four small solid dots. User messages are right-aligned asymmetric light-blue shapes with a square upper-right corner; Xiaoyi answers are unboxed and left-aligned. Resolve `E` from the current device class, use `T=E+8 vp`, and compute every component inside the current active column `K`; never scale the `440 x 744 vp` reference page. Screenshot status content is ignored, source imagery/private text is not bundled, and all geometry is reconstructed responsively in vp/fp.
