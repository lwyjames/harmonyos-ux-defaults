# HarmonyOS Sans Font Assets

Use the user-supplied `HarmonyOS+Sans.zip` package as the authoritative font-binary supplement. Keep the binary font files outside this skill so the skill stays below package-size limits. Do not treat a font filename alone as proof that the correct file is present; validate it against `harmonyos-sans-font-manifest.json` with `scripts/resolve_harmonyos_fonts.py`.

## Family and locale mapping

| Content or treatment | Required file | Internal family | Use |
|---|---|---|---|
| Simplified Chinese, including mixed Chinese/Latin UI | `HarmonyOS_Sans_SC.ttf` | HarmonyOS Sans SC / 鸿蒙黑体 | Default for `zh-CN` HarmonyOS UI |
| Traditional Chinese, including mixed Chinese/Latin UI | `HarmonyOS_Sans_TC.ttf` | HarmonyOS Sans TC / 鴻蒙黑體 | Default for Traditional Chinese UI |
| Latin-only UI | `HarmonyOS_Sans.ttf` | HarmonyOS Sans | Use when Chinese glyph coverage is not needed |
| Latin-only italic UI | `HarmonyOS_Sans_Italic.ttf` | HarmonyOS Sans | Use only when italic is explicitly required |
| Condensed Latin UI | `HarmonyOS_Sans_Condensed.ttf` | HarmonyOS Sans Condensed | Use only when the source or user explicitly requires condensed type |
| Condensed italic Latin UI | `HarmonyOS_Sans_Condensed_Italic.ttf` | HarmonyOS Sans Condensed Italic | Use only when both treatments are explicitly required |
| Arabic UI labels and controls | `HarmonyOS_Sans_Naskh_Arabic_UI.ttf` | HarmonyOS Sans Naskh Arabic UI | Use for Arabic interface text |
| Arabic reading text | `HarmonyOS_Sans_Naskh_Arabic.ttf` | HarmonyOS Sans Naskh Arabic | Use for longer Arabic text |

All eight files are variable fonts. The six Latin/Chinese families expose a `wght` axis from `40` to `900`; the two Arabic families expose `wght` from `100` to `900`. Use the existing HarmonyOS type-role weights through the variable axis. Do not synthesize bold, italic, condensed, or oblique forms when an exact supplied face exists.

## External asset resolution

Resolve fonts in this order:

1. An explicit `--font-dir` supplied for the task.
2. `HARMONYOS_FONT_DIR`.
3. `%LOCALAPPDATA%\HarmonyOSUXAssets\fonts` on Windows.
4. The current user's or system Windows font folder.
5. A task-local `font-assets`, `fonts`, or `assets/fonts` directory.
6. In ChatGPT Work/cloud, the exact account asset named `HarmonyOS+Sans.zip`, materialized into the current task and extracted outside the skill.

Run the deterministic resolver before producing any final text-bearing high-fidelity mockup, generated-image prompt with exact typography, presentation visual, prototype preview, or implementation handoff:

```bash
python3 scripts/resolve_harmonyos_fonts.py --profile sc --json
```

Select `sc`, `tc`, `latin`, `latin-italic`, `condensed`, `condensed-italic`, `arabic-ui`, `arabic-text`, or `all` to match the deliverable. A passing result returns absolute file paths and verifies every required SHA-256 checksum. Pass those exact paths to the renderer instead of relying on an unverified family-name lookup.

For a web/cloud task that cannot access the user's Windows asset directory, request the original `HarmonyOS+Sans.zip`, extract it into a task-local temporary directory, and pass that directory to the resolver. Never copy the font binaries into this skill merely to make them globally available.

When the exact account asset is available, use it directly instead of creating a second font-only skill. A personal skill cannot depend on another personal skill as a deterministic callable module. Resolve the account file by exact filename, verify the archive checksum in the manifest, and prepare it with:

```bash
python3 scripts/resolve_harmonyos_fonts.py \
  --profile sc \
  --archive /path/to/HarmonyOS+Sans.zip \
  --extract-to /task/temp/harmonyos-font-assets \
  --json
```

The extraction directory is temporary task data, not part of the personal skill or final deliverable.

## Rendering and fallback rules

- Use `HarmonyOS_Sans_SC.ttf` by default for the user's Simplified Chinese HarmonyOS screens. It contains the Latin and Chinese glyphs needed for mixed UI copy.
- Preserve fp-based role sizes, line height, letter spacing, wrapping, truncation, and large-font behavior from the typography baseline. The font package changes font binaries, not type-role geometry.
- Use the exact verified font for final high-fidelity raster output. Do not silently substitute Microsoft YaHei, Arial, Source Han Sans, Noto Sans, or another system font.
- If the required exact font is unavailable, pause final rendering and request the original font package. A low-fidelity wireframe may use a fallback only when clearly labeled `typography approximate`; never present it as a brand-exact visual.
- Do not convert, subset, rename, edit, optimize, hint, outline, or otherwise modify the supplied font files.
- Record the chosen font file, profile, checksum status, weight, size in fp, and any fallback state in developer handoff.

## License constraints

The supplied `LICENSE-update.txt` permits use, copying, embedding, bundling, and redistribution of **unmodified** HarmonyOS Sans Fonts with software other than font software, subject to its notice and retention conditions. It prohibits modifying the fonts and prohibits redistributing or selling the fonts on a stand-alone basis. Therefore:

- retain `LICENSE-update.txt` with every copied font set;
- include a prominent HarmonyOS Sans usage notice in software that embeds or bundles the fonts;
- do not create or distribute a stand-alone repackaged font ZIP;
- do not create subset or converted font derivatives;
- distribute rendered design outputs normally; the license explicitly permits works created with the fonts.

The license text controls over this summary.

## Acceptance criteria

- The locale-appropriate file resolves from an external asset location.
- The file size and SHA-256 match `harmonyos-sans-font-manifest.json`.
- The renderer uses the resolved absolute font path and correct variable-weight value.
- No synthetic style or silent fallback is used in a final high-fidelity output.
- Text layout still follows the HarmonyOS fp roles and accessibility behavior.
- The font binaries add zero bytes to the HarmonyOS UX Defaults skill package.
- Any copied external font set retains the supplied license and remains unmodified.
