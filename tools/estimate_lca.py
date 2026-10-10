"""Transparent hypothetical AI service footprint arithmetic (no external dependencies).

Not a measurement or a certified lifecycle assessment.
"""
import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


def number(record, key, *, minimum=Decimal('0')):
    if key not in record or record[key] is None or isinstance(record[key], bool):
        raise ValueError(f'Missing/invalid {key}')
    try:
        value = Decimal(str(record[key]))
    except (InvalidOperation, ValueError):
        raise ValueError(f'Invalid number {key}') from None
    if not value.is_finite() or value < minimum:
        raise ValueError(f'Invalid range for {key}')
    return value


def calculate(record):
    if record.get('status') not in ('ILLUSTRATIVE', 'ESTIMATED', 'MEASURED'):
        raise ValueError('status must be ILLUSTRATIVE, ESTIMATED or MEASURED')
    for field in ('system_boundary', 'factor_source', 'factor_method', 'model_or_workload'):
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError(f'Missing disclosure {field}')
    it_kwh = number(record, 'it_energy_kwh')
    pue = number(record, 'pue', minimum=Decimal('1'))
    intensity = number(record, 'grid_intensity_kgco2e_per_kwh')
    embodied = number(record, 'allocated_embodied_kgco2e')
    count = number(record, 'valid_results', minimum=Decimal('1'))
    site_kwh = it_kwh * pue
    op = site_kwh * intensity
    total = op + embodied
    return {
        'status': record['status'],
        'measured_footprint': record['status'] == 'MEASURED',
        'system_boundary': record['system_boundary'],
        'model_or_workload': record['model_or_workload'],
        'site_energy_kwh': str(site_kwh),
        'operational_kgco2e': str(op),
        'allocated_embodied_kgco2e': str(embodied),
        'total_included_kgco2e': str(total),
        'kgco2e_per_1000_valid_results': str(total * Decimal('1000') / count),
        'factor_method': record['factor_method'],
        'factor_source': record['factor_source'],
        'warning': 'Illustrative/estimated values are not verified impact measurements.'
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('json_input', type=Path)
    args = p.parse_args()
    try:
        result = calculate(json.loads(args.json_input.read_text(encoding='utf-8')))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        p.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
