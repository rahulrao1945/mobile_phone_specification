import csv
from pathlib import Path

source_path = Path('mobile_phone_specifications_and_price_dataset_2026.csv')
output_dir = Path('.')

with source_path.open('r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

chunk_size = 1000
parts = [rows[i:i + chunk_size] for i in range(0, len(rows), chunk_size)]

for idx, part in enumerate(parts, start=1):
    output_path = output_dir / f'mobile_phones_part{idx}.csv'
    with output_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(part)
    print(f'Wrote {len(part)} rows to {output_path}')

print(f'Total parts: {len(parts)}')
