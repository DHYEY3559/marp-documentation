---
marp: true
title: Product Documentation — Example
author: Dhyey Pithadia
theme: gaia
paginate: true
class: lead
---

<!--
  Custom theme CSS (scoped to this deck)
  You may adjust fonts/colors here.
-->
<style>
section {
  font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  color: #0f172a;
}

/* Header style */
h1, h2, h3 {
  color: #0b5ed7;
  font-weight: 700;
}

/* Footer/page number */
footer {
  font-size: 12px;
  color: rgba(0,0,0,0.6);
  text-align: center;
  padding-top: 8px;
}

/* Custom class for code blocks */
pre code {
  font-size: 0.9rem;
  line-height: 1.3;
}

/* Highlight panel */
.note {
  border-left: 4px solid #0b5ed7;
  padding: 8px 12px;
  background: rgba(11,94,215,0.06);
  border-radius: 6px;
}

/* Mobile tweak */
@media (max-width: 800px) {
  section { font-size: 18px; }
}
</style>

---

# Product Documentation Overview

**Contact:** 23f2001472@ds.study.iitm.ac.in

- Maintainable in Git (Markdown)  
- Exportable to HTML/PDF/PPTX with Marp CLI  
- Uses a small custom theme & directives  

<!-- _footer: "Product Docs • v1.0" -->
<!-- _header: "**Product Documentation**" -->

---

![bg fit](assets/architecture-bg.jpg)

# Architecture & Design  
<!-- _class: center, middle -->

> Visual overview of the product architecture.

<div class="note">
This slide uses a **background image** located at:<br>
`assets/architecture-bg.jpg`
</div>

---

## API Example

```javascript
// sample API request
fetch('/api/v1/items', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({name: 'Item A'})
})
.then(r => r.json())
.then(console.log)
```

---

## Algorithmic Complexity (math)

Block complexity (Big-O):

$$
T(n) = 2T(n/2) + n \quad\Rightarrow\quad T(n) = \Theta(n \log n)
$$

Inline math: $O(n \log n)$

---

## Release Notes

- v1.0 — Initial stable release  
- v1.1 — Performance improvements  

---

## Speaker Notes (example)

Notes:  
- Walk through architecture  
- Show API request example  
- Explain the complexity analysis  

---

# Appendix — Local Build

To export:

```bash
# HTML
marp slides.md -o slides.html

# PDF
marp slides.md --pdf

# PPTX
marp slides.md --pptx
```

---

<footer>Contact: 23f2001472@ds.study.iitm.ac.in • Product Docs</footer>
