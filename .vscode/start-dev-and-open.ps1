$ErrorActionPreference = "Stop"
$siteDir = Join-Path $PSScriptRoot "..\site"
$port = 3000

# 1) Encerrar tudo que ocupa a porta do servidor
$pids = @()
try {
    $pids += (Get-NetTCPConnection -LocalPort $port -ErrorAction Stop | Select-Object -ExpandProperty OwningProcess)
} catch {
    $pids += (netstat -ano -p TCP | Select-String ":$port\s" | ForEach-Object { ($_ -split '\s+')[-1] })
}

$pids | Where-Object { $_ -and $_ -ne 0 } | Sort-Object -Unique | ForEach-Object {
    $targetPid = [int]$_
    try {
        Stop-Process -Id $targetPid -Force -ErrorAction Stop
        Write-Host "Processo $targetPid na porta $port encerrado."
    } catch {
        if (Get-Process -Id $targetPid -ErrorAction SilentlyContinue) {
            Write-Warning "Não foi possível encerrar o processo $targetPid na porta ${port}: $($_.Exception.Message)"
        }
    }
}

# 2) Encerrar todos os processos Python
Get-Process -Name python, pythonw, py -ErrorAction SilentlyContinue | ForEach-Object {
    $targetPid = $_.Id
    if (-not (Get-Process -Id $targetPid -ErrorAction SilentlyContinue)) {
        return
    }
    try {
        Stop-Process -Id $targetPid -Force -ErrorAction Stop
        Write-Host "Processo Python $targetPid encerrado."
    } catch {
        if (Get-Process -Id $targetPid -ErrorAction SilentlyContinue) {
            Write-Warning "Não foi possível encerrar o processo Python ${targetPid}: $($_.Exception.Message)"
        }
    }
}

# 3) Remover o lock do vinext, que impede um novo servidor de subir
$lockFile = Join-Path $siteDir ".vinext\dev\lock.json"
if (Test-Path -LiteralPath $lockFile) {
    try {
        $lockPid = (Get-Content -LiteralPath $lockFile -Raw | ConvertFrom-Json).pid
        $lockProc = Get-Process -Id $lockPid -ErrorAction SilentlyContinue
        if ($lockProc -and $lockProc.ProcessName -eq "node") {
            Stop-Process -Id $lockPid -Force -ErrorAction SilentlyContinue
            Write-Host "Servidor anterior (PID $lockPid) encerrado."
        }
    } catch {
        Write-Warning "Lock do vinext ilegível; será removido mesmo assim."
    }
    Remove-Item -LiteralPath $lockFile -Force -ErrorAction SilentlyContinue
    Write-Host "Lock do vinext removido."
}

# 4) Iniciar o servidor de desenvolvimento
Start-Process -FilePath "powershell.exe" -ArgumentList @("-NoExit", "-Command", "Set-Location -LiteralPath '$siteDir'; npm run dev") -WindowStyle Minimized

$ready = $false
for ($i = 0; $i -lt 30; $i++) {
    try {
        Invoke-WebRequest -Uri "http://localhost:$port" -UseBasicParsing -TimeoutSec 1 | Out-Null
        $ready = $true
        break
    } catch {
        Start-Sleep -Seconds 1
    }
}

if (-not $ready) {
    Write-Warning "O servidor não respondeu em 30s; abrindo o navegador mesmo assim."
}

# 5) Abrir a página inicial
Start-Process "http://localhost:$port/"
