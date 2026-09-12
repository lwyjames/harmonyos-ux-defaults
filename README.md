# HarmonyOS UX Defaults

> 面向 AI Agent、UX 设计与原型工作流的 HarmonyOS 默认设计规范 Skill。

**HarmonyOS UX Defaults** 将用户提供并持续校正的 HarmonyOS 设计资料整理为可执行的 Agent 规则，用于 UX 需求、流程、线框图、高保真界面、图像提示词、可点击原型、服务卡片、通知、实况窗、画中画、闪控球/闪控窗和多设备体验。

仓库的核心入口是 [`SKILL.md`](SKILL.md)。它是 Agent 的执行规范；本 README 用于帮助人类理解、安装和维护该 Skill。

> [!IMPORTANT]
> 本项目是个人设计与开发工作流，不是华为官方仓库，也不代表华为官方发布、认证或背书。

## 核心能力

- 默认采用 HarmonyOS NEXT 的视觉与交互语言。
- 根据目标设备、横竖屏、折叠状态和窗口模式应用响应式布局。
- 支持 Pura X Max 展开竖屏/横屏、Pura X View 和 Pura 90 Pro Max 等已有设备机框的设备。
- 使用指定设备的设备机框、桌面、状态栏和导航指示条规则。
- 覆盖实况窗、状态栏胶囊、Picture-in-Picture、Flash Control Ball/Window 等系统表面。
- 对安全与隐私界面应用对应的品牌资产和校验约束。
- 使用外置 HarmonyOS Sans 字体资产，并在高保真输出前进行文件和校验和验证。
- 提供导航条、实况窗、字体和设备机框的确定性计算或验证脚本。
- 提供基于文字重建的微信聊天界面参考，并将底部导航指示条的浅色半透明处理推广为跨应用默认规则。

## 适用场景

本 Skill 适用于：

- HarmonyOS 手机 UX 需求与交互流程
- 线框图和高保真界面
- 产品概念图、演示图及关键帧
- 可点击原型与前端实现交付
- 图片或视频生成提示词
- 已有设计的 HarmonyOS 规范审查
- 折叠屏、外屏、横屏、分屏和浮窗适配

如果任务没有指定其他平台，Skill 会把 HarmonyOS 作为默认移动平台。若用户明确指定 iOS、Material Design、Windows 或 Web，应优先遵循目标平台规范。

## 使用方法

在支持个人 Skill 的 ChatGPT 或 Agent 环境中选择或引用：

```text
@HarmonyOS UX Defaults
请为 Pura X Max 展开竖屏设计……
```

调用名称在不同宿主中可能显示为 `HarmonyOS UX Defaults`，Skill 内部名称为：

```text
apply-harmonyos-ux-defaults
```

未明确指定手机时，当前默认设备为 Pura X Max 展开竖屏：

```text
1828 × 2584 px
665 × 940 vp
```

## 安装

克隆仓库：

```bash
git clone https://github.com/lwyjames/harmonyos-ux-defaults.git
```

将克隆后的目录注册或复制到所用 Agent 环境的个人 Skill 目录，并确保 `SKILL.md` 位于 Skill 根目录。不同 ChatGPT、Codex 或第三方 Agent 宿主的安装入口可能不同，请以对应宿主当前的 Skill 安装机制为准。

完整目录必须一并保留；不要只复制 `SKILL.md`，否则参考文档、设备资产和验证脚本将不可用。

## 仓库结构

```text
harmonyos-ux-defaults/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
├── references/
│   ├── quick-reference.md
│   ├── wechat-chat-interface.md
│   ├── device-preview-frames.md
│   ├── system-chrome-verification.md
│   ├── navigation-bar-geometry.md
│   ├── live-view-sketch-spec.md
│   ├── expanded-live-view-card.md
│   ├── harmonyos-sans-font-assets.md
│   └── source-index.md
└── scripts/
    ├── composite_validate_bezel.py
    ├── expanded_live_view_geometry.py
    ├── navigation_bar_geometry.py
    ├── resolve_harmonyos_fonts.py
    ├── materialize_home_screen.py
    └── extract_frozen_pdf.py
```

- `SKILL.md`：Agent 的主执行规则和验收要求。
- `agents/`：宿主所需的 Skill 元数据。
- `assets/`：设备机框、系统界面参考及其他工作流资产。
- `references/`：详细设计规范、来源索引和快速参考。
- `scripts/`：几何计算、字体解析、PDF 恢复和机框合成验证工具。

## 关键设计约束

### 设备机框

- 对应的官方设备机框 PNG 是屏幕开口、边角曲率、相机位置和透明度的几何依据。
- UI 与机框必须分层渲染，机框作为未经修改的最终顶层。
- 四边、四角以及直边与圆角过渡区域均需通过像素级接缝检查。
- 不允许使用手绘圆角矩形或通用设备蒙版替代对应设备机框。

