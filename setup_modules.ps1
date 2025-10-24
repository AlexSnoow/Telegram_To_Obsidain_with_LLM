# Путь к корню проекта (относительно текущей директории)
$projectRoot = "C:\Users\user\Documents\ProgramProjects\Telegram_To_Obsidain_with_LLM"

# Папки модулей
$modules = @("telegram_input", "modify_llm", "youtube_info")

# Убедимся, что папка src существует
$srcPath = Join-Path $projectRoot "src"
if (-not (Test-Path $srcPath)) {
    New-Item -ItemType Directory -Path $srcPath | Out-Null
    Write-Host "Создана папка src" -ForegroundColor Green
}

# Создаём каждую папку модуля и __init__.py внутри
foreach ($module in $modules) {
    $modulePath = Join-Path $srcPath $module
    if (-not (Test-Path $modulePath)) {
        New-Item -ItemType Directory -Path $modulePath | Out-Null
        Write-Host "Создана папка $module" -ForegroundColor Cyan
    }

    $initFile = Join-Path $modulePath "__init__.py"
    if (-not (Test-Path $initFile)) {
        New-Item -ItemType File -Path $initFile | Out-Null
        Write-Host "Создан файл __init__.py в $module" -ForegroundColor Yellow
    }
}

Write-Host "✅ Структура модулей создана успешно!" -ForegroundColor Green