# Blocking oc

## Formulas

Используй project-specific Excel syntax, но logic from notes такая:

```text
Flat 48" o.c.     = G * 12 / 48 * 2 * 1.1 / D, ceiling to 1
Diagonal 48" o.c. = G * 12 / 48 * 2.5 * 1.1 / D, ceiling to 1
```

## Проверить

- Убедись, что 1.1 уже не included upstream.
- Используй 16' ceiling для ribbons, bracings и ledgers, когда требуется.
- Plates и wall blocking держи в LFT, когда это expected output.
