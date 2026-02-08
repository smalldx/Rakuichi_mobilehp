$ErrorActionPreference = "Stop"

Write-Host "--- Rakuichi HP Generator (PowerShell) ---"

$baseDir = Get-Location
$srcDir = Join-Path $baseDir "src"
$sectionsDir = Join-Path $srcDir "sections"
$outputPath = Join-Path $baseDir "index.html"

# 1. Load Base Template
$basePath = Join-Path $srcDir "base.html"
if (-not (Test-Path $basePath)) {
    Write-Error "Base template not found at $basePath"
}
$baseHtml = Get-Content $basePath -Raw -Encoding utf8
Write-Host "Loaded base template: $(Split-Path $basePath -Leaf)"

# 2. Load and Concatenate Sections
$sectionsHtml = ""
$sectionFiles = Get-ChildItem $sectionsDir -Filter "*.html" | Sort-Object Name

if ($sectionFiles.Count -eq 0) {
    Write-Warning "No section files found in $sectionsDir"
}

foreach ($file in $sectionFiles) {
    Write-Host "Processing section: $($file.Name)"
    $content = Get-Content $file.FullName -Raw -Encoding utf8
    $sectionsHtml += $content + "`n"
}

# 3. Inject Content
$finalHtml = $baseHtml.Replace("{{content}}", $sectionsHtml)

# 4. Write Output
$finalHtml | Set-Content $outputPath -Encoding utf8

Write-Host "✓ Generated: $outputPath"
Write-Host "Done! The website has been rebuilt."
