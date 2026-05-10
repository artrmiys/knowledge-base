# Manual GitHub Pages deploy helper.
# Use when Actions are paused (e.g. after long repo inactivity) and you need
# to push the latest content to gh-pages right now.
#
# Usage:
#   .\tools\deploy.ps1
#
# Steps:
#   1. mkdocs build --strict (catches broken links / missing files).
#   2. mkdocs gh-deploy --force --clean --remote-branch gh-pages.
# After it finishes, the live site at https://artrmiys.github.io/knowledge-base/
# updates within ~30-60 seconds.

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$python = Join-Path $repoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $python)) {
    Write-Host "Python venv not found at $python. See CLAUDE.md section 2 for setup." -ForegroundColor Red
    exit 1
}

# MkDocs / Material print to stderr; PowerShell wraps that as NativeCommandError
# even when the command succeeded. Trust exit code only.
$ErrorActionPreference = 'Continue'

Write-Host "==> Building docs (strict mode)" -ForegroundColor Cyan
& $python -m mkdocs build --strict
if ($LASTEXITCODE -ne 0) {
    Write-Host "mkdocs build --strict failed (exit $LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "==> Deploying to gh-pages" -ForegroundColor Cyan
& $python -m mkdocs gh-deploy --force --clean --remote-branch gh-pages
if ($LASTEXITCODE -ne 0) {
    Write-Host "mkdocs gh-deploy failed (exit $LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "==> Done. Live site updates in ~30-60 sec:" -ForegroundColor Green
Write-Host "    https://artrmiys.github.io/knowledge-base/"
