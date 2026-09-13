# Phone-in-Hand Contact and Occlusion Compositing

Use this reference whenever a rendered phone is held, touched, or closely surrounded by hands or fingers. It supplements [device-preview-frames.md](device-preview-frames.md): that file establishes the protected device master and bezel geometry; this file governs pose planning, finger/device depth, contact edges, hand masks, and regression checks.

## Scope and precedence

- Apply these rules to every mapped phone model, fold state, and portrait or landscape orientation.
- A current user instruction or approved project-specific contact map controls which fingers may cover the device. Do not generalize one project's grip into a universal HarmonyOS hand pose.
- The official mapped bezel remains the sole source of truth for the phone. Never deform, redraw, regenerate, resize independently, or generatively repair the frozen device master to fit a hand.
- Preserve all system-chrome, screen-aperture, camera/cutout, navigation, and bezel-validation rules from the parent skill.
- Natural gaps created by a genuinely bent finger are allowed. Background-colored gaps at a declared physical-contact edge, matte fringes, and bezel pixels visibly passing through foreground skin are defects.

## Plan the grip from the device

Resolve the exact device master before designing the hand pose. Use the device's physical presentation width, height, aspect ratio, corner curvature, orientation, and intended touch targets to set:

- palm-to-palm spacing;
- finger reach and joint flexion;
- thumb joint bend and touch location;
- which digits remain behind the phone;
- where skin contacts, approaches, or clears the bezel.

Do not paste a grip designed for a conventional narrow straight phone onto a wider or differently proportioned device. A wider landscape phone usually needs a wider-support geometry, less index-finger curl, and thumb reach adjusted independently from the distance between the two hands. Treat these as ergonomic relationships, not fixed coordinates.

When the requested pose is uncomfortable or cannot meet the mapped phone without distortion, regenerate or reposition the hands. Never modify the phone to rescue the pose.

## Create a contact map before generation or masking

Divide each visible finger/device boundary into short, inspectable segments. Assign exactly one relationship to every segment:

| Relationship | Meaning | Required visible result |
|---|---|---|
| `foreground_occlusion` | Skin is physically in front of the device | The complete skin silhouette covers the intended bezel/screen area; no device pixel passes through the skin |
| `behind_device` | Finger or hand is behind the phone | The official bezel remains continuous and fully visible in front; no hand mask crosses onto it |
| `physical_contact` | Skin and device meet at the same visible boundary | No background-colored pixel, transparent hairline, or matte halo separates the two surfaces |
| `natural_clearance` | A real air gap is created by anatomy or joint curvature | The gap is retained, has a plausible shape, and is not filled merely to make the contact look tighter |

Record at least:

| Field | Required content |
|---|---|
| Side and digit | left/right and thumb/index/middle/ring/little finger or palm region |
| Boundary segment | the relevant corner, upper edge, side edge, lower edge, or screen region |
| Relationship | one of the four values above |
| Layer owner | rear hand, frozen device master, or foreground hand |
| Expected device visibility | complete, partially occluded, or fully occluded within the segment |
| Gap policy | zero contact gap or intentional natural clearance |
| Review anchor | nearby corner, nail, joint, hardware feature, or accepted opposite-side segment |

Do not describe an entire hand as simply “in front” or “behind.” Split one source hand into separate rear and foreground masks whenever different digits occupy different depth planes.

## Fixed layer order

Build every phone-in-hand scene in this order:

1. Background or environment.
2. Rear-hand regions and all digits classified as `behind_device`.
3. Frozen, already validated screen-plus-official-bezel device master.
4. Foreground hand regions classified as `foreground_occlusion`, using explicit masks.
5. Local contact-edge blending or contact shadow only when physically justified, clipped to the approved contact segment and never used to hide a seam broadly.

The same hand photograph or generated hand may supply both rear and foreground regions, but the masks must be separate. Do not flatten the layers until device invariance and contact checks pass.

## Contact and occlusion rules

### Foreground fingers and thumbs

- Extend the foreground mask through the complete skin contour at every intended overlap. The mask must not terminate early at a thumb root, fingertip, nail edge, or curved contact point.
- Cover only the device area that the contact map marks as occluded. Preserve the remaining bezel continuously.
- Where skin meets the bezel, allow a small mask overlap into the already-approved occluded device area so antialiasing cannot reveal a background sliver. Derive the overlap at the current output scale; do not define one universal pixel value.
- Reject any bezel highlight, colored frame line, screen pixel, or contact shadow that appears to travel through foreground skin.

### Fingers behind the device

- Keep the complete official bezel above all `behind_device` regions.
- A rear finger may approach or touch the outer contour but may not cover or erase the frame unless the contact map explicitly reclassifies that segment as foreground.
- Close unintended background gaps by correcting the rear-hand pose or mask boundary, not by painting over the bezel.
- Middle, ring, and little fingers that support the phone from behind may be partly or wholly invisible. Do not force them into view for symmetry.

### Corners and transitions

- Inspect every device corner where a finger changes from contact to clearance or from behind to foreground.
- Preserve the official corner curve wherever the contact map says the bezel is visible.
- Do not let a broad hand mask flatten a corner, shorten a side rail, or change the apparent device radius.
- A natural wedge-shaped clearance caused by a bent finger is valid; a thin white or background-colored line that follows the skin/device boundary is not.

## Hand matting and edge quality

