# WeChat Chat Interface Reference

Use this reference when a request explicitly shows WeChat, asks for a WeChat conversation screen, or uses a WeChat chat as the unobscured application background beneath a system surface. It is a textual reconstruction of the user-supplied 908 x 1536 screenshot reviewed on 2026-09-12, supplemented by three correction crops reviewed the same day. The screenshots and crops are deliberately not bundled as assets.

## Scope and precedence

- Apply this reference to the **application-owned WeChat/chat layer** only.
- Ignore the source screenshot's status-bar time, icons, spacing, and styling. In a HarmonyOS mockup, the HarmonyOS status-bar, cutout, device-bezel, and time rules remain authoritative.
- Use [navigation-bar-geometry.md](navigation-bar-geometry.md) for the system navigation indicator's geometry and the light-surface treatment derived from this screenshot.
- Do not present these screenshot-derived values as official WeChat or HarmonyOS design tokens. They are project reconstruction defaults for faithful mockups.
- Do not reproduce the screenshot's contact name, avatars, private message text, ticket number, or stickers. Use fictional, task-appropriate content and non-identifying avatar imagery.

## Page architecture

Build the screen as four vertically ordered layers:

1. HarmonyOS system status region, governed by the system-chrome rules rather than this reference.
2. A fixed conversation app bar with a back control at the left, the contact title optically centered, and a three-dot overflow control at the right.
3. A vertically scrollable conversation field on a uniform light-neutral background.
4. A fixed composer above the system navigation region, followed by the system-owned navigation area.

The app bar and conversation field share the same light-neutral background so the transition is quiet. Separate the app bar from the messages with a thin, low-contrast divider. Do not use an elevated card, large title treatment, or colored toolbar.

## Conversation app bar

- Resolve the complete HarmonyOS status region and cutout-safe boundary first. Start the app-owned conversation bar **below** that boundary; never place the back control or title inside the status region.
- Use a compact `44 vp` conversation bar. Place its controls on the bar's vertical centerline. The title center is therefore `22 vp` below the resolved status-region bottom, rather than being anchored to the canvas top, clock, or camera hole.
- The leading control is a **standalone back chevron only**. Do not render the word `微信`, `WeChat`, a previous-page label, or another text label beside it.
- Give the leading control a `48 x 44 vp` interaction slot and inset the visible chevron approximately `16 vp` from the logical left edge. Keep the chevron's visible bounds entirely below the status-region boundary so it has clear vertical separation from the system clock and can never appear attached to `08:08`.
- Keep the contact title optically centered in the full canvas, not merely in the space between left and right controls. Do not place it immediately under the punch hole or on the status/app-bar seam; the resolved status region contains the cutout, and the title belongs to the bar below it.
- Keep the overflow control in a symmetric `48 x 44 vp` trailing slot. Default to title text only; decorative hearts, badges, or presence marks require explicit scenario content and are not inferred from the standard reference.
- Do not solve top-edge crowding by changing the HarmonyOS status-bar geometry. Move and size only the app-owned conversation bar.

## Conversation field

- Reference-derived conversation background: approximately `#EDEDED` in the supplied flattened JPEG.
- Center time separators in the available width. Use small, low-emphasis neutral-gray text with no pill, card, shadow, or divider line.
- Stack message groups chronologically with visibly more space around time separators than between consecutive messages from the same sender.
- Incoming messages align left: avatar first, then a white bubble with a small tail pointing toward the avatar.
- Outgoing messages align right: green bubble first, then the sender avatar, with a small tail pointing toward the avatar.
- Reference-derived outgoing bubble appearance: a bright, soft yellow-green near `#AAEA7A` in the flattened JPEG. Treat this as an effective appearance rather than a guaranteed source color value.
- Incoming bubble appearance: neutral white. Body text is near-black. Link-like or tappable inline text may use a restrained blue while preserving surrounding text hierarchy.
- Use square avatars with gently rounded corners. A practical responsive reconstruction uses a `40 vp` avatar, approximately `12 vp` outer edge inset, and approximately `12 vp` avatar-to-bubble gap; adapt only when the selected device width or text scale requires it.
- Let bubble width follow content up to roughly two-thirds of the conversation width. Use compact padding and small radii; do not turn chat bubbles into large floating cards.
- Preserve natural Chinese line breaking. Do not shrink text, distort avatars, or stretch bubbles to force the screenshot's exact wrapping on a different canvas.

## Composer

- In the normal full-screen, keyboard-hidden state, use a compact `56 vp` app-owned composer controls band immediately above the system-owned `28 vp` bottom interaction region:

```text
composerY = H - 28 vp - 56 vp
composerHeight = 56 vp
```

- Do not add a blank spacer between the composer and the system interaction region. Continue the same bottom surface through both regions so the composer visually meets the navigation substrate while ownership remains distinct.
- Reference-derived composer/system-bottom surface: approximately `#F6F6F6`.
- Use a `40 vp`-high white rounded text field, vertically centered in the `56 vp` band with `8 vp` top and bottom insets. Vertically center the voice, microphone, emoji, and add controls on the same line; do not let the microphone or field float upward into a tall empty footer.
- Keep voice input at the left and microphone, emoji, and add controls in a clear horizontal sequence.
- Use neutral dark outline icons. The voice, emoji, and add controls read as circular outline controls; the microphone may sit inside the trailing end of the white input field.
- Use a `32 vp` visible circle for the trailing add control. Anchor its outer right edge exactly `12 vp` from the **visible screen aperture's logical right edge**:

