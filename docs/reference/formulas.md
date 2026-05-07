# Formulas and Factors

## Joist / Stud Spacing Factors

| Spacing | Factor |
| --- | ---: |
| 12" o.c. | 1.4667 |
| 16" o.c. | 1.1 |
| 24" o.c. | 0.625 |

For studs at 16" o.c., boss feedback says use 1:1 plus 10% waste rather than
0.75. For 24" o.c., use 0.5 plus 25% waste.

## Rim and Blocking

| Item | Unit | Factor |
| --- | --- | --- |
| Rim Board | LFT | 1.05 |
| Blocking | LFT | no factor if continuous |
| Ribbons / ledgers / bracing | pieces | use 16' ceiling when required |

## COM Waste

- Use 1.1 for formulas unless the source value already includes the 1.1.
- Do not double-count waste through chained formulas.

## Shaft Walls

```text
CH channels vertical  = LFT * 0.5 * 1.1 / 12
J-channels horizontal = LFT * 2 / 10 * 1.1 / 10
Shaft panels          = LFT * 0.5 * 1.1, listed as 2x12
```

## Dropped Ceiling Metal Joists

```text
12" C-type metal joists = Area * 0.75 * 1.1 LF
```

## Blocking Formulas

```excel
Flat 48" o.c.     = CEILING(G * 12 / 48 * 2 * 1.1 / D, 1)
Diagonal 48" o.c. = CEILING(G * 12 / 48 * 2.5 * 1.1 / D, 1)
```

## Kitchen and Bath Blocking

| Location | Rule |
| --- | --- |
| Kitchen | 2x6 blocking, 4 pieces of 14' per kitchen |
| Bathroom | 2x6 blocking, 1 piece of 14' per bathroom |
