from pathlib import Path


directory = Path(r'C:\Users\user\Desktop\Work\ExcelWorker')
line_count = 0

for f in directory.rglob('*.py'):
    if not f.is_file() or not f.exists():
        continue

    local_count = 0
    for line in f.read_text(encoding="utf8").splitlines():
        line = line.strip()
        if not line or line.startswith(('#', '"', "'")):
            continue
        local_count += 1
    
    print(f'{f} - {local_count} ст')
    line_count += local_count

print("=====================================")
print(f"Всего строк - {line_count}")