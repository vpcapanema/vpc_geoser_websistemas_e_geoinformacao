param([switch]$DryRun, [switch]$CheckOnly)
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$scriptPath = Join-Path $root 'site/scripts/publish-production.ps1'
if (-not (Test-Path -LiteralPath $scriptPath)) {
    Write-Host '[ERRO] Checkout site/ ausente ou sem scripts de publicacao.' -ForegroundColor Red
    exit 1
}
Write-Host '[VPC] O repositorio principal publica a aplicacao site/ e sincroniza sua referencia Git.' -ForegroundColor Yellow
& $scriptPath -DryRun:$DryRun -CheckOnly:$CheckOnly -ParentRepo $root
exit $LASTEXITCODE
