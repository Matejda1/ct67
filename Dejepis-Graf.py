import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Let's generate a refined and beautiful chart specifically for retail fuel prices in CZK/l (estimated based on Brent and crisis timeline)
dates = [
    datetime.date(2026, 2, 25),
    datetime.date(2026, 3, 5),
    datetime.date(2026, 3, 20),
    datetime.date(2026, 4, 10),
    datetime.date(2026, 5, 1),
    datetime.date(2026, 5, 20),
    datetime.date(2026, 6, 10),
    datetime.date(2026, 7, 1),
    datetime.date(2026, 7, 20),
    datetime.date(2026, 8, 10),
    datetime.date(2026, 9, 1)
]

# Estimated Czech retail prices (CZK/l) for Natural 95 and Diesel during the crisis
natural_95 = [36.5, 41.2, 39.8, 41.5, 43.8, 44.0, 45.5, 47.0, 50.2, 47.1, 48.0]
diesel = [35.8, 40.5, 39.2, 40.8, 43.0, 40.2, 43.8, 42.2, 47.5, 49.4, 51.2]

plt.figure(figsize=(10, 5))
plt.plot(dates, natural_95, marker='o', color='#e67e22', linewidth=2.5, label='Natural 95 (Kč/l)')
plt.plot(dates, diesel, marker='s', color='#2980b9', linewidth=2.5, label='Nafta (Kč/l)')
plt.title('Vývoj cen pohonných hmot v ČR během krize (2026)', fontsize=12, fontweight='bold')
plt.xlabel('Datum', fontsize=10)
plt.ylabel('Cena (Kč / litr)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axvline(datetime.date(2026, 2, 28), color='black', linestyle=':', label='Začátek krize (28. 2. 2026)')
plt.legend()
plt.tight_layout()
plt.savefig('pohonne_hmoty_cr_graf3.png', dpi=300)
print("Graf pohonných hmot vytvořen.")