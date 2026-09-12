# WeChat Chat Interface Reference

Use this reference when a request explicitly shows WeChat, asks for a WeChat conversation screen, or uses a WeChat chat as the unobscured application background beneath a system surface. It is a textual reconstruction of the user-supplied 908 x 1536 screenshot reviewed on 2026-09-12. The screenshot itself is deliberately not bundled as an asset.

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

- Keep the composer fixed above the system interaction region.
- Reference-derived composer/system-bottom surface: approximately `#F6F6F6`.
- Place a white rounded text field in the center. Keep voice input at the left and microphone, emoji, and add controls in a clear horizontal sequence.
- Use neutral dark outline icons. The voice, emoji, and add controls read as circular outline controls; the microphone may sit inside the trailing end of the white input field.
- Preserve comfortable touch targets and keyboard transition behavior. When the keyboard appears, move the composer with it and avoid duplicating the device navigation inset.

## System overlays above the conversation

When a Live View card, system alert, privacy surface, or another system-owned overlay is shown above the chat:

- Composite it above the existing conversation rather than pushing the app bar or message list downward to make room.
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
- App bar, conversation, bubbles, time separators, avatars, and composer preserve the described hierarchy.
- Incoming and outgoing message ownership is unambiguous.
- Fictional content replaces all source personal data.
- A system overlay covers the conversation layer without reflowing it unless the requested interaction explicitly changes layout.
- The navigation indicator uses the current HarmonyOS geometry plus the applicable semantic/translucent visual treatment.
