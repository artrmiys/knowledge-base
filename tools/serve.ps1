$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Url = "http://127.0.0.1:8000/"
$Python = Join-Path $Root ".venv\Scripts\python.exe"
$ReadyMarker = Join-Path $Root ".venv\.mkdocs-ready"

function Test-Port8000 {
    $listener = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue
    return $null -ne $listener
}

if (Test-Port8000) {
    Start-Process $Url
    Write-Host "Knowledge Base preview is already running: $Url"
    exit 0
}

if (-not (Test-Path $Python)) {
    Write-Host "Creating local .venv..."
    py -m venv (Join-Path $Root ".venv")
}

if (-not (Test-Path $ReadyMarker)) {
    Write-Host "Installing MkDocs dependencies..."
    & $Python -m pip install -U mkdocs mkdocs-material mkdocs-material-extensions
    New-Item -ItemType File -Path $ReadyMarker -Force | Out-Null
}

Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "http://127.0.0.1:8000/"
} | Out-Null

Write-Host "Serving Knowledge Base at $Url"
Write-Host "Keep this window open while viewing. Press Ctrl+C to stop."
Set-Location $Root
& $Python -m mkdocs serve -a 127.0.0.1:8000
