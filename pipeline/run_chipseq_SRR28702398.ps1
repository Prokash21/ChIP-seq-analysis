# Install Miniconda (if needed), create chipseq env with snakemake, run pipeline for SRR28702398
# Usage: Open PowerShell, cd to the repo root and run: .\pipeline\run_chipseq_SRR28702398.ps1
# Notes: Recommended to run inside WSL or Git Bash for best compatibility because some pipeline commands expect a Unix shell.

$ErrorActionPreference = 'Stop'

function Has-Conda {
    try {
        conda --version > $null 2>&1
        return $true
    } catch {
        return $false
    }
}

# 1) Install Miniconda if missing
if (-not (Has-Conda)) {
    Write-Host "Conda not found. Downloading Miniconda installer..."
    $installer = "$env:TEMP\\Miniconda3-latest-Windows-x86_64.exe"
    Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -OutFile $installer
    Write-Host "Running Miniconda installer (silent)..."
    Start-Process -FilePath $installer -ArgumentList "/InstallationType=JustMe","/AddToPath=1","/RegisterPython=0","/S","/D=$env:USERPROFILE\\Miniconda3" -Wait
    Remove-Item $installer -Force
    # Update PATH for this session
    $env:Path = $env:Path + ";" + "$env:USERPROFILE\\Miniconda3\\Scripts" + ";" + "$env:USERPROFILE\\Miniconda3"
    Write-Host "Miniconda installed (added to PATH for this session)."
} else {
    Write-Host "Conda already available."
}

# 2) Create or update chipseq conda environment with snakemake
Write-Host "Creating or updating Conda environment 'chipseq' with snakemake..."
conda create -n chipseq snakemake -c bioconda -c conda-forge -y

# 3) Identify repository root and SRR list
$cwd = Get-Location
# If run from repo root, pipeline\SRR_Acc_List.txt should exist
if (-not (Test-Path "$cwd\pipeline\SRR_Acc_List.txt")) {
    Write-Host "Can't find pipeline\\SRR_Acc_List.txt in current directory ($cwd). Please run this script from the repo root.";
    exit 1
}

$srList = Join-Path $cwd "pipeline\\SRR_Acc_List.txt"
$backup = "$srList.bak_$(Get-Date -Format yyyyMMddHHmmss)"
Copy-Item $srList $backup
Write-Host "Backed up original SRR list to $backup"

# Replace SRR list with only SRR28702398
"SRR28702398" | Out-File -FilePath $srList -Encoding ASCII
Write-Host "Wrote single SRR entry to $srList"

# 4) Run snakemake from the snakemake_ChIPseq_pipeline directory using conda run
$pipelineDir = Join-Path $cwd "snakemake_ChIPseq_pipeline"
Set-Location $pipelineDir

Write-Host "Performing dry-run (no actions) to verify workflow..."
conda run -n chipseq snakemake -n --use-conda 2>&1 | Tee-Object -Variable dryrunOut

Write-Host "Starting pipeline run (this may take a long time, Conda envs will be created)..."
$logFile = Join-Path ".." ("snakemake_run_{0}.log" -f (Get-Date -Format yyyyMMddHHmmss))
conda run -n chipseq snakemake -j 4 --use-conda | Tee-Object -FilePath $logFile

Write-Host "Snakemake finished (check the log at $logFile). Restoring original SRR list..."
# Restore backup
Copy-Item $backup $srList -Force
Write-Host "Original SRR list restored from $backup"

Write-Host "Pipeline run complete. Look in the following directories for outputs:"
Write-Host "  - 01seq/, 02fqc/, 03seqClean/, 04aln/, 05peak/, images/"

Write-Host "If you run into errors, copy the log file ($logFile) and I can help debug."
