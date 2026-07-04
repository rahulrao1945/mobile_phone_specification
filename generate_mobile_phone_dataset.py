import csv
import random
from pathlib import Path

random.seed(42)

output_path = Path(__file__).with_name('mobile_phone_specifications_and_price_dataset_2026.csv')

brands = [
    'Samsung', 'Apple', 'Xiaomi', 'OnePlus', 'Google', 'Motorola', 'Vivo', 'Oppo',
    'Realme', 'Nothing', 'Asus', 'Sony', 'Honor', 'Huawei', 'Nokia', 'Poco', 'iQOO'
]

brand_models = {
    'Samsung': ['Galaxy A15', 'Galaxy A25', 'Galaxy S23', 'Galaxy S24', 'Galaxy S24 Ultra', 'Galaxy Z Flip5', 'Galaxy Z Fold5', 'Galaxy XCover7'],
    'Apple': ['iPhone 14', 'iPhone 14 Plus', 'iPhone 15', 'iPhone 15 Plus', 'iPhone 15 Pro', 'iPhone 15 Pro Max', 'iPhone 16'],
    'Xiaomi': ['Redmi 12', 'Redmi Note 13 Pro', 'Xiaomi 13 Lite', 'Xiaomi 14', 'Xiaomi 14T Pro', 'Mi 14 Ultra', 'Poco F6'],
    'OnePlus': ['Nord CE 3 Lite', 'OnePlus 11R', 'OnePlus 12', 'OnePlus 12R', 'OnePlus Open', 'OnePlus 13'],
    'Google': ['Pixel 7a', 'Pixel 8', 'Pixel 8 Pro', 'Pixel 8a', 'Pixel 9', 'Pixel Fold'],
    'Motorola': ['Moto G54', 'Moto Edge 40', 'Moto Razr 40', 'Moto G84', 'Moto Edge 50 Pro', 'Moto X50 Ultra'],
    'Vivo': ['Vivo Y18', 'Vivo V30e', 'Vivo V30', 'Vivo X100', 'Vivo X100 Pro', 'Vivo V40 Pro'],
    'Oppo': ['Reno 10', 'Reno 11', 'Find X6', 'Find X7', 'A98', 'Oppo F25 Pro'],
    'Realme': ['Narzo 70', 'Realme 12+', 'Realme 12 Pro', 'Realme GT 6', 'Realme GT 6T', 'Realme 13 Pro+'],
    'Nothing': ['Phone (2)', 'Phone (2a)', 'Phone (3)', 'Phone (2) Plus'],
    'Asus': ['Zenfone 10', 'ROG Phone 7', 'ROG Phone 8', 'Zenfone 11 Ultra', 'ROG Phone 7 Ultimate'],
    'Sony': ['Xperia 10 VI', 'Xperia 1 V', 'Xperia 5 V', 'Xperia 10 V', 'Xperia 1 VI'],
    'Honor': ['Honor 200', 'Honor X9b', 'Honor Magic6 Lite', 'Honor 200 Pro', 'Honor Magic V2', 'Honor Magic6 Pro'],
    'Huawei': ['Pura 70', 'Nova 12', 'Mate 60 Pro', 'P60 Pro', 'Mate XT'],
    'Nokia': ['G42', 'C32', 'X30', 'Nokia XR21', 'Nokia G60', 'Nokia 2780 Flip'],
    'Poco': ['Poco M6', 'Poco X6', 'Poco F5', 'Poco X6 Pro', 'Poco F6 Pro'],
    'iQOO': ['iQOO Z9', 'iQOO Neo 9', 'iQOO 12', 'iQOO 12 Pro', 'iQOO Neo 10']
}

processors = {
    'budget': ['Snapdragon 4 Gen 2', 'MediaTek Helio G99', 'Snapdragon 695', 'MediaTek Dimensity 700', 'Unisoc T760'],
    'mid': ['Snapdragon 7 Gen 3', 'MediaTek Dimensity 7200', 'Snapdragon 7s Gen 2', 'Dimensity 8300 Ultra', 'Exynos 1380'],
    'premium': ['Snapdragon 8 Gen 2', 'MediaTek Dimensity 9200+', 'Google Tensor G3', 'Exynos 2400', 'Snapdragon 8+ Gen 1'],
    'flagship': ['Snapdragon 8 Gen 3', 'MediaTek Dimensity 9400', 'Apple A17 Pro', 'Apple A18 Pro', 'Google Tensor G4', 'Exynos 2500']
}

chipsets = {
    'budget': ['Snapdragon 4 Gen 2', 'Helio G99', 'Snapdragon 695', 'Dimensity 700', 'Unisoc T760'],
    'mid': ['Snapdragon 7 Gen 3', 'Dimensity 7200', 'Snapdragon 7s Gen 2', 'Dimensity 8300 Ultra', 'Exynos 1380'],
    'premium': ['Snapdragon 8 Gen 2', 'Dimensity 9200+', 'Tensor G3', 'Exynos 2400', 'Snapdragon 8+ Gen 1'],
    'flagship': ['Snapdragon 8 Gen 3', 'Dimensity 9400', 'A17 Pro', 'A18 Pro', 'Tensor G4', 'Exynos 2500']
}

