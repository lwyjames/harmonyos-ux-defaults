# Status Bar and Navigation Bar Design Verification

Use this reference before composing top/bottom app chrome and again before delivery. The bundled status-bar and navigation-bar PDFs remain authoritative for behavior. The corrected user-supplied responsive geometry in [navigation-bar-geometry.md](navigation-bar-geometry.md) controls the visible navigation indicator and its interaction region.

## 1. Resolve ownership and state

For every frame or prototype state, record:

- device, orientation, fold/screen role, and window mode;
- whether the status bar and navigation bar are visible, temporarily hidden, absent, or system-owned;
- which background extends behind each bar;
- app-owned safe area, fixed/floating controls, scroll-end padding, and keyboard behavior;
- reveal gesture, auto-hide timing, and layer order when relevant.

Do not copy the normal portrait treatment into every state. Apply the state-specific matrix below.

### Navigation-bar presence gate

- Default to **visible** for every normal full-screen phone app window, including Pura X Max unfolded portrait.
- Treat absence as an exception that requires one of these reasons: explicit user override; floating window; Picture-in-Picture; Pura X/Pura X Max-like compact outer display; or the post-timeout hidden phase of a qualifying immersive experience.
- If the state is unclear or no exception can be named, render the navigation bar. Do not optimize it away for aesthetics or screen space.
- Render the system navigation indicator inside the screen opening. A hardware bezel, app tab bar, toolbar, or bottom action is not a substitute.
- Use one system navigation indicator only. Do not duplicate it in both the UI canvas and bezel artwork.
- Calculate every visible navigation indicator from [navigation-bar-geometry.md](navigation-bar-geometry.md): a horizontally centered 6 vp-high capsule, its bottom edge exactly 6 vp above the visible screen bottom, and responsive width `112 vp` for `360 <= W < 600`, `W / 3 - 48 vp` for `600 <= W <= 840`, or `W / 4 - 48 vp` for `W > 840`. Derive the visible boundary from the mapped bezel's center-connected alpha aperture; ignore raw canvas rows occluded by the bottom bezel.
- Keep the centered `35% W x 28 vp` interaction region separate, invisible, and bottom-anchored. Do not turn it into a visible 28 vp-high capsule or background.
- In a single static immersive mockup with no phase specified, render the initial/default visible state. In a multi-frame sequence, include the initial/revealed visible state and post-timeout hidden state when the transition matters.

## 2. Status bar rules

- Treat the status bar as the system-owned top region containing time, connectivity, battery, and device-state information.
- Default static phone time to **08:08** unless a different time is required to communicate the scenario accurately.
- At the status bar's right end, follow `assets/system-chrome/status-bar-right-default-reference.png`. Match its physical left-to-right order: NearLink logo, Wi-Fi 7 logo, dual stacked 5A cellular signals, battery 100. From the screen's right edge inward, this is battery, dual 5A, Wi-Fi 7, NearLink.
- Preserve the reference icon anatomy and relative spacing. Do not replace NearLink with a generic Bluetooth/NFC symbol, omit the Wi-Fi 7 identifier, collapse dual 5A into one cellular row, or replace battery 100 with a generic battery state.
- Keep its content clear of the device camera/cutout and rounded corners.
- Use a transparent background by default and extend the page background through the region for an integrated appearance. Do not create an unrelated strip solely behind the status bar.
- Select black or white status content from the local background, not from the page's average color.
- Maintain a contrast ratio of at least 1.9 between status content and the page background beneath it.
- Avoid a strong left/right background contrast split that makes only part of the status content readable. Adjust the image crop, overlay, gradient, or surrounding surface while preserving content intent.
- Hide the status bar only for a justified full-screen immersive state or a source-defined state such as phone landscape, split-screen, or a Pura X/Pura X Max-like compact outer display.
- When temporarily hidden, provide a simple gesture that reveals it and define how it returns to the hidden state.
- When Live View occupies the status-bar host, read [live-view-sketch-spec.md](live-view-sketch-spec.md). Align its system-owned capsule to a centered punch hole or to the left on side-punch/no-hole devices, verify coexistence with fixed status elements, and use the 128 x 28 expanded state only when measured host space permits. Do not copy the Sketch documentation-artboard coordinates into the device frame.

## 3. Navigation bar rules

- Navigation-bar adaptation is mandatory for native apps, WebView content, and third-party frameworks.
- Treat the 6 vp capsule height, 6 vp **bottom-edge-to-visible-screen-bottom** gap, responsive logical-width formula, and separate bottom-anchored `35% W x 28 vp` interaction region as mandatory geometry. The earlier `1252 x 84 px`, 42 px radius, and 16 px gap are invalid. Runtime implementation uses the HarmonyOS system bar and reported insets.
- When present, extend an immersive app background behind the navigation region and keep bottom controls clear of the 28 vp interaction region.
- Do not treat the 28 vp as universal padding: floating windows, Picture-in-Picture, and compact outer displays do not display the navigation bar and must not retain wasted space.
- Scrollable content may pass behind the navigation region, but its final content/action must lift above it. Keep any bottom scrollbar from overlapping the navigation bar.
- Lift fixed and floating bottom controls above the visible navigation bar. Test with the keyboard hidden and shown so neither the keyboard nor system navigation obscures the primary action.
- In a half-modal, scrollable content may extend behind the navigation region, but the final action remains unobscured. The system navigation bar stays above the modal/popup layer.
- In normal landscape, the navigation bar remains visible and must be adapted; app bottom controls are usually hidden.
- In immersive full-screen content, show the navigation bar initially, auto-hide it after 2 seconds without interaction, and reveal it with an upward swipe from the bottom.
- In games, support anti-accidental-touch behavior: the second upward swipe performs system navigation. Other immersive scenarios use one upward swipe.
- For wide-screen immersive content, fill the available display rather than reducing the content into a smaller band because of the navigation region.
- For short video, fill the vertical display and keep bottom controls above the navigation region.

