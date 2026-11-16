# Soffit & Fascia

<figure markdown>
  ![Roof overhang corner from below: vented soffit and fascia](../../assets/images/photos/trims/soffit-vented-panel-fascia.jpg)
  <figcaption markdown="span">Eave corner from below: vented soffit panels between the wall and the fascia, fascia with a gutter along the edge. Soffit is counted by area (overhang length times width), fascia in LFT along the same line. Photo: brothersgutters.com, [source](https://brothersgutters.com/gutter-services/exterior-solutions/fascia-board/), found via Pinterest.</figcaption>
</figure>

<figure markdown>
  ![Cornice eave return](../../assets/images/trims/ext-eave-return.png)
  <figcaption markdown="span">Gable corner: the eave with soffit and fascia runs along the wall, the rake follows the slope, a return in the corner. The return length is measured as its own line and added to the eave length in the soffit and fascia rows.</figcaption>
</figure>

## What it is

Soffit (the underside of the overhang), fascia (the edge board), frieze (the board on the wall
under the soffit), rake moulding, returns and porch columns. Usually a separate block
`Soffits and Fascias`. Eave and rake lengths come from
[Eve](../sheathing-and-misc/eve.md) and [Rake](../sheathing-and-misc/rake.md);
soffit sheathing (5/8" exterior gypsum, plywood) is
[Sheathing](../vertical/sheathing/wall-sheathing.md), not trim. Plywood as the
visible soffit finish itself is different: it is `AC Ply` in `Soffits at Eves`,
SQ FT (defaults table below).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Eave and rake details (A5xx) | Overhang width, soffit material (vinyl vented, beadboard, 1x), fascia, frieze, rake moulding |
| Elevations | Where the eaves are, where the rakes are, returns (cornice or pork-chop), columns and their type |
| RCP and porch sections | Porch and canopy ceiling: material, area, 5/8" exterior gypsum under the finish |
| Spec | `Soffits assumed Vinyl; Fascias assumed PVC or 1x Alum wrapped; verify` |

## How to measure in OurPlanCore

Overhang lengths are Lines in `eves rakes/eves` and `eves rakes/rakes` with the overhang in
inches in the name (`eve 24 main`, `rake 12 main`, `returns 24`): one line
feeds both the trim and the overhang sheathing. Soffit as an area (beadboard, panel) is an
Area along the real underside outline in `trims` or in the job's agreed branch
(`rcp 1.6`); the outline is not the roof deck. Do not feed one area twice:
either `length x width` or an Area. A canopy is not part of eave and rake; it has its own
rows. Columns are Count points.

## Tree name and DFL row

| Tree name | DFL row | Size | Unit | Rule |
| --- | --- | --- | --- | --- |
| `eves rakes/eves/eve 24 main` | `Soffits at Eves` | `12" Vinyl vented`, `T&G beadboard`, `Soffit panel` | SQ FT | `=EVEN((eve + returns)*G/12*1.1)`, G = soffit width in inches |
| | `Soffits at Eves` | `1x12`, `1x4`, a single narrow vinyl strip | LFT | a soffit ONE board or strip wide: `=EVEN((eve + returns)*1.1)`, no width |
| | `Fascia at Eves` | `1x8`, `1x10`, `1x6`, `2x8` | LFT | `=EVEN((eve + returns)*1.1)` |
| | `Frieze Board` | `5/4x6` / `5/4x10` | LFT | on the wall under the soffit, only where the section shows it; same length |
| | `Crowns` | `3" crown` | LFT | crown or moulding under the fascia or at the frieze, only where the section shows it |
| | `Over Fascia Trims` | `1x3` / `1x4` | LFT | second board over the fascia; same length as the fascia |
| `eves rakes/rakes/rake 12 main` | `Soffits at Rakes`, `Fascia at Rakes` | `9" Vinyl`, `1x12`; `1x8`, `1x6` | SQ FT or LFT; LFT | separate from eaves: `=EVEN(rake*G/12*1.1)` and `=EVEN(rake*1.1)`; the same one-board rule |
| `eves rakes/eves/returns 24` | no row of its own | | LFT | the number in the name is the overhang of the eave that turns the corner; the returns length is added to the eave in `Soffits at Eves` and `Fascia at Eves` |
| `trims/soffit porch` | `Soffits at Porch`, `Soffits at Canopy`, `Soffits at Floor Overhangs` | `Beadboard`, `Azek Beadboard` | SQ FT | their own rows, not in main eaves |
| `trims/columns` | `Columns` | `12" Dia Fbg Non-taper` | column height (`8'`) | C = number of columns; taper, round or square in B; E `w/ cap & base` |
| | `Post Wrap` | `1x8` | LFT | boards around a post, not a column: G = height x 4 sides x number of posts; C = G x 1.1, under 50 round up to 2, from 50 up to 10 |
| | `Posts at Rails`, `Post Sleeve`, `Post Cap` | `4x4 P.T.`, `Sleeve for 4x4` | `4` for posts (post length), pcs for sleeves and caps | a set, see [Rails & Decking](rails-decking.md) |

In the formulas `eve`, `returns` and `rake` are the lengths from the tree in LFT; in
the DFL template they come from the eaves table on their own, and only the width in G
is typed by hand. `EVEN` rounds up to an even number.

### Soffit: LFT or SQ FT

- Soffit is counted in `SQ FT`: (eave + returns) x width / 12 x 1.1.
- `LFT` only when the overhang is closed by ONE board or one strip across its width
  (`1x12`, `1x4`, a single narrow vinyl strip): (eave + returns) x 1.1, and the width
  is not in the formula.
- Check with one question: how many pieces of material lie across the overhang? One
  piece = LFT. Panels, beadboard, several boards = SQ FT.
- So `12" Vinyl vented` panels are SQ FT at any overhang. A 9" overhang is LFT
  only if it is closed by a single `1x10` or a single strip; the same 9" overhang in
  vinyl panels is SQ FT.
- Aluminum and metal soffit, and fascia with an alum wrap on the section: by others,
  no row, with a note.

Soffit not named on the drawings: pick it by the siding type (training).

| Siding | Default soffit | Unit |
| --- | --- | --- |
| Vinyl | vinyl soffit | SQ FT |
| Wood or composite clapboard | `1x` Azek board; if many overhangs are wider than 12", soffit panel for all | LFT; panel SQ FT |
| Cedar shingles | beadboard | SQ FT |
| Hardie, board and batten, panels | soffit panel | SQ FT |
| Plywood soffit per the detail | `AC Ply` | SQ FT, not `4x8` sheets |

Material assumed, not read from the drawings: `Note: Soffits assumed Vinyl; Fascias
assumed PVC or 1x Alum wrapped; verify`. Do not substitute wood if vinyl or alum is
possible.

<figure markdown>
  ![Eave section with DFL rows](../../assets/images/roof/eave-parts-takeoff.svg)
  <figcaption markdown="span">Eave section: soffit, fascia, sub fascia, frieze, trim over fascia and the soffit frame, each part with its own row and unit.</figcaption>
</figure>

<figure markdown>
  ![Rake: elevation, plan and overhang section](../../assets/images/roof/rake.svg)
  <figcaption markdown="span">Rake at the gable: where to draw the line and which rows it gives, rake moulding included.</figcaption>
</figure>

<figure markdown>
  ![Pork-chop eave return](../../assets/images/trims/ext-pork-chop.png)
  <figcaption markdown="span">Pork-chop return: a simple triangular stub. Trim is minimal, but the fascia and a small soffit are counted.</figcaption>
</figure>

## Common mistakes

- Canopy and porch counted again in eave and rake.
- Soffit panel counted both as LFT x width and as an Area.
- A panel soffit written in LFT, or a one-board soffit in SQ FT.
- Eaves and rakes in one row with different sizes.
- Returns not measured with a `returns` line: soffit and fascia along them missed.
- A label that differs from the template: `Frieze` instead of `Frieze Board`, `Trim over fascia` instead of `Over Fascia Trims`.
- Columns without type, taper and height; `Post Wrap` confused with a column.
- 5/8" exterior gypsum soffit written in trim instead of sheathing and WRB.
- All roof mistakes: [Roof](../../start/common-mistakes.md#roof).

## Example

```text
Takeoffs/Main/eves rakes/eves/eve 24 main     Line   310 LFT
Takeoffs/Main/eves rakes/eves/returns 24      Line   8 LFT
Takeoffs/Main/eves rakes/rakes/rake 12 main   Line   96 LFT

Soffits at Eves     12" Vinyl vented   700  SQ FT  =EVEN((310+8)*24/12*1.1)   24" Projection
Fascia at Eves      1x8                350  LFT    =EVEN((310+8)*1.1)
Frieze Board        5/4x6              350  LFT    =EVEN((310+8)*1.1)
Soffits at Rakes    1x12               106  LFT    =EVEN(96*1.1)              12" Projection
Fascia at Rakes     1x6                106  LFT    =EVEN(96*1.1)
Columns             12" Dia Fbg Non-taper   4  8'     w/ cap & base

Eave soffit: 12" panels on a 24" overhang = SQ FT: 318 x 24 / 12 x 1.1 = 699.6, up to even = 700
Rake soffit: a 12" overhang closed by one 1x12 board = LFT: 96 x 1.1 = 105.6, up to even = 106
Fascia and frieze: 318 x 1.1 = 349.8, up to even = 350
```

## See also

- [Overview](overview.md), [Casing, Corner & Band](casing-corner-band.md), [Porch / Deck / Balcony](porch-deck-balcony.md)
- [Eve](../sheathing-and-misc/eve.md), [Rake](../sheathing-and-misc/rake.md), [Returns](../sheathing-and-misc/returns.md), [Canopy](../horizontal/roof-framing/canopy.md)
- [Porch SQFT](../sqfts/porch.md), [Standard notes](../../reference/standard-notes.md)