gpus = {
    'budget': ['Adreno 610', 'Mali-G57 MC2', 'Adreno 619', 'Mali-G57 MC3', 'Mali-G57 MC1'],
    'mid': ['Adreno 725', 'Mali-G610 MC6', 'Adreno 732', 'Immortalis-G715', 'Mali-G615 MC2'],
    'premium': ['Adreno 740', 'Immortalis-G720', 'Mali-G710 MC10', 'Xclipse 920', 'Adreno 735'],
    'flagship': ['Adreno 750', 'Immortalis-G925', 'Apple GPU (6-core)', 'Apple GPU (5-core)', 'Mali-G715 MC7']
}

display_types = ['AMOLED', 'OLED', 'IPS LCD', 'LTPO AMOLED', 'Super AMOLED']

colors = ['Black', 'White', 'Blue', 'Silver', 'Midnight', 'Graphite', 'Purple', 'Green', 'Gold', 'Titanium', 'Gray', 'Red']

resolution_map = {
    'budget': ['720x1600', '1080x2400'],
    'mid': ['1080x2400', '1080x2520', '1440x3200'],
    'premium': ['1440x3200', '1560x3120', '1290x2796'],
    'flagship': ['1440x3200', '1800x3200', '1290x2796', '1440x3120']
}

os_versions = {
    'Android': ['13', '14', '15'],
    'iOS': ['17', '18']
}

sim_types = ['Dual SIM', 'Single SIM', 'Dual SIM (Nano-SIM)', 'Dual SIM (Nano-SIM/eSIM)']

fingerprints = ['Side-mounted', 'Under-display', 'Rear-mounted', 'None']

water_resistance = ['IP52', 'IP54', 'IP67', 'IP68', 'None']

wifi_standards = ['Wi-Fi 5', 'Wi-Fi 6', 'Wi-Fi 6E', 'Wi-Fi 7']

bluetooth_versions = ['5.0', '5.1', '5.2', '5.3', '5.4']

# Balanced distribution across tiers and brands
brand_counts = {}
for idx, brand in enumerate(brands):
    if idx < 15:
        brand_counts[brand] = [74, 74, 73, 73]
    else:
        brand_counts[brand] = [75, 74, 73, 73]

rows = []
phone_ids = set()
seen_rows = set()

