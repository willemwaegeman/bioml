---
title: Tools
nav:
  order: 2
  tooltip: Software, datasets, and more
---

<section style="
  background-image: url('images/banner.jpg');
  background-size: cover;
  background-position: center;
  padding: 4rem 2rem;
  text-align: center;
  color: #4fc067;
">
  <h2 style="
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
  ">
    Tools
  </h2>

  <p style="
    font-size: 1.25rem;
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
color: #000000;
  ">
On this page you find an overview of the <strong>software packages</strong> that we 
developed. You can also download the <strong>slides</strong> of the <strong>tutorials</strong> 
that we recently orgainzed.
  </p>
</section>

{% include search-info.html %}

{% include section.html full=true %}

## Featured

{% include list.html component="card" data="tools" filters="group: featured" %}

{% include section.html full=true %}

## More

{% include list.html component="card" data="tools" filters="group: more"%}
