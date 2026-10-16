# Spec-Craft 戦略ロードマップ

## コア・フィロソフィー: 戦略的ビジョンと戦術的収束
Spec-Craft は**仕様駆動開発 (SDD)** に基づいています。
- **戦略 (Obsidian)**: 「何を」「なぜ」作るかを定義します。**Spec-Kit の Constitution（開発原則）プロセスを拡張・詳細化**し、実装タスク着手前にプロジェクトのアーキテクチャ方針、ドメインモデル、製品ロードマップを明文化します。
- **戦術 (spec-kit)**: 「どのように」作るかを定義します。**Shorter Path (`specify` → `plan` → `tasks` → `implement` → `converge`)** を用いて反復的な実装サイクルを回し、仕様の意図と実装の乖離を継続的に収束（Convergence）させます。

## 現在の到達点: v0.1.7 達成

Spec-Craft の基盤は安定しており、マルチ環境での動作が検証されています。

### v0.1.2 以降の新機能
- **Spec-Kit Convergence と Colab 連携** (v0.1.7 / Phase 015): 最新の Spec-Kit `/speckit-converge` コマンドおよび `.agents/skills/` を統合。Shorter Path (`specify` → `plan` → `tasks` → `implement` → `converge`) を確立。Quickstart ノートブックおよび OpenCode ノートブックを整備し、運用境界と制約事項を明記。
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
1. **Google Colab ノートブックの単一ソース管理 (`docs/source/notebooks/`)**:
   - **配置規約**: Sphinx (`docs/source/`) および `myst-nb` と連携するため、ノートブックの実体は `docs/source/notebooks/` 配下にのみ配置（単一の信頼できる情報源とする。`docs/notebooks/` 等の重複配置は行わない）。
   - **A. Quickstart ノートブック (`docs/source/notebooks/spec_craft_quickstart.ipynb`)**:
     - 完全自動バッチ実行: Rust/Cargo 経由の `sigoden/aichat` を CLI シェルコマンドとして非対話呼び出し + Ollama 公式 Gemma 4 QAT + `specify-cli` (`spec-kit`) + `spec-craft`。
     - エンドツーエンドの SDD 自動パイプライン (Obsidian 戦略仕様 → StoryboardParser → コード・テスト生成 → pytest 検証)。
   - **B. OpenCode MCP ノートブック (`docs/source/notebooks/spec_craft_opencode.ipynb`)**:
     - 対話型 AI エージェント開発: `opencode` (AI Coding Agent) + `spec-craft serve` (FastMCP サーバー) + `specify-cli` (OpenCode integration)。
     - `colab-xterm` による対話型 Web ターミナル起動により、ユーザーが実際に AI エージェントへ開発を依頼するハンズオンおよび YouTube デモ動画撮影環境を提供。
2. **Read the Docs & Sphinx 連携**:
   - Sphinx ビルダーに `myst-nb` を統合（`docs/source/conf.py` および `docs/requirements.txt`）、セル再実行なしのキャッシュ表示（`nb_execution_mode = "off"`）を設定。
   - 各ノートブックに `[Open in Colab]` バッジを設置し、クラウド上で即座に追試可能な導線を整備。

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
