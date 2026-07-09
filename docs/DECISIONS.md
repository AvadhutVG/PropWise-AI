# Engineering Decisions

## Dataset

- Bengaluru House Price Dataset

---

## Decision 1

Dropped `society` column.

Reason:
- More than 40% missing values.
- Very high cardinality.
- Low expected contribution to prediction.

---

## Decision 2

Converted `total_sqft` ranges into their average value.

Example:

1200 - 1500 → 1350

---

## Decision 3

Removed unsupported units (Acres, Sq. Meter, Guntha, etc.)

Reason:

- Only 46 rows affected (~0.35%).
- Simpler and more maintainable preprocessing pipeline.

---

## Decision 4

Removed rows with missing values in:

- location
- size
- bath

Reason:

Very small percentage of missing data.

---

## Decision 5

Removed duplicate rows after preprocessing.

Final dataset:

12632 rows