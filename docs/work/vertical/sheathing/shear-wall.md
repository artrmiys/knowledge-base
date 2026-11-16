# Shear Wall (стена жёсткости)

<figure markdown>
  ![Внутренняя shear wall, обшитая OSB с одной стороны](../../../assets/images/photos/sheathing/sh-shear-wall-interior-osb.jpg)
  <figcaption markdown="span">Внутренняя shear wall: OSB только с одной стороны, по таблице. Длина участка - Line в ветке shear walls; обшивка - по SW schedule, не по Arch. Фото: bbaunach, CC BY 2.0, <a href="https://www.flickr.com/photos/93734858@N00/5792759950">источник</a>.</figcaption>
</figure>

## Что это

Shear wall (SW) - участок стены, который держит ветер и сейсмику через
структурную обшивку, усиленную гвоздёвку и holdowns на концах. Обшивка SW
считается строго по structural shear wall schedule: тип, толщина, сторона,
слои. Обычная стена той же длины уже есть в `walls`: SW не складывается с ней,
а добавляет только то, чего в обычной стене нет (вторую сторону, другой
материал). Анкеровка - отдельная страница [Holdowns](holdowns.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Shear wall schedule (S) | Марка, обшивка и толщина, одна или две стороны, blocking, nailing, holdown, шаг анкеров |
| Framing plan (`s201 2nd`) | Марки SW и их границы; план перекрытия показывает стены ниже - этаж из notes "walls below/above" |
| Details holdown и SW | Что у концов стены, что между этажами |
| Wall sections (`sec`) | На каком уровне стена, высота |

<figure markdown>
  ![Фрагмент shear wall schedule](../../../assets/images/confluence/confluence-153.png)
  <figcaption markdown="span">Shear wall schedule: марка, обшивка, blocking, крепёж, шаг анкеров. Одна марка в другом доме не означает ту же спецификацию. Архивный фрагмент.</figcaption>
</figure>

## Как мерить в OurPlanCore

1. Инструмент Line по фактическому сегменту SW между его границами, не по
   контуру комнаты. Единица LFT.
2. План перекрытия показывает SW этажа ниже: копия листа в `Struct/Shear` с
   точкой S направляет новые замеры в `shear walls/<этаж ниже>`.
3. Одна позиция на строку schedule: `SW4-1` и `SW4-2` не объединяй по
   одинаковой длине. Внутри позиции может быть несколько участков.
4. Прочитай сторону: наружная сторона ext SW уже посчитана в `Wall Sheathing`
   наружных стен, нужна только внутренняя (ext SW с обшивкой с одной стороны
   строки не даёт). Внутренняя SW с двух сторон - одна линия по длине стены;
   удвоение стоит в строке DFL (`(2 sides)` и `*2` в формуле), длину второй
   раз не удваивай. `P` у марки = perforated.
5. На panel-job одна обшитая сторона уже в панели; считаем только требуемую
   вторую.

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Материал | Unit | Формула |
| --- | --- | --- | --- | --- |
| `shear walls/1st floor/shear/SW1-1` | `Shear Walls SW1-1` в блоке стен этажа, одна строка на марку | по schedule, например `15/32" Ply` | `4x8` | `=ОКРВВЕРХ(G*H/32*1.1;1)` |
| `shear walls/1st floor/shear/WSW-C 7-16 OSB DTT2Z` | `Shear Walls WSW-C` | `7/16" OSB` | `4x8` | то же |
| внутренняя SW с двух сторон | `Shear Walls SW-F (2 sides)` | по schedule | `4x8` | `=ОКРВВЕРХ(G*H*2/32*1.1;1)` |
| `shear walls/2nd floor/shear/ext W4B` | `Shear Walls W4B`, только внутренняя сторона | по schedule | `4x8` | как у односторонней |
| отдельно | `Draft Stop` | из легенды roof plan | `SQ FT` | не из суммы SW, см. [Gable Sheathing](gable.md) |

Что стоит в формуле:

- **G** - длина SW в LFT (остаётся длиной, площадь в G не пишется).
- **H** - высота стены этажа в футах, та же, что в имени стены
  (`ext 2x6 9.09` даёт H = 9.09). Стена от перекрытия до перекрытия - H =
  floor-to-floor.
- `G x H` - площадь стороны, `/32` - листы `4x8`, `x 1.1` - запас.
- В E - сторона и лист: `int S5.01`, `int one side`.

Имя = марка плюс подтверждённые отличия (материал, толщина, крепёж).
Полоса XL, кнопка SW, кладёт площади в блок стен этажа.

## Частые ошибки

- Две стороны удвоены дважды (и в длине, и `*2` в формуле), или `P` прочитано как две стороны.
- В H стоит высота другого этажа или floor-to-floor вместо высоты стены.
- Строки schedule с разной спецификацией слиты по длине.
- Этаж SW взят по листу, а не по notes "walls below": SW ушла на этаж выше.
- Draft stop чердака скопирован из суммы shear walls.
- FRT для demising SW поставлен автоматически; FRT только по правилам наружной стены.
- A35 и прочие клипсы добавлены по привычке, а не по детали.

Все ошибки: [common-mistakes](../../../start/common-mistakes.md#holdowns).

## Пример

```text
Takeoffs/Main/shear walls/1st floor/shear/
  SW1-1                      Line   86 LFT
  WSW-C 7-16 OSB DTT2Z       Line   42 LFT
  ext W4B                    Line  118 LFT
Takeoffs/Main/shear walls/1st floor/holdowns/
  HDU11 SB1x30 S2.2          Count  14

1st Floor Walls (высота стены 9.09')
Shear Walls SW1-1     15/32" Ply    27   4x8   int S5.01    86 x 9.09 / 32 x 1.1 = 26.9
Shear Walls WSW-C     7/16" OSB     14   4x8   int S5.01    42 x 9.09 / 32 x 1.1 = 13.1
Shear Walls W4B       15/32" Ply    37   4x8   int one side 118 x 9.09 / 32 x 1.1 = 36.9
```

## См. также

- [Holdowns](holdowns.md) - анкеровка SW, правило 1 к бетону и 2 через перекрытие
- [Wall Sheathing](wall-sheathing.md), [Demising Walls](../walls/demising.md)
- [Anchor Bolts](../../deck/anchor-bolts.md), [Hardware catalog](../../../reference/hardware-catalog.md)
