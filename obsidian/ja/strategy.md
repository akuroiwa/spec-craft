# Spec-Craft 戦略ロードマップ

## コア・フィロソフィー
Spec-Craft は**仕様駆動開発 (SDD)** に基づいています。
- **戦略 (Obsidian)**: 「何を」「なぜ」作るかを定義します。プロジェクトの「魂」です。
- **戦術 (spec-kit)**: 「どのように」作るかを定義します。反復的な実装サイクルを担当します。

## 現在の到達点: v0.1.6 達成

Spec-Craft の基盤は安定しており、マルチ環境での動作が検証されています。

### v0.1.2 以降の新機能
- **Emacs 検査機能とパーサー堅牢化** (v0.1.6 / Phase 014): ファイルを上書きせずに安全に LSP/Flymake 診断を取得する `eval_in_buffer()` の追加、デーモン起動時のポーリングループ化、`init.el` への `global-auto-revert-mode` 追加、および `StoryboardParser` のコードフェンス内見出し誤検知の修正。
- **Obsidian CLI 統合** (v0.1.5): `obsidian/` へのファイル書き込み時に `obsidian` CLI の存在を確認し、正しい YAML フロントマターを生成。未導入時はプレーン Markdown へフォールバック。
- **プロンプト明確化** (v0.1.4): `BOOT_TACTICAL_KNOWLEDGE` を再設計し、spec-kit スラッシュコマンドとシェルコマンドの境界、CJK マークアップ規則を明確化。
- **マルチエージェント検出** (v0.1.3): `detector.py` による Antigravity CLI や各種 AI エージェントの自動検出。

### 確立された機能
- 多ドメイン生成: 2D (SVG), 3D (Blender/盆景), CAD (JSCAD), BIM (Bonsai)。
- 視覚的フィードバック: AI が SVG プロジェクションを介して成果物を確認可能。
- 隔離された編集環境: AI 専用の Emacs サンドボックス（LSP/Lint 対応）。
- 透明性: ユーザーとの対話を重視した「提案と確認」型ワークフロー。

## Phase 015: インタラクティブな Colab Notebook とチュートリアル統合

ハンズオン検証、YouTube デモ動画制作、スムーズなユーザー導入を実現するため：
1. **Google Colab ノートブック (`docs/notebooks/spec_craft_quickstart.ipynb`)**:
   - ワンクリック環境構築: Ollama バックグラウンド起動 + 軽量 QAT モデル切り替え（`gemma-2-2b-it` / `qwen2.5` / `gemma-4-qat` 等）。
   - CLI ツール群の導入: `uv`、`sigoden/aichat`、`spec-craft`。
   - エンドツーエンドの SDD ワークフロー実演:
     - Step 1: `aichat` による Obsidian 戦略仕様の生成。
     - Step 2: `spec-craft` による戦略仕様の解析とプレビュー。
     - Step 3: `spec-kit` 自動ワークフローによるコードおよびテストコードの生成。
     - Step 4: Colab 上でのテスト実行と動作確認。
2. **Read the Docs & Sphinx 連携**:
   - Sphinx ビルダーに `myst-nb` を統合（`docs/source/conf.py` および `docs/requirements.txt`）、セル再実行なしのキャッシュ表示（`nb_execution_mode = "off"`）を設定。
   - `[Open in Colab]` バッジを設置し、クラウド上で即座に追試可能な導線を整備。

## Antigravity CLI およびマルチエージェント環境への移行に関する注記
このプロジェクトはマルチエージェント SDD ワークフロー（Antigravity CLI、Gemini CLI、Claude Code、Aider）をサポートします。

**AI エージェントへの指示**:
1. `specs/` ディレクトリにある戦術的な歴史（Phase 001-014）をすべて読みなさい。
2. 公式マニュアル [https://spec-craft.readthedocs.io/](https://spec-craft.readthedocs.io/) を確認しなさい。
3. `spec-craft check-env` を実行してローカル環境を検証しなさい。
4. 常に SDD ワークフロー（仕様 → 計画 → タスク → 実装）を遵守しなさい。
5. `obsidian/` への書き込み前に `obsidian help` を実行して Obsidian CLI の有無を確認しなさい。

## 将来の展望
- 建築解析ツール（Bonsai/BlenderBIM）とのより深い統合。
- `obsidian.yaml` コマンドマッピング: `trigger_bonsai_build` 用の `obsidian-bonsai` エントリを追加。
- 生成音楽・ビデオドメインの拡張サポート。
- Obsidian キャンバスと戦術タスクのリアルタイム同期。
- SVG ドライバー: レイアウト崩れなしの `<tspan>` ネストテキスト置換対応。