```text
addDiameter = 32 vp
addRight = W - 12 vp
addCenterX = W - 28 vp
```

- The trailing touch slot may remain larger than the visible circle, but it must not create a visible empty column after the add control. Do not center the whole composer group inside a narrower container or reserve an unused trailing gutter. Resolve this inset from the visible logical screen edge, never from the outer bezel PNG canvas.
- Preserve comfortable touch targets and keyboard transition behavior. When the keyboard appears, move the composer with it and avoid duplicating the device navigation inset; the `H - 84 vp` placement formula applies only to the keyboard-hidden full-screen state.

## System overlays above the conversation

When a Live View card, system alert, privacy surface, or another system-owned overlay is shown above the chat:

- First construct the complete normal WeChat state with the conversation title bar and chronological messages positioned exactly as they would be without any overlay. Freeze that app layer, then composite the Live View above it. Do not begin message layout from the Live View's lower edge.
- Preserve every title, time-separator, avatar, bubble, and scroll coordinate between the card-free and card-present states. The Live View must never change the conversation's scroll position, top content inset, message order, or vertical spacing.
- In an established conversation mockup, place at least one earlier time separator or message group naturally below the normal app bar and within the area the expanded card will later cover. After compositing, that earlier content is blurred/occluded in place; it is not deleted or moved below the card.
- Reject a composition whose first time separator or first message starts at `cardBottom + gap`, or whose top conversation area becomes a deliberately clean buffer matching the card height. A visible message below the card is acceptable only when a card-free base frame proves its coordinate was already there.
- Apply the universal expanded-phone-card stacking, material, and cross-device rules in [expanded-live-view-card.md](expanded-live-view-card.md). Those rules apply over every app and scene; they are not WeChat-specific.
- In the WeChat mapping of that universal rule, the app-owned region to occlude is the complete conversation-title region. The back chevron, contact title, decorative title marks, and overflow control must not peek around or remain legible through the expanded card, while the HarmonyOS status bar remains visible.
- Preserve enough recognizable conversation context around the overlay to communicate that the user remains in WeChat.
- Respect the overlay's own material, geometry, collision, and system-chrome rules.
- Do not tint the entire conversation to match the overlay unless the governing system surface explicitly requires a scrim or blur.

## Navigation visual treatment learned from the screenshot

The supplied flattened JPEG shows an effective navigation-region background near `#F6F6F6` and a centered indicator near `#E3E3E3`. Over the observed background, this is consistent with a neutral-black overlay at approximately `8%` opacity:

```text
light navigation substrate: approximately #F6F6F6
indicator model: rgba(0, 0, 0, 0.08)
observed flattened result: approximately #E3E3E3
```

Because JPEG pixels contain antialiasing and compression and the original layer stack is unavailable, `8%` is a screenshot-derived **project default**, not a recovered official alpha token. Apply the cross-application rules and exceptions in [navigation-bar-geometry.md](navigation-bar-geometry.md).

## Verification

- No source screenshot or crop is present in `assets/` or any deliverable package.
- The status bar follows HarmonyOS, not the supplied screenshot.
- The app bar starts below the resolved status region, is `44 vp` high, contains only a standalone back chevron at the leading edge, and keeps the title and controls on its vertical centerline.
- The back chevron has clear vertical separation from the system clock; no `微信` back label is present.
- The title is centered in the app bar below the cutout-safe status region rather than crowded against the screen top, camera hole, or status/app-bar seam.
- App bar, conversation, bubbles, time separators, avatars, and composer preserve the described hierarchy.
- In the keyboard-hidden state, the composer controls band is `56 vp` high, begins at `H - 84 vp`, uses a centered `40 vp` field, and directly adjoins the separate `28 vp` system interaction region without extra vertical padding.
- The trailing add circle is `32 vp` in diameter with its outer right edge `12 vp` from the visible logical screen edge; there is no visible unused gutter to its right.
- Incoming and outgoing message ownership is unambiguous.
- Fictional content replaces all source personal data.
- A system overlay covers the conversation layer without reflowing it unless the requested interaction explicitly changes layout.
- A card-free comparison or separate-layer evidence shows identical title, time-separator, avatar, bubble, and scroll coordinates before and after overlay. At least one earlier conversation element remains underneath the expanded card in an established-chat example.
- The first visible uncovered message is not positioned from `cardBottom`; no synthetic empty band was inserted to make room for the card.
- An expanded Live View card covers the complete WeChat title region without hiding the HarmonyOS status bar; no back, title, badge, or overflow element remains visible or legible through it. This is the WeChat instance of the universal cross-application rule in `expanded-live-view-card.md`, not a WeChat-only material behavior.
- The navigation indicator uses the current HarmonyOS geometry plus the applicable semantic/translucent visual treatment.
