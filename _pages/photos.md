---
layout: page
permalink: /photos/
title: Work Photos
---
<style>
  body {
    background-color: #fafaf8;
  }
  /* .content {
    text-align: justify;
  } */
</style>


<style>
  .ggrid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
  }
  .ggrid img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 12px;
    display: block;
    cursor: zoom-in;
  }

  /* Lightbox (no extra panel/background, no scrollbars) */
  dialog#lightbox {
    border: 0;
    padding: 0;
    background: transparent;
    box-shadow: none;
    width: fit-content;
    height: fit-content;
    max-width: 96vw;
    max-height: 92vh;
    overflow: visible;
  }
  dialog#lightbox::backdrop {
    background: transparent; /* change to rgba(0,0,0,0.65) if you want a dim overlay */
  }
  #lightbox-img {
    display: block;
    width: auto;
    height: auto;
    max-width: 96vw;
    max-height: 92vh;
    border: 4px solid #000;
    box-sizing: border-box;
    cursor: zoom-out;
  }
</style>

<div class="ggrid">
  {% for p in site.data.my_album.photos %}
    <img
      loading="lazy"
      src="{{ p.thumb | default: p.url }}"
      data-full="{{ p.full | default: p.url }}"
      alt="">
  {% endfor %}
</div>

<dialog id="lightbox">
  <img id="lightbox-img" alt="">
</dialog>

<script>
  (function () {
    const dlg = document.getElementById('lightbox');
    const img = document.getElementById('lightbox-img');

    document.querySelectorAll('.ggrid img').forEach(el => {
      el.addEventListener('click', () => {
        img.src = el.dataset.full || el.src;
        dlg.showModal();
      });
    });

    // Close on click anywhere (image/backdrop) and Escape
    dlg.addEventListener('click', () => dlg.close());
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && dlg.open) dlg.close();
    });
  })();
</script>
