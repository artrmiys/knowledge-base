# Картинки и схемы

Шаблоны, как вставлять картинки и схемы единообразно. Это конструкторская
шпаргалка — визуала будет много, поэтому держим все вставки в одном стиле.

## Куда класть файлы

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

- Раскладка по папкам = по разделу wiki, чтобы не превратилось в свалку.
- Имена файлов: латиница, нижний регистр, тире (`exterior-2x6-section.png`).
- PNG/SVG для схем, JPG/WEBP для фото. Свыше 500 KB — по возможности ужимать.

## Одна картинка с подписью

```markdown
<figure markdown>
  ![Wall section, exterior 2×6](../assets/images/walls/exterior-2x6-section.png)
  <figcaption>Exterior 2×6 wall — typical section</figcaption>
</figure>
```

<figure markdown>
  ![Заглушка](../assets/images/logo.png){ width="120" }
  <figcaption>Так выглядит figure + figcaption.</figcaption>
</figure>

## Две колонки: текст слева — схема справа

```markdown
<div class="kb-split" markdown>

Текстовая часть: правила, bullets, таблицы.

<figure markdown>
  ![alt](../assets/images/your-schema.png)
  <figcaption>Подпись.</figcaption>
</figure>

</div>
```

## Ряд миниатюр (галерея)

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

## Большая схема на всю ширину

```markdown
<div class="kb-schema-full">
  ![Roof framing — full schema](../assets/images/roof/full-schema.png)
</div>
```

## Картинка внутри admonition-блока

```markdown
!!! note "Смотри схему"
    <figure markdown>
      ![alt](../assets/images/some-detail.png)
      <figcaption>Деталь — где смотреть.</figcaption>
    </figure>
```

## Правила оформления

- Каждой схеме — короткая подпись (что, где смотреть, какой проект).
- Если схема из конкретного проекта — добавь номер проекта в подпись и не
  публикуй приватные части (имена клиентов, цены, личные данные).
- Не вставляй скриншоты с полем «Email/UID/Password» — обрезай до содержания.
- Большие PDF не вставляй картинкой — лучше отдельной страницей с pdf.js или
  ссылкой на raw-файл.
