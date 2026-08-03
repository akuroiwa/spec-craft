# Spec-Craft 戦略ロードマップ

## コア・フィロソフィー
Spec-Craft は**仕様駆動開発 (SDD)** に基づいています。
- **戦略 (Obsidian)**: 「何を」「なぜ」作るかを定義します。プロジェクトの「魂」です。
- **戦術 (spec-kit)**: 「どのように」作るかを定義します。反復的な実装サイクルを担当します。

## 現在の到達点: v0.1.5 達成

Spec-Craft の基盤は安定しており、MCP プロンプト層が大幅に改善されました。

### v0.1.2 以降の新機能
- **Obsidian CLI 統合** (v0.1.5): `obsidian/` へのファイル書き込み時に `obsidian` CLI の存在を確認し、正しい YAML フロントマターを生成します。Obsidian が使用不可または拒否された場合は、手動フロントマターを付加したプレーン Markdown にフォールバックします。
- **プロンプト明確化** (v0.1.4): `BOOT_TACTICAL_KNOWLEDGE` を全面的に書き直し、spec-kit スラッシュコマンドをシェルコマンドと誤認する問題、SDD フェーズ実行前の TOML/SKILL.md 必須読み込み、RST CJK インラインマークアップ規則を追加しました。
- **マルチエージェント検出** (v0.1.3): `detector.py` が Antigravity CLI を自動識別します。

### 確立された機能 (v0.1.2 時点)
- 多ドメイン生成: 2D (SVG), 3D (Blender/盆景), CAD (JSCAD), BIM (Bonsai)。
- 視覚的フィードバック: AI が SVG プロジェクションを介して成果物を確認可能。
- 隔離された編集環境: AI 専用の Emacs サンドボックス（LSP/Lint 対応）。
- 透明性: ユーザーとの対話を重視した「提案と確認」型ワークフロー。

## 対処すべき既知の問題 (Phase 014)

詳細なアーキテクチャレビュー（2026-07-30）に基づく改善項目：

1. **`EmacsManager.edit_file()` が常に保存する**: `save-buffer` が強制実行されるため、AI が Flymake の診断結果や xref の定義情報を読み取るだけの参照専用操作でもファイルを上書きしてしまいます。読み取り専用の検査メソッド（`eval_in_buffer`）が必要です。
2. **`init.el` 起動時のレースコンディション**: `emacs --daemon` 後の 1 秒スリープは、`package-install-selected-packages` がネットワークからパッケージを取得する場合には不十分です。`start_daemon()` にヘルスチェックのポーリングループが必要です。
3. **`init.el` に `global-auto-revert-mode` が未設定**: AI がファイルを直接編集し Emacs が同じバッファを開いている場合、インメモリバッファが古くなり、次の `save-buffer` で AI の変更を上書きしてしまいます。`(global-auto-revert-mode 1)` の追加が必要です。
4. **`parser.py` のコードブロック内見出し誤検知**: MULTILINE 正規表現 `^#{1,6}` がフェンスコードブロック内の `# コメント` 行に一致し、セクションが意図せず分割されます。コードフェンス状態トラッカーまたは AST ベースのパーサーへの移行が必要です。

## Antigravity CLI およびマルチエージェント環境への移行に関する注記
このプロジェクトはマルチエージェント SDD ワークフロー（Antigravity CLI、Gemini CLI、Claude Code、Aider）をサポートします。

**AI エージェントへの指示**:
1. `specs/` ディレクトリにある戦術的な歴史（Phase 001-014）をすべて読みなさい。
2. 公式マニュアル [https://spec-craft.readthedocs.io/](https://spec-craft.readthedocs.io/) を確認しなさい。
3. `spec-craft check-env` を実行してローカル環境を検証しなさい。
4. 常に SDD ワークフロー（仕様 → 計画 → タスク → 実装）を遵守しなさい。
5. `obsidian/` への書き込み前に `obsidian help` を実行して Obsidian CLI の有無を確認しなさい（`BOOT_TACTICAL_KNOWLEDGE` セクション 6 参照）。

## 将来の展望
- 建築解析ツール（Bonsai/BlenderBIM）とのより深い統合。
- `obsidian.yaml` コマンドマッピング: `trigger_bonsai_build` 用の `obsidian-bonsai` エントリを追加。
- 生成音楽・ビデオドメインの拡張サポート。
- Obsidian キャンバスと戦術タスクのリアルタイム同期。
- SVG ドライバー: レイアウト崩れなしの `<tspan>` ネストテキスト置換対応。
