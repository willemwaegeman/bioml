---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

At this moment our team consists of the following members. 

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: programmer"
%}
{:.center}

{% include section.html background="images/banner.jpg" dark=true%}

Former PhD students: Laure Van Den Bulcke, Friederike Mey, Jim Clauwaert, Peter Rubbens, Christina Papagiannopoulou, Michiel Stock

{% include section.html %}

## Join

#### If you are looking for a PhD or postdoc position, please contact Willem Waegeman

## Funding

Our work is made possible by funding from several organizations.
{:.center}

{%
  include gallery.html
  style="square"

  image1="images/ai_flanders_logo_300.png"
  link1="https://www.flandersairesearch.be/en"
  tooltip1="Flanders AI"

%}

## Thesis Students and Their Topics

Our group has had the privilege of guiding numerous thesis students through their research projects. Below is a list of these students, their thesis topics, and the year of their thesis:

<ul>
<li>J.-H. Nowé - Countering illegal timbering by using multimodal machine learning (2022 – 2023)</li>
<li>N. Tourne - Two-branch neural networks for predicting protein-DNA interaction (2022 – 2023)</li>
<li>Y. Van Laere - Detection of 5mC modification in Nanopore sequencing data using deep learning (2021 – 2022)</li>
</ul>