### 系统导航指示条

当导航条存在时：

- 可见胶囊高度为 `6 vp`。
- 胶囊底边距可见屏幕底部 `6 vp`。
- 宽度根据当前逻辑屏幕宽度响应式计算。
- 独立的不可见交互区域为 `35% W × 28 vp`。
- 不得把交互热区渲染成可见的大型胶囊。
- 普通浅色应用界面中，应用底部浅色表面应延伸到系统导航区域；导航指示条使用中性黑约 `8%` 的半透明语义层。参考截图中的观测合成为约 `#F6F6F6` 底面与 `#E3E3E3` 指示条。
- 深色、彩色、图像或高变化背景不得机械复用 `8%` 黑色；应使用系统语义反转或自适应处理，并验证对比度。

完整规则见 [`references/navigation-bar-geometry.md`](references/navigation-bar-geometry.md)。

### 微信聊天界面

微信一对一聊天的应用层参考见 [`references/wechat-chat-interface.md`](references/wechat-chat-interface.md)。该参考以文字和近似颜色记录界面结构，不包含原始截图，也不得复用截图中的联系人、头像、消息、票务信息或贴纸。截图状态栏不属于该参考范围，仍由 HarmonyOS 系统栏规范控制。

聊天界面应保留左右消息流、头像与气泡关系、居中时间分隔、固定底部输入区，以及系统覆盖层出现时不重排聊天内容的行为。

### 展开实况窗

对于逻辑宽度为 `W` 的手机画布，展开实况窗使用：

```text
x = 16 vp
y = 50 vp
width = W - 32 vp
height = (W - 32 vp) × 6 / 17
cornerRadius = 20 vp
```

材质包含模糊的下层内容、`48%` 中性深色覆盖层和 `25%` 中性描边。逻辑几何应先完整计算，再转换为目标光栅并仅舍入一次。

完整规则见 [`references/expanded-live-view-card.md`](references/expanded-live-view-card.md)。

## HarmonyOS Sans 字体

字体二进制文件不包含在本仓库中，也不应作为独立字体包从本仓库再分发。

需要品牌精确的文字渲染时，应单独提供经过授权、未经修改的原始 `HarmonyOS+Sans.zip` 或配置外置字体目录，并通过以下脚本解析和校验：

```bash
python3 scripts/resolve_harmonyos_fonts.py --help
```

简体中文及中英混排默认使用经校验的 `HarmonyOS_Sans_SC.ttf`。当字体缺失或校验失败时，高保真交付不得静默替换为其他字体后声称具备品牌精确性。

详细规则见 [`references/harmonyos-sans-font-assets.md`](references/harmonyos-sans-font-assets.md)。

## 验证工具

查看各脚本参数：

```bash
python3 scripts/navigation_bar_geometry.py --help
python3 scripts/expanded_live_view_geometry.py --help
python3 scripts/composite_validate_bezel.py --help
python3 scripts/resolve_harmonyos_fonts.py --help
```

提交规范更新前应至少确认：

- `SKILL.md` 与引用文件之间不存在失效链接。
- 新规则没有与仍然有效的旧规则冲突。
- vp/fp 逻辑值在转换为像素之前完成计算。
- 设备机框、状态栏和导航条没有被意外改变。
- 外置字体和受控资产通过完整性校验。
- 示例值没有被错误地当作所有设备的固定值。

## 来源与维护原则

本仓库将用户提供的冻结基线和后续补充资料分开管理。后续来源仅在其明确范围内覆盖旧规则；不会因为出现新资料而静默替换无关规范。

详细来源、优先级和适用范围见：

- [`references/source-index.md`](references/source-index.md)
- [`references/quick-reference.md`](references/quick-reference.md)
- [`SKILL.md`](SKILL.md)

## 许可与第三方资产

仓库中的文字、脚本、字体、设备机框、品牌图形、截图和源设计资料可能分别适用不同许可条件。

- 不要假定所有文件都采用同一许可。
- 在公开复制、修改、发布或商业使用任何第三方资产前，应确认对应权利人的授权范围。
- 未包含的字体文件不得通过本仓库另行分发。
- 华为、HarmonyOS、Pura 及相关名称和标识属于其各自权利人。

如果仓库根目录没有单独的 `LICENSE` 文件，则不应推定获得了对整个仓库进行复制、修改或再分发的许可。

## 贡献

修改规范时，请保持来源可追溯、适用范围明确，并同时更新相关快速参考、验证规则、示例和脚本。任何精确尺寸或行为要求都应能够回溯到已确认的来源；无法验证的内容应标记为项目建议，而不是 HarmonyOS 强制规范。
