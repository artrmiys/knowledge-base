# Page preview

This page is a quick visual check for the editor: open it locally and look at
readability, image cards, tables and links between rules. It does not
replace the working sections; it shows what a good topic page should look like.
The template is the same for the reader and the editor: it is also described in
[How to use the KB](how-to-use.md).

## Quick route

<div class="grid cards" markdown>

-   :material-floor-plan:{ .lg .middle } **Joist**

    ---

    Product family, spacing, hangers and EWP naming should be visible next to
    the images, not hidden in long text.

    [Open Joist](../work/horizontal/floor-framing/joist.md)

-   :material-format-paint:{ .lg .middle } **Interior Trims**

    ---

    Base, Crown, Casing and Door/Window Trim are best checked with rule cards:
    image + rule + what to do in the takeoff.

    [Open Interior Trims](../work/interior-trims/overview.md)

-   :material-wall:{ .lg .middle } **Exterior Wall**

    ---

    Wall height, bottom plate, shear/draft-stop notes and material variants
    should read like a checklist.

    [Open Exterior](../work/vertical/walls/exterior.md)

-   :material-clipboard-check-outline:{ .lg .middle } **QA**

    ---

    Before output, check scope, drawings, formulas, waste, FRT, hangers and
    client-specific rules.

    [Open QA checklist](quality-checklist.md)

</div>

## How a topic page should read

A topic page of the "Work" section goes in this order:

| Block | What it should contain | What it is for |
| --- | --- | --- |
| Picture at the top | A section or plan of the element itself; every part has a number, and the number is a DFL row with its unit | So the worker recognizes the element on the drawing and sees at once which row it goes to |
| `What it is` | How the element differs from its neighbor | So a Sill Plate is not mixed up with a Btm Plate |
| `Where to find it in the drawings` | Sheet, schedule, notes, details | So nobody searches for the source at random |
| `How to measure in OurPlanCore` | Tool (Line, Area, Count, J Area, Beam, Openings), what to trace, on a sheet with which point W/F/S/U; a screenshot of measuring this very element | So everybody measures the same way |
| `How to name it in the tree and the DFL row` | Takeoff name, row label, column D, formula and factor | So the macros can read the name and the number adds up |
| `Common mistakes` | What was found in reviews, with real numbers | To catch the mistake before delivery |
| `Example` | 3-6 rows of the tree or the DFL; the arithmetic adds up and matches the neighboring pages | So there is something to check your own workbook against |
| `See also` | Related pages | So a rule is not duplicated |

One rule lives on one page. If a number or a unit is needed elsewhere, put a short version and a link there, not a second wording: two wordings drift apart sooner or later.

!!! note "Main rule"
    An image must be tied to an action: what to check on the drawings and how
    it changes the takeoff/output.

## Shortcuts

| Where | Keys | What it does |
| --- | --- | --- |
| Wiki search | ++ctrl+k++ / ++cmd+k++ | Quickly find a rule by a Russian or English term. |

!!! tip "Where the full table is"
    The app's shortcuts and the key binding editor are described in one place:
    [OurPlanCore keyboard shortcuts](../reference/ourplancore-shortcuts.md).
    On a topic page, leave a link to the right scenario, so that an old
    copy of the table does not show up in search as a current instruction.

## Visual check

<details class="kb-figures kb-figures--rows" open>
  <summary>Hide 4 illustrated rules</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Joist product family</div>
      <div class="kb-figure-row__rule">Keep the exact series: <code>TJI 230</code>, <code>RED</code>, <code>LPI</code>, <code>BCI</code>.</div>
      <div class="kb-figure-row__note">The output should show which product family was specified in the schedule.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-007.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-007.png" alt="TJI joist series reference" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">O.C. spacing</div>
      <div class="kb-figure-row__rule">Spacing is measured center-to-center, not from the edge of the lumber.</div>
      <div class="kb-figure-row__note">Before the formula, check that the plan really shows 12 / 16 / 19.2 / 24 o.c.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-075.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-075.png" alt="Joist spacing diagram" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Interior Trim perimeter</div>
      <div class="kb-figure-row__rule">Base and Crown are counted by room perimeter, but exceptions have to be checked separately.</div>
      <div class="kb-figure-row__note">Kitchen cabinets, closets, garage and the room schedule can change the count.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/trims/int-trims-02.png" target="_blank" rel="noopener"><img src="../../assets/images/trims/int-trims-02.png" alt="Baseboard and crown perimeter example" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Feedback rules</div>
      <div class="kb-figure-row__rule">Corrections from the boss should go into the exact topic page, and into reference if it is a general rule.</div>
      <div class="kb-figure-row__note">That way the rule can be found later through search and does not get lost in the source map.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/reference/important-change-04.png" target="_blank" rel="noopener"><img src="../../assets/images/reference/important-change-04.png" alt="Important change reference" loading="lazy"></a>
  </figure>
</details>

## Mini checklist before delivery

- [ ] The rule is short and usable; the unit is as in column D (`LFT`, `SQ FT`, `4x8`, `pcs`).
- [ ] The formula and the example are recalculated by hand; the number matches the neighboring pages and [Formulas](../reference/formulas.md).
- [ ] The caption under a picture describes what the picture actually shows.
- [ ] Technical terms kept in English: `Joist`, `Rim Board`, `FRT`,
  `Sheathing`, `Hangers`.
- [ ] Explanations in the page language (Russian on Russian pages).
- [ ] The image has an action note: what to check and what to do.
- [ ] There is a link to related pages.
- [ ] No private data: emails, UID, salary, credentials, private links.

## See also

- [How to use the KB](how-to-use.md)
- [Images and diagrams](images-and-schemas.md)
- [Tips and key rules](../reference/boss-feedback-rules.md)
