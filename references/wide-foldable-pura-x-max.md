# Pura X Max-like Wide-Foldable Adaptation

Use this supplement for Pura X/Pura X Max-like wide foldables and devices with a comparable wide-folded family ratio. It extends the HarmonyOS baseline; it does not replace it.

## Contents

1. Scope and state resolution
2. Continuity and system behavior
3. Application architecture
4. Immersive browsing
5. Component adaptation
6. Content-pattern adaptation
7. Delivery checks

## 1. Scope and state resolution

- A wide foldable has a broad horizontal viewport and an unfolded state close to a book proportion. Its outer display is smaller than its inner display and needs targeted adaptation.
- Apply the general continuity principles to the whole device family and to comparably proportioned devices.
- Apply rules explicitly marked **outer display** only when the target is the Pura X/Pura X Max-like compact outer display or an equivalent compact screen state.
- Do not automatically treat Pura X Max unfolded portrait as an outer display. Resolve device, fold state, screen role, orientation, and current window width/height first.
- Keep the existing Pura X Max unfolded portrait default canvas and bezel from [device-preview-frames.md](device-preview-frames.md) unless the request specifies another state or device.

## 2. Continuity and system behavior

### Layout integrity

- During folding, unfolding, or orientation change, prevent image/video/control misalignment, truncation, overlap, deformation, and blur.
- Keep outer-display text and icon sizes equal to their inner-display counterparts. Adapt composition and overflow instead of shrinking essential content.

### Outer-display system chrome

- Hide the navigation bar and remove its reserved vertical space.
- Hide the status bar and remove its reserved vertical space.

### Outer-display window behavior

- The outer display does not support floating-window or split-screen mode.
- If the device folds while inner-display floating or split windows exist, open the focused window full screen on the outer display and move non-focused windows to the background.
- Picture-in-Picture is supported on the outer display. It may start through the Picture-in-Picture button or a qualifying video-detail swipe-up exit flow.
- If Picture-in-Picture is already open on the inner display, continue it without interruption after folding to the outer display.

## 3. Application architecture

- Preserve the inner app's basic structure on the outer display: title area, primary content area, and optional bottom area such as tabs or a toolbar.
- Keep functionality and displayed content complete and interactive.
- For lists, grids, and waterfall/scroll layouts, retain the structure and place overflow off-screen for scrolling. The top title and bottom navigation/toolbar may temporarily hide during scrolling.
- For fixed layouts, allow controlled compression or transformation only when all content remains complete and interactive. Do not overlap or clip elements.

## 4. Immersive browsing

Use immersive hiding where compact dimensions make it valuable:

- General judgment condition shown by the source: horizontal dimension `[320, 600]` and vertical dimension `[0, 680)`.
- Special judgment condition: horizontal dimension `[600, ∞]` and vertical dimension `[0, 480]`; the height condition also applies in portrait split-screen scenarios.
- Treat these as source-defined window-size conditions. Do not reinterpret them as the baseline's horizontal architecture breakpoints.

Choose the interaction by content:

| Scenario | Hide/reveal behavior |
|---|---|
| News, general information, feeds | Swipe up to hide bottom tabs/toolbars/title; swipe down to restore; restore at the top or bottom boundary |
| Messages and chat history | Swipe down to hide; swipe up or tap to restore; an optional variant keeps controls hidden on swipe-up and restores them on tap |
| Novel reader | Tap to hide; tap again to restore |

Choose the presentation type:

- **Full hide:** hide top and bottom controls together for news, browser, and detail-reading pages.
- **Partial hide:** retain lightweight content or controls while expanding list/feed space.
- **Gradient blur:** use the source's softened transition variant for list/feed immersion.
- Outer-display immersive top banners must scale proportionally, remain at most 60% of screen height, avoid image/text deformation, and keep core content fully visible.

## 5. Component adaptation

| Component | Outer-display rule |
|---|---|
| Title bar | Convert a large title to a small title to reduce empty space |
| Search | Convert a full search field to a search icon in the title row |
| Alphabet index | Use a segmented index; long-press a segment and slide to select an exact letter |
| Popup/dialog | Prefer the system control; keep the popup body and any outside interactive objects fully visible; total height <= 90% of screen height |
| Half-modal | Preserve all functions; make overflow scrollable; maximum extent leaves 8 vp below the window top |

## 6. Content-pattern adaptation

### Image and text details

- For a single image above text, scale the image proportionally and keep its height at or below 60% of window height so both image and details remain visible.
- For multiple images above text, scale proportionally and convert formerly swipe-only images into an extended layout on the outer display.

### Long video

- Keep the video image fully visible and make the upper area a fixed/frozen region.
- On upward scroll, proportionally shrink the frozen top region to 40% of screen height; restore it on downward scroll.
- Outer-display full-screen video does not rotate; retain the current orientation.

### Short video and live video

- Keep the full image visible without cropping.
- Horizontal 16:9, 21:9, and 4:3 video fills the width and adapts height.
- Vertical 9:16 video fills the vertical content-area height and adapts width.
- Side controls must not truncate or overlap; make them scrollable when necessary.
- Bottom live comments/barrage must not exceed 50% of window height.

### Comments

- Default comment-region height is at least 40% of screen height.
- Keep the comment input fully visible.
- Pull upward to expand comments full screen; swipe downward to restore.

### Sign-in

- Compress excessive whitespace.
- Keep top and bottom action areas fixed.
- Make incomplete middle content scrollable. Do not use a fixed composition that overlaps or clips content.

## 7. Delivery checks

- Label every frame as inner/unfolded or outer/compact display and record orientation/window dimensions.
- Verify fold/unfold continuity for task state, scroll position, media playback, and Picture-in-Picture where relevant.
- Verify that outer-display text/icons retain inner-display size while the layout adapts through scrolling, compression, or transformation.
- Verify status/navigation bar and multi-window behavior against the actual screen role.
- Check all percentage and vp limits against the authoritative PDF figure when they affect implementation.
- Apply the mapped device bezel to every rendered phone frame unless the user explicitly requests an allowed bezel-free output.