for brand in brands:
    counts = brand_counts[brand]
    tiers = ['budget', 'mid', 'premium', 'flagship']
    for tier, count in zip(tiers, counts):
        for _ in range(count):
            while True:
                phone_id = f'PH-{random.randint(100000, 999999)}'
                if phone_id not in phone_ids:
                    phone_ids.add(phone_id)
                    break

            model_base = random.choice(brand_models[brand])
            year = random.randint(2022, 2026)
            if tier == 'budget':
                year = random.choice([2022, 2023, 2024])
            elif tier == 'mid':
                year = random.choice([2023, 2024, 2025])
            else:
                year = random.choice([2024, 2025, 2026])

            if tier == 'budget':
                ram = random.choice([4, 6, 8])
                storage = random.choice([64, 128, 256])
                usd = random.randint(150, 280)
                battery = random.randint(3000, 4500)
                charging = random.choice([10, 18, 22, 33, 45])
                display = round(random.uniform(6.0, 6.8), 1)
                refresh = 60
                wireless = 'No'
                has_5g = random.choice(['No', 'No', 'Yes'])
                has_nfc = 'No'
                weight = random.randint(175, 220)
                rating = round(random.uniform(3.5, 4.2), 1)
                reviews = random.randint(10, 12000)
                os_name = 'Android'
            elif tier == 'mid':
                ram = random.choice([6, 8, 12])
                storage = random.choice([128, 256, 512])
                usd = random.randint(300, 599)
                battery = random.randint(4000, 5200)
                charging = random.choice([45, 67, 80])
                display = round(random.uniform(6.2, 6.9), 1)
                refresh = random.choice([90, 120])
                wireless = random.choice(['No', 'Yes'])
                has_5g = 'Yes'
                has_nfc = random.choice(['No', 'Yes'])
                weight = random.randint(165, 210)
                rating = round(random.uniform(4.0, 4.6), 1)
                reviews = random.randint(500, 25000)
                os_name = 'Android'
            elif tier == 'premium':
                ram = random.choice([8, 12, 16])
                storage = random.choice([256, 512])
                usd = random.randint(600, 999)
                battery = random.randint(4500, 5500)
                charging = random.choice([45, 67, 80, 100])
                display = round(random.uniform(6.1, 6.8), 1)
                refresh = random.choice([120, 144])
                wireless = 'Yes'
                has_5g = 'Yes'
                has_nfc = 'Yes'
                weight = random.randint(160, 205)
                rating = round(random.uniform(4.2, 4.8), 1)
                reviews = random.randint(3000, 50000)
                os_name = random.choice(['Android', 'iOS'])
            else:  # flagship
                ram = random.choice([12, 16, 24])
                storage = random.choice([256, 512, 1024])
                usd = random.randint(1000, 1800)
                battery = random.randint(5000, 7000)
                charging = random.choice([80, 100, 150])
                display = round(random.uniform(6.3, 7.2), 1)
                refresh = random.choice([120, 144])
                wireless = 'Yes'
                has_5g = 'Yes'
                has_nfc = 'Yes'
                weight = random.randint(150, 202)
                rating = round(random.uniform(4.4, 5.0), 1)
                reviews = random.randint(10000, 50000)
                os_name = random.choice(['Android', 'iOS'])

            if brand == 'Apple' and os_name != 'iOS':
                os_name = 'iOS'
            if brand != 'Apple' and os_name == 'iOS':
                os_name = 'Android'

            processor = random.choice(processors[tier])
            chipset = random.choice(chipsets[tier])
            gpu = random.choice(gpus[tier])

            if brand == 'Apple':
                processor = random.choice(['A16 Bionic', 'A17 Pro', 'A18 Pro'])
                chipset = processor
                gpu = random.choice(['Apple GPU (5-core)', 'Apple GPU (6-core)'])
            elif brand == 'Google':
                processor = random.choice(['Google Tensor G3', 'Google Tensor G4'])
                chipset = processor
                gpu = random.choice(['Mali-G715 MC7', 'Mali-G710 MC10'])

            if tier == 'budget':
                display_type = random.choice(['IPS LCD', 'AMOLED'])
            elif tier == 'mid':
                display_type = random.choice(['AMOLED', 'OLED', 'Super AMOLED'])
            elif tier == 'premium':
                display_type = random.choice(['AMOLED', 'LTPO AMOLED', 'OLED'])
            else:
                display_type = random.choice(['AMOLED', 'LTPO AMOLED', 'OLED', 'Super AMOLED'])

            resolution = random.choice(resolution_map[tier])
            rear_cam = random.choice([12, 48, 50, 64, 108])
            front_cam = random.choice([8, 12, 16, 20])
            num_rear = random.choice([2, 3, 4]) if rear_cam >= 48 else 2
            video = random.choice(['4K@60fps', '8K@30fps', '4K@120fps', '8K@24fps'])
            if tier == 'budget':
                video = random.choice(['1080p@30fps', '4K@30fps'])

            if brand == 'Apple':
                model = random.choice(['iPhone 14', 'iPhone 14 Plus', 'iPhone 15', 'iPhone 15 Plus', 'iPhone 15 Pro', 'iPhone 15 Pro Max', 'iPhone 16'])
            elif brand == 'Samsung':
                model = random.choice(['Galaxy A15', 'Galaxy A25', 'Galaxy S23', 'Galaxy S24', 'Galaxy S24 Ultra', 'Galaxy Z Flip5', 'Galaxy Z Fold5'])
            elif brand == 'Google':
                model = random.choice(['Pixel 7a', 'Pixel 8', 'Pixel 8 Pro', 'Pixel 8a', 'Pixel 9', 'Pixel Fold'])
            else:
                model = model_base

            if brand == 'Nothing' and tier == 'flagship':
                model = 'Phone (3)'

            price_inr = int(round(usd * 83.0))
            rating = min(5.0, max(3.5, rating))
            if tier == 'flagship' and brand == 'Apple':
                rating = round(random.uniform(4.6, 5.0), 1)

            row = [
                phone_id,
                brand,
                model,
                year,
                usd,
                price_inr,
                ram,
                storage,
                processor,
                chipset,
                gpu,
                battery,
                charging,
                wireless,
                display,
                resolution,
                refresh,
                display_type,
                rear_cam,
                front_cam,
                num_rear,
                video,
                os_name,
                random.choice(os_versions[os_name]),
                random.choice(sim_types),
                has_5g,
                has_nfc,
                random.choice(bluetooth_versions),
                random.choice(wifi_standards),
                random.choice(fingerprints),
                random.choice(water_resistance),
                weight,
                random.choice(colors),
                f'{rating:.1f}',
                random.randint(10, 50000),
            ]
            row_key = tuple(row)
            if row_key in seen_rows:
                continue
            seen_rows.add(row_key)
            rows.append(row)

with output_path.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'Phone_ID', 'Brand', 'Model', 'Release_Year', 'Price_USD', 'Price_INR', 'RAM_GB', 'Storage_GB', 'Processor', 'Chipset', 'GPU',
        'Battery_mAh', 'Charging_Watts', 'Wireless_Charging', 'Display_Size_Inches', 'Resolution', 'Refresh_Rate_Hz', 'Display_Type',
        'Rear_Camera_MP', 'Front_Camera_MP', 'Number_of_Rear_Cameras', 'Video_Recording', 'Operating_System', 'OS_Version', 'SIM_Type',
        'Has_5G', 'Has_NFC', 'Bluetooth_Version', 'WiFi_Standard', 'Fingerprint_Type', 'Water_Resistance', 'Weight_Grams', 'Color',
        'User_Rating', 'Number_of_Reviews'
    ])
    writer.writerows(rows)

print(f'Created {len(rows)} rows at {output_path}')
