# Spec-Craft 戦略ロードマップ

## コア・フィロソフィー
Spec-Craft は**仕様駆動開発 (SDD)** に基づいています。
- **戦略 (Obsidian)**: 「何を」「なぜ」作るかを定義します。プロジェクトの「魂」です。
- **戦術 (spec-kit)**: 「どのように」作るかを定義します。反復的な実装サイクルを担当します。

## 現在の到達点: v0.1.2 達成
Spec-Craft の基盤は完成しています。
- 多ドメイン生成: 2D (SVG), 3D (Blender/盆景), CAD (JSCAD), BIM (Bonsai)。
- 視覚的フィードバック: AI が SVG プロジェクションを介して成果物を確認可能。
- 隔離された編集環境: AI 専用の Emacs サンドボックス（LSP/Lint 対応）。
- 透明性: ユーザーとの対話を重視した「提案と確認」型ワークフロー。

## Antigravity CLI およびマルチエージェント環境への移行に関する注記
このプロジェクトは、新しい AI エージェント環境（Antigravity CLI）へ移行するとともに、マルチエージェント（Antigravity, Gemini CLI, Claude Code, Aiderなど）によるSDDワークフローをサポートします。
**AI エージェントへの指示**:
1. `specs/` ディレクトリにある戦術的な歴史（Phase 001-013）をすべて読みなさい。
2. 公式マニュアル [https://spec-craft.readthedocs.io/](https://spec-craft.readthedocs.io/) を確認しなさい。
3. `spec-craft check-env` を実行してローカル環境を検証しなさい。
4. 常に SDD ワークフロー（仕様 -> 計画 -> タスク -> 実装）を遵守しなさい。
5. Aiderやローカル環境での作業時は、Markdown形式のスキルの直接読み込みや、`spec-kit-mcp` 統合のオプションを活用しなさい。

## 将来の展望
- 建築解析ツールとのより深い統合。
- 生成音楽・ビデオドメインの拡張サポート。
- Obsidian キャンバスと戦術タスクのリアルタイム同期。