- Preserve the full anatomy of fingertips, nails, cuticles, finger pads, thumb roots, and narrow skin folds. Do not over-erase these regions during cutout work.
- Remove source-background contamination at the alpha edge with edge-color decontamination or a better source mask. Do not conceal a white fringe by blurring the whole hand, expanding a skin-colored blob, or retouching the phone.
- Keep edge antialiasing proportional to the final preview or native scale. Avoid hard stair-steps, translucent double edges, white/gray halos, and excessive feathering.
- When a source was generated on white, inspect it on black and a saturated color before using it. When generated on a dark background, also inspect it on white.
- If a finger or nail is clipped, restore or regenerate the hand source. Do not crop the defect away by moving the phone over it.

## Bilateral coordination

Treat left and right hands as coordinated but anatomically independent.

- Match intended grip depth, contact type, and approximate exposure across corresponding digits.
- Do not mirror one mask mechanically when perspective, lighting, joint posture, or screen touch targets differ.
- When one side has been approved, use it as the visual reference for the corresponding side's exposure and contact relationship.
- Compare index-pad visibility, thumb-root overlap, distance to the nearest corner, and visible bezel continuity side by side.
- A local correction on one side must not silently change the other side.

## Revision and regression control

After a contact region is approved, lock its hand source, mask, device placement, and device-master pixels.

For every subsequent local correction:

1. Define a small region of interest around the requested defect.
2. Modify only the relevant hand pose or hand mask.
3. Keep the frozen device master unchanged.
4. Compare the new composite with the last approved version outside the region of interest.
5. Reject unexplained changes outside that region.
6. Re-run the complete contact checklist, because repairing a side or finger can reintroduce a thumb, corner, root, or opposite-side defect.

Do not replace an approved full composite with a fresh one-pass generated scene to make a local fix.

## Validation

Retain the bezel/aperture validation from [device-preview-frames.md](device-preview-frames.md), then validate the hand/device relationship separately.

### Pixel and mask invariants

- Outside the union of approved foreground-occlusion masks and explicitly scoped contact-blend masks, placed device pixels must match the frozen device master exactly.
- Along every `physical_contact` segment, no connected run of background-colored or transparent pixels may separate skin from device.
- Along every `behind_device` segment, no hand foreground-mask pixel may cover the visible bezel.
- Inside every intended foreground skin silhouette, no device pixel may remain visible through the hand.
- Outside the current edit region, the new composite must match the last approved composite unless a difference is documented and approved.

Automate these comparisons whenever the project retains masks and layer coordinates. If the source is not deterministic enough for a reliable pixel classifier, perform them as explicit overlay/difference inspections and record the result rather than claiming an automated pass.

### Contrast-background inspection

Inspect the flattened result at 400% or equivalent pixel-level zoom on white, black, and a saturated diagnostic background. Check both sides independently, especially:

- index-finger pads near upper corners;
- thumb roots and the bezel segments they cover;
- fingertips, nails, and cuticles;
- middle- and ring-finger roots beside side rails;
- transitions between contact and natural clearance;
- all four phone corners;
- any location edited in a previous revision.

Reject the output for:

- white or background-colored contact seams;
- transparent hairlines or matte halos;
- bezel/frame pixels crossing foreground skin;
- hand pixels covering a segment classified as behind-device;
- clipped fingertips or nails;
- inconsistent left/right exposure not explained by pose or perspective;
- a local fix that regresses a previously approved region;
- any unapproved change to the frozen device master.

## Pura X View landscape regression case

Use the previously approved two-hand Pura X View landscape grip as a regression scenario, not as a universal pose template:

- Construct the phone first at the mapped Pura X View landscape size and rotate the untouched official bezel 90 degrees counterclockwise, with the front camera on the left.
- The approved project contact map allows the thumbs to occlude the screen/bezel. Other fingers remain behind or adjacent to the frame, so all bezel not covered by the thumbs stays complete and visible.
- The wider phone requires a less-curled, more comfortable index-finger posture than a conventional narrow straight-phone grip. Set hand spacing and thumb joint bend independently.
- No background seam may remain at either index pad or at the visible middle/ring-finger root contact areas. Preserve only genuine clearance created by natural finger curvature.
- Neither thumb may show frame penetration at its root or contact boundary. The foreground thumb masks must contain the complete visible skin silhouettes.
- Corresponding left/right index exposure and contact depth should match unless perspective supplies a clear reason for a difference.
- Recheck every previously approved contact after each local edit.

Do not store the project's exact finger coordinates, source images, or masks as global HarmonyOS tokens.

## Delivery evidence

For production handoff or an editable source package, retain:

- the frozen validated device master;
- rear-hand and foreground-hand layers;
- the foreground-occlusion mask;
- the contact map;
- device and hand placement coordinates;
- the edit region for the latest revision;
- device-invariance and outside-region difference results;
- white, black, and saturated-background inspection evidence.

Observable acceptance criterion:

> The phone retains its exact approved geometry and every unoccluded bezel pixel. Each finger/device boundary follows an explicit contact-map relationship: foreground skin fully covers only its intended device area, rear fingers never cover the bezel, physical-contact segments contain no background seam or matte halo, and natural anatomical clearance remains intact. Fingertips and nails are complete, no frame passes through foreground skin, corresponding left/right grip relationships are coherent, and a local correction introduces no regression elsewhere.
