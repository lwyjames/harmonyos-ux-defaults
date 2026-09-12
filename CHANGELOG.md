# Changelog

本文件记录 **HarmonyOS UX Defaults** 的重要变更。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号采用 [Semantic Versioning](https://semver.org/lang/zh-CN/) 约定。除非特别说明，日期使用 `YYYY-MM-DD` 格式。

> 当前仓库尚未创建 GitHub Release 或版本标签。`1.0.0` 是首次完整 GitHub 快照的版本标识；创建正式 Release 时应建立对应的 `v1.0.0` 标签。

## [Unreleased]

### Added

- 新增面向使用者和维护者的中文 `README.md`。
- 新增 `CHANGELOG.md`，建立后续版本变更记录规范。
- 新增微信聊天界面的文字化 UX 参考，记录会话结构、消息气泡、时间分隔、输入区和系统覆盖层行为；原始截图及其中的私人内容不进入仓库。

### Changed

- 明确忽略微信参考截图中的状态栏设计，状态栏继续使用 HarmonyOS 既有系统规范。
- 将浅色界面的底部导航指示条视觉处理推广为跨应用项目默认：应用浅色底面延伸至系统导航区域，指示条使用中性黑约 `8%` 的半透明语义层；深色、彩色、图像及高变化背景使用系统语义反转或自适应处理。

## [1.0.0] - 2026-09-11

首次将完整的 HarmonyOS UX Defaults Skill 发布至 GitHub。

### Added

- 新增主执行规范 `SKILL.md`，定义平台优先级、默认设备、设计工作流、验证要求和原型交付规则。
- 新增 `agents/openai.yaml` Skill 元数据。
- 加入 2026-09-03 冻结的 16 份核心 HarmonyOS 设计文档基线、可检索文本和来源索引。
- 新增 Pura X Max 展开竖屏/横屏、Pura X View 和 Pura 90 Pro Max 的设备机框与官方机框工作流。
- 新增默认桌面、状态栏、导航指示条和系统区域规范。
- 新增 Flash Control Ball/Window（闪控球/闪控窗）系统表面规范。
- 新增 Picture-in-Picture（画中画）行为与适用范围。
- 新增实况窗基础卡片、展开卡片、状态栏胶囊和紧凑外屏形态规范。
- 新增安全与隐私品牌资产使用规则。
- 新增 HarmonyOS Sans 外置字体映射、清单和 SHA-256 校验工作流。
- 新增设备机框合成、导航条几何、展开实况窗几何、字体解析、默认桌面恢复和冻结 PDF 提取脚本。

### Changed

- 将 Pura X Max 展开竖屏设为未指定手机任务的默认设备：
  - `1828 × 2584 px`
  - `665 × 940 vp`
- 统一手机高保真输出的官方机框合成方式：
  - UI 与机框分层渲染。
  - 根据机框 Alpha 通道推导屏幕开口和隐藏出血。
  - 对上、下、左、右四边及四角执行独立接缝验证。
  - 禁止使用手绘圆角矩形或通用设备蒙版替代映射机框。
- 将导航指示条从旧固定像素规则更新为响应式 vp 规则：
  - 可见胶囊高度 `6 vp`。
  - 胶囊底边距可见屏幕底部 `6 vp`。
  - 根据逻辑屏幕宽度 `W` 计算响应式宽度。
  - 独立保留底部 `35% W × 28 vp` 不可见交互区域。
- 将展开手机实况窗更新为响应式几何：
  - `x = 16 vp`
  - `y = 50 vp`
  - `width = W - 32 vp`
  - `height = (W - 32 vp) × 6 / 17`
  - `cornerRadius = 20 vp`
- 将展开实况窗材质更新为模糊下层内容、`48%` 中性深色覆盖层和 `25%` 中性描边。
- 将简体中文及中英混排的默认精确字体映射为经校验的 `HarmonyOS_Sans_SC.ttf`。
- 明确字体二进制必须保留在 Skill 外部，不得静默替换或作为独立字体包重新分发。

### Removed

- 移除已被更正来源取代的固定 `1252 × 84 px` 导航指示条规则、`42 px` 圆角和 `16 px` 固定底部偏移。
- 移除将展开实况窗固定为所有手机通用尺寸的旧规则。
- 移除展开实况窗的旧 `16 vp` 圆角和黑色 `82%` 覆盖层要求。
- 移除展开实况窗内部区域中不具响应性的固定右侧坐标和固定扩展宽度。
- 不在仓库中包含 HarmonyOS Sans 字体二进制文件。

### Fixed

- 修正手机机框合成中上、下、左、右边缘或四角可能出现透明缝隙的问题。
- 修正将导航条可见胶囊与 `28 vp` 交互热区混为同一图形的问题。
- 修正把 Pura X View 的 `408 × 144 vp` 展开实况窗结果当作所有手机固定尺寸的问题。
- 修正 Pura X Max 展开横屏机框方向：官方竖屏机框需顺时针旋转 90°，前摄位于右上角。
- 强化状态栏胶囊与展开实况窗卡片的互斥、碰撞和系统所有权验证。

### Source milestones included in 1.0.0

以下日期表示规范来源整合时间，不代表曾发布独立版本：

- **2026-09-03**：建立 16 份核心 HarmonyOS 设计文档冻结基线。
- **2026-09-07**：加入 Flash Control Ball/Window 补充规范。
- **2026-09-08**：加入 Picture-in-Picture 补充规范。
- **2026-09-09**：加入安全与隐私品牌、设备机框、宽折叠屏、默认桌面和初始光栅系统栏补充规范。
- **2026-09-10**：加入实况窗 Sketch 几何来源，并用更正截图替换旧导航条固定像素规则。
- **2026-09-11**：加入 Pura X View 展开实况窗完整画布参考和 HarmonyOS Sans 字体资产规范；发布首次完整 GitHub 快照。

[Unreleased]: https://github.com/lwyjames/harmonyos-ux-defaults/compare/acb2bc573b1a50afa3b5166f8af9d33ad55a3fe1...HEAD
[1.0.0]: https://github.com/lwyjames/harmonyos-ux-defaults/commit/acb2bc573b1a50afa3b5166f8af9d33ad55a3fe1
