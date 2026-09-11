# HarmonyOS Security & Privacy Branding — Official Shield Visual

Status: **Supplementary rule**. This adds to the existing HarmonyOS UX Defaults baseline and does not supersede any existing design specification.

## Official asset

The file `assets/branding/harmonyos-shield-security-logo-official.ai` is the user-provided official **鸿蒙星盾安全 标准色 Logo (RGB)**.

Derived convenience assets are provided for design/prototyping workflows:

- `assets/branding/harmonyos-shield-security-logo-official-transparent.png` — transparent PNG render of the official vector artwork.
- `assets/branding/harmonyos-shield-security-logo-official.svg` — vector convenience export derived from the same PDF-compatible Illustrator source.

The original `.ai` file is the source of truth if any derived asset differs.

## Mandatory usage rule

For **all HarmonyOS security- and privacy-related product UX, prototypes, mockups, keyframes, launch visuals, system alerts, safety cards, permission/security notices, anti-fraud experiences, secure preview experiences, privacy protection experiences, and related developer handoff**, use this official shield as the default HarmonyOS security/privacy branding visual whenever a branded security/privacy emblem or shield icon is shown.

Examples include, but are not limited to:

- 鸿蒙星盾防诈 / anti-fraud
- screen-sharing fraud protection
- risk-call / risk-message / risk-app alerts
- secure preview
- app-access recall / permission recall
- privacy warnings and privacy protection surfaces
- sensitive-operation safety warnings
- system-level security and privacy education cards

## Do not invent substitutes

- **Do not create, redraw, approximate, or invent another shield icon.**
- Do not substitute a generic red warning shield, lock shield, checkmark shield, or third-party security icon when HarmonyOS security/privacy branding is intended.
- Do not alter the shield geometry, central blue bar, proportions, stroke shape, spacing, or silhouette.
- Do not add a colored icon tile/background behind the shield unless a separate HarmonyOS specification explicitly requires that container.
- Do not recolor the official standard-color logo merely to fit a dark surface. If contrast is insufficient, prefer a light/neutral alert/card container or another layout treatment that preserves the official artwork. Only use an alternate logo colorway when an official alternate asset is explicitly supplied.

## Color and appearance

The supplied standard-color artwork contains:

- Shield geometry: black (#000000)
- Center vertical mark: approximately RGB(31, 105, 255), hex **#1F69FF**
- Background: transparent in the supplied convenience PNG/SVG exports

Treat the original Illustrator artwork as authoritative for exact color values and vector geometry.

## Placement

- Preserve the original aspect ratio.
- Keep sufficient clear space so the outer shield silhouette is not crowded by text or controls.
- Do not stretch, rotate, skew, add perspective, add drop shadows, or place decorative shapes inside the shield.
- In compact notification/app-icon contexts, scale the full logo proportionally; never crop away the top/bottom split or center mark.
- In warning dialogs, use the logo as brand identification; urgency should come from message copy, hierarchy, or system alert styling rather than changing the shield itself to red/orange.

## Asset priority

When generating or editing security/privacy UX:

1. Use the original `.ai` asset when the workflow can consume Illustrator/PDF-compatible vectors.
2. Otherwise use the provided SVG.
3. Otherwise use the transparent PNG.
4. Never redraw from visual memory when one of these assets is available.

## Source

User-provided official file: `鸿蒙星盾安全_标准色logo_RGB(1).ai`.
