# Images and diagrams

Templates for inserting images and diagrams consistently. This is an estimator's
cheat sheet - there will be a lot of visuals, so we keep all inserts in one style.

## Where to put files

```
docs/
└── assets/
    └── images/
        ├── walls/
        │   ├── exterior-2x6-section.png
        │   └── ...
        ├── framing/
        ├── roof/
        └── hangers/
```

- Folder layout = wiki section, so it does not turn into a dump.
- File names: Latin letters, lowercase, hyphens (`exterior-2x6-section.png`).
- PNG/SVG for diagrams, JPG/WEBP for photos. Over 500 KB - compress if possible.

## One image with a caption

```markdown
<figure markdown>
  ![Wall section, exterior 2×6](../assets/images/walls/exterior-2x6-section.png)
  <figcaption markdown="span">Exterior 2×6 wall - typical section</figcaption>
</figure>
```

<figure markdown>
  ![Placeholder](../assets/images/logo.svg){ width="120" }
  <figcaption markdown="span">This is what figure + figcaption looks like.</figcaption>
</figure>

## Two columns: text on the left, diagram on the right

```markdown
<div class="kb-split" markdown>

Text part: rules, bullets, tables.

<figure markdown>
  ![alt](../assets/images/your-schema.png)
  <figcaption markdown="span">Caption.</figcaption>
</figure>

</div>
```

## Row of thumbnails (gallery)

```markdown
<div class="kb-gallery">

  <a class="kb-gallery__item" href="../assets/images/walls/exterior.png">
    <img src="../assets/images/walls/exterior.png" alt="Exterior wall">
    <div class="kb-gallery__caption">Exterior wall</div>
  </a>

  <a class="kb-gallery__item" href="../assets/images/walls/corridor.png">
    <img src="../assets/images/walls/corridor.png" alt="Corridor wall">
    <div class="kb-gallery__caption">Corridor wall</div>
  </a>

</div>
```

## Large full-width diagram

```markdown
<div class="kb-schema-full">
  ![Roof framing - full schema](../assets/images/roof/full-schema.png)
</div>
```

## Image inside an admonition block

```markdown
!!! note "See the diagram"
    <figure markdown>
      ![alt](../assets/images/some-detail.png)
      <figcaption markdown="span">Detail - where to look.</figcaption>
    </figure>
```

## Formatting rules

- Every diagram gets a short caption (what it is, where to look, which project).
- The caption describes what the picture actually shows: the same elements, names,
  sizes and numbers. If the frame shows something else (another sheet, another size,
  no promised frame or detail), change the picture or the caption instead of leaving it.
- A diagram never contradicts the text of its page: its row labels and units are the
  same as in the DFL table of that page (`LFT`, `SQ FT`, `4x8`, board length).
- If the diagram is from a specific project, add the project number to the caption and do not
  publish private parts (client names, prices, personal data).
- Do not insert screenshots with an "Email/UID/Password" field - crop to the content.
- Do not insert large PDFs as an image - a separate page with pdf.js or a
  link to the raw file is better.