## 4. Required state matrix

| State | Status bar | Navigation bar | Verification focus |
|---|---|---|---|
| Normal portrait | Visible | Visible and rendered | Cutout avoidance, local contrast, integrated backgrounds, 28 vp interaction-region clearance |
| Live View capsule | Visible/system-owned host | Follow the underlying window state | 80 x 28 default or space-verified 128 x 28 expanded geometry; cutout anchor; no collision with time/connectivity/battery; no simultaneous card |
| Normal phone landscape | Temporarily hidden | Visible and rendered | More content vertically; navigation adaptation remains; app bottom controls usually hidden |
| Full-screen immersive | Temporarily hidden when justified | Initially visible and rendered; hides after 2 seconds | Single unspecified static frame shows visible phase; sequences communicate visible/revealed and hidden phases |
| Scrollable page/WebView | Visible unless state says otherwise | Visible and rendered | Content may pass behind; final item/action and bottom scrollbar clear the bar |
| Fixed or floating bottom action | Visible unless state says otherwise | Visible and rendered | Action lifts above navigation and remains usable with keyboard shown |
| Half-modal or popup | Visible unless state says otherwise | Visible and rendered above modal layer | Scroll overflow safely; final action and popup do not collide with the bar |
| Top/bottom split | System status bar hidden | Rendered at device bottom; lower window adapts | Upper window is not over-lifted; lower window has no overlap |
| Left/right split | System status bar hidden | Rendered at device bottom; both windows adapt | Each side's bottom controls remain clear |
| Floating window | Window-specific | Absent inside window | Remove inherited bottom inset; avoid wasted space |
| Picture-in-Picture | Not represented as app chrome | Absent inside window | No duplicated system chrome or wasted inset |
| Pura X/Pura X Max-like compact outer display | Hidden; release space | Absent; release space | Do not apply this restriction to the unfolded inner display |
| Short video | State-dependent | Visible and rendered unless explicitly showing the post-timeout immersive phase | Video fills vertically; bottom controls never overlap navigation |
| Game | Immersive/temporarily hidden | Initially visible and rendered; hides after 2 seconds | Bottom swipe reveals; second swipe performs navigation |

## 5. Design workflow checkpoint

Before high-fidelity styling:

1. Draw system-owned top/bottom regions and the physical cutout/rounded-corner exclusions.
2. Choose the content/background extension and black/white status-content mode for every visual state.
3. Place scroll-end padding and fixed/floating actions according to the actual navigation-bar state.
4. Render the system navigation indicator in every state classified as visible; calculate the centered 6 vp-high capsule and 6 vp bottom-edge gap from the current logical screen width, then define the separate centered `35% W x 28 vp` bottom interaction region rather than relying on an annotation or bezel to imply its presence.
5. Set static time to 08:08 and construct the right-side cluster from the supplied NearLink/Wi-Fi 7/dual-5A/battery-100 reference unless a documented scenario override applies.
6. Add window-mode, orientation, keyboard, fold-state, immersive, and modal variants that materially change system chrome.
7. Mark every deliberate omission or time override with its qualifying state and cite the governing source or user instruction.
8. If Live View is present, mark its capsule host, cutout anchor, default/expanded state, and collision envelope; record why the chosen state fits the available status-bar width.

## 6. Delivery evidence

- Include at least one annotated frame or implementation note showing status/navigation ownership and safe-area boundaries.
- Perform a frame-by-frame presence audit: every required navigation bar is visibly rendered, and every omission has a documented exception.
- Measure every present phone navigation indicator in logical units: height 6 vp, bottom-edge gap 6 vp, horizontal center alignment, and the correct responsive width branch for current `W`. Separately measure a centered `35% W x 28 vp` invisible interaction region flush with the bottom. For bezel-free screen-only output, use the raw canvas bottom; for bezeled output, use the center-connected aperture's visible bottom.
- Reject any fixed `1252 x 84 px`, 42 px radius, or 16 px gap; reject a rectangular indicator, a gap measured from the centerline, a 28 vp-high visible indicator, or a hot region inferred from the indicator bounds.
- Verify 08:08 in every static phone frame without a scenario-specific time and verify the right-side cluster's NearLink, Wi-Fi 7, dual stacked 5A, battery-100 anatomy and order.
- For every Live View capsule, verify the measured 80 x 28 or 128 x 28 geometry, correct centered-hole versus left-side placement, clear separation from fixed status content, and mutual exclusion with the floating/card form.
- Reject a normal full-screen phone mockup that omits the navigation bar, even when its bottom spacing happens to look safe.
- Verify the darkest and lightest status-region backgrounds, including imagery and gradients, against the 1.9 threshold.
- Inspect the final scroll position, keyboard-open state, modal/popup state, and every fixed/floating bottom action for overlap.
- Test navigation appearance/disappearance and reveal gestures in immersive states; test the second-swipe rule for games when applicable.
- Inspect portrait, landscape, split, floating, Picture-in-Picture, fold/outer-display, and short-video states only when the requested experience supports them; do not invent irrelevant states.
- Reject delivery if any system icon, time, bottom action, final list item, scrollbar, modal control, or video control is clipped, low-contrast, duplicated, or obscured.
