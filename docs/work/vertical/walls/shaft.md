# Shaft Walls (стены шахт)

<figure markdown>
  ![2" H-stud и C-runner с панелями shaftliner](../../../assets/images/walls/shaft-h-c-assembly.jpg)
  <figcaption markdown="span">Сборка Type 2: панели 1" x 24" shaftliner между 2" H-studs, по периметру 2" C-runner. Источник: PABCO Gypsum, H-Stud ASW.</figcaption>
</figure>

## Что это

Shaft wall - ограждение вертикальной шахты: лифт, вентканал, trash chute,
mechanical. Почти всегда fire-rated и почти всегда из металлических
профилей с гипсовым liner, поэтому это не обычная перегородка и не
[Metal Tracks](metal-tracks.md). Два рабочих типа: `2-1/2" CH + J-channel`
(шахта, liner с одной стороны) и `2" H + C-channel` (area separation wall
между юнитами, liner с двух сторон). Систему бери из UL-детали, в одной стене
они не смешиваются. Лифт из CMU деревянного
или liner-каркаса не даёт.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Планы этажей `a101` | Где реально стоят шахты: лифт, chute, vent, mech |
| Wall type schedule (`wt`), тип `7A` и подобные | CH или H, размер профиля, слои liner, gypsum снаружи |
| Детали шахты `a806` | Периметральные channels, стык с перекрытием, переход в дерево |
| Разрезы | Высота шахты по этажам; где шахта кончается выше потолка |
| S-планы | Hangers над шахтой (`DHU`), когда joists заходят над fire wall |

## Как мерить в OurPlanCore

Инструмент **Line**, единица LFT, по периметру шахты на плане каждого этажа.
Своя позиция на тип сборки и высоту; ветка - `walls/<этаж> floor walls`,
позиция называется `shaft`, дальше тип стены и высота (например `shaft 7A 10.5`).
Высота в имени обязательна: панели и вертикальные профили считаются от
**площади** стены (длина x высота), а не от длины.
Кнопка `SHF` полосы XL собирает блок Shaft walls над первым framing-листом.

1. Типовая деталь сама по себе не количество: найди каждую шахту на плане.
2. Материал фиксируй всегда: CMU-лифт, metal shaftliner, дерево. Шахту не
   выбрасывай по общей ноте `walls are panels by others`.
3. Переход дерево-шахта выше потолка не множь на полную высоту этажа.
4. Если wall type даёт shaft assembly, а план только resilient channel,
   считай resilient channel отдельно, не полную шахту.

## Как назвать в дереве и строка DFL

Что стоит в G:

- **Площадь** = длина shaft-стен (LFT) x высота, сумма по всем этажам, в SQ FT.
  Это G строк панелей и вертикальных профилей.
- **Длина** = LFT shaft-стен, сумма по этажам. От неё считаются только
  горизонтальные и периметральные профили.
- `24` в формуле панелей - площадь одной панели 2' x 12' (24 SQ FT), поэтому
  делить на 24 можно только площадь. Если в G попадёт длина, панелей выйдет
  меньше во столько раз, какова высота стены.

Type 1, `2-1/2" CH + J-channel`, liner с одной стороны:

| Строка DFL | Материал (B) | D | Формула C | G |
| --- | --- | --- | --- | --- |
| `Linear Panels` | `1" Shaft Panels` | `12`, в E `2x12 Panels` | `=ОКРВВЕРХ(G*1.1/24;2)` | площадь |
| `CH Channels Vertical` | `2 1/2" CH-channels` | `12` | `=ОКРВВЕРХ(G*0.5*1.1/D;2)` | та же площадь; `0.5` = профиль каждые 24" |
| `J Channels Horizontal` | `2 1/2" J-channels` | `12` | `=ОКРВВЕРХ(G*1.1/D;2)` | длина x 2 (верх и низ) |

Type 2, `2" H + C-channel` (area separation wall), liner с двух сторон:

| Строка DFL | Материал (B) | D | Формула C | G |
| --- | --- | --- | --- | --- |
| `Linear Panels` | `1" Shaft Panels` | `12`, в E `2x12 Panels` | `=ОКРВВЕРХ(G*2*1.1/24;2)` | площадь одной стороны; `x 2` = две стороны |
| `Channels Vertical` | `2" H-channels` | `12` | `=ОКРВВЕРХ(G*0.5*1.1/D;2)` | площадь одной стороны |
| `Channels Horizontal` | `2" H-channels` | `12` | `=ОКРВВЕРХ(G*2*1.1/D;2)` | длина; `x 2` = верх и низ |
| `Channels Perimeter` | `2" C-channels` | `12` | `=ОКРВВЕРХ(G*1.1/D;2)` | периметр стены в LFT по детали |

- D - длина штуки в футах (обычно 12), C - число штук, округление до 2.
- Профиль 16" o.c.: фактор `0.75` вместо `0.5` и подпись `CH Channels Vertical 16" o.c.`.
- Панели 10' по детали: делитель `20`, D `10`, в E `2x10 Panels`.
- Размер профиля (`2 1/2"`, `3"`, `4"`) - из wall type. `x 2` у панелей только
  в Type 2: у односторонней шахты его нет.

Полный разбор формул - [Формулы: Shaft Walls](../../../reference/formulas.md#shaft-walls).
Состав без детали пиши с `assumed; verify`. Resilient channels:
`CEILING(area x 12 / spacing x 1.1, 10)` только где показаны в типе стены;
metal RC под перекрытием обычно by others.

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-129.png">
    <img src="../../../../assets/images/confluence/confluence-129.png" alt="Профили C-T stud, J-track и J-L corner" loading="lazy">
    <div class="kb-gallery__caption">Type 1: C-T (CH) stud 2-1/2", 4", 6", J-track и J-L corner. Размер из wall type.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/walls/shaft-h-stud.png">
    <img src="../../../../assets/images/walls/shaft-h-stud.png" alt="2 inch H-stud" loading="lazy">
    <div class="kb-gallery__caption">Type 2: 2" H-stud, панели входят в пазы с двух сторон.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/walls/shaft-c-runner.png">
    <img src="../../../../assets/images/walls/shaft-c-runner.png" alt="2 inch C-runner" loading="lazy">
    <div class="kb-gallery__caption">Type 2: 2" C-runner по периметру: top, bottom, end cap.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-131.jpg">
    <img src="../../../../assets/images/confluence/confluence-131.jpg" alt="1 inch gypsum shaftliner" loading="lazy">
    <div class="kb-gallery__caption">1" shaftliner: один слой в Type 1, два слоя в Type 2. Отдельная строка.</div>
  </a>
</div>

## Частые ошибки

- Лифт из CMU записан как shaftliner, или chute wall type 7A пропущен вовсе.
- Шахты выброшены как "panels by others".
- Два типа смешаны в один блок: у них разные channels и разные формулы.
- Переход дерево-шахта умножен на полную высоту этажа.
- Hangers над шахтой взяты `ITS` вместо `DHU` по детали.
- Resilient channel посчитан как полная шахта.
- В G строки панелей стоит длина вместо площади: шахта 64 LFT x 10.5' даёт 4 панели вместо 32.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
walls/2nd floor walls/
  shaft 7A 10.5        Line, 64.0 LFT     Notes: A806 det 3, 2-1/2" CH + 1" liner
  shaft elev 10.5      Line, 48.0 LFT     Notes: CMU per S201, framing by others
```

Строки DFL для `shaft 7A 10.5`. Площадь = 64 x 10.5 = 672 SQ FT, длина = 64 LFT:

```text
Linear Panels           1" Shaft Panels       32   12   2x12 Panels   672 x 1.1 / 24 = 30.8
CH Channels Vertical    2 1/2" CH-channels    32   12                 672 x 0.5 x 1.1 / 12 = 30.8
J Channels Horizontal   2 1/2" J-channels     12   12                 64 x 2 x 1.1 / 12 = 11.7
```

## См. также

- [Формулы: Shaft Walls](../../../reference/formulas.md#shaft-walls), [Demising Walls](demising.md)
- [Metal Tracks](metal-tracks.md), [Hangers](../../../reference/hangers.md)
- [Wall Panels](wall-panels.md): шахта не исключается общей нотой
