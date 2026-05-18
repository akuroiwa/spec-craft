;; Spec-Craft AI Agent Emacs Configuration
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; Install and configure essential packages for AI coding
(setq package-selected-packages '(eglot python-mode))
(unless package-archive-contents (package-refresh-contents))
(package-install-selected-packages)

;; Use Tree-sitter for Python if available
(when (fboundp 'python-ts-mode)
  (add-to-list 'major-mode-remap-alist '(python-mode . python-ts-mode)))

;; Enable Eglot and Flymake automatically for Python
(add-hook 'python-mode-hook 'eglot-ensure)
(add-hook 'python-ts-mode-hook 'eglot-ensure)
(add-hook 'prog-mode-hook 'flymake-mode)

;; Disable backups and lockfiles to keep the sandbox clean
(setq make-backup-files nil)
(setq create-lockfiles nil)

;; Start server to allow emacsclient connection
(require 'server)
(unless (server-running-p)
  (server-start))

(message "Spec-Craft AI Emacs Sandbox Initialized.")
