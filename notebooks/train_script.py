# Minimal retrain script that marks retrain timestamp
from pathlib import Path
Path('reports').mkdir(parents=True, exist_ok=True)
with open('reports/auto_retrain.txt','w') as f:
    f.write('Auto retrained at: ' + __import__('datetime').datetime.now().isoformat())
print('Auto retrain marker written to reports/auto_retrain.txt')