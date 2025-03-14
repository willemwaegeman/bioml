---
title: Team
nav:
  order: 3
  tooltip: About our team
---

{% include section.html %}
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
    Team
  </h2>
</section>


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

{% include section-title.html 
background="images/banner.jpg" dark=true
title="Our Former Members"
subtitle=""
%}
{%
include list.html
data="members"
component="names"
filters="role: exmember"
%}

{% include section.html %}

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
    Join Us
  </h2>

  <p style="
    font-size: 1.25rem;
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
  ">
    If you are looking for a <strong>PhD</strong> or <strong>Postdoc</strong> position,<br>
    please contact <strong>Willem Waegeman</strong>.
  </p>
</section>

<hr style="
  border: none;
  border-top: 2px solid #ccc;
  margin: 2rem 0;
  width: 100%;
">

<section style="
  background-image: url('images/banner.jpg');
  background-size: cover;
  background-position: center;
  padding: 4rem 2rem;
  text-align: center;
  color: #309379;
align-items: center;
">
  <h2 style="
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
  ">
    Funding
  </h2>

  <p style="
    font-size: 1.25rem;
    line-height: 1.6;
    max-width: 90%;
    margin: 0 auto;
align-items: center;
  ">
    Our work is made possible by funding from several organizations.
  </p>
</section>

{:.center}

{% include section.html full=true %}
{%
  include gallery-custom-size.html
  style="square"

  image1="images/institutions/flanders_ai.png"
  link1="https://www.flandersairesearch.be/en"
  tooltip1="Flanders AI"

    image2="images/institutions/ghentUniversity.png"
    link2="https://www.ugent.be/en"
    tooltip2="Ghent University"

    image3="images/institutions/fwo.png"
    link3="https://www.fwo.be/en/"
    tooltip3="Research Foundation Flanders"

%}
{% include section.html %}
<hr style="
  border: none;
  border-top: 2px solid #ccc;
  margin: 2rem 0;
  width: 100%;
">

## Thesis Students and Their Topics

Our group has had the privilege of guiding numerous thesis students through their research projects. Below is a list of these students, their thesis topics, and the year of their thesis:

(2024 – 2025)
<ul>
<li>R. Claeys - Variational inference for DTI</li>
<li>W. Welvaert - End-to-end de novo metabolomics</li>
</ul>

(2023 – 2024)
<ul>
<li>S. Jimenez - Disentangling uncertainties in Machine Learning: A comparative approach.</li>
<li>J. Cueva Villavicencio - Novel neural networks for bacterial species prediction from MALDI-TOF data</li>
</ul>

(2022 – 2023)
<ul>
<li>J.-H. Nowé - Countering illegal timbering by using multimodal machine learning</li>
<li>N. Tourne - Two-branch neural networks for predicting protein-DNA interaction</li>
</ul>


(2021-2022)
<ul>
<li>Y. Van Laere - Detection of 5mC modification in Nanopore sequencing data using deep learning</li>
<li>V. Moortgat - On Calibration of Probabilistic Multi-Class Classifiers with Hierarchical Factorization</li>
</ul>


(2020 – 2021)
<ul>
<li>E. Lorrez - Quantifying the environmental controls on African tropical forest dynamics through using a Granger causality framework</li>
<li>L. Theunissen - A comparison of flat and hierarchical classification for automatic annotation of single-cell transcriptomics data</li>
<li>T. Willaert - Improving classification by rejection of high epistemic uncertainty points</li>
<li>K. Zhang - Drug-target interaction prediction using multi-target prediction methods</li>
</ul>


(2019 – 2020)
<ul>
<li>L. Davey - Artificial neural networks to uncover features in promoter sequences responsible for nonorthogonality in E. Coli</li>
<li>B. De Saedeleer - Combatting illegal timber trade using chemical fingerprints: the power of mathematics and mass spectrometry</li>
<li>L. Pollaris - Protein secondary structure prediction using transformer networks</li>
<li>G. Tjon - Automative drinking water monitoring using flow cytometry data</li>
<li>B. Verfaillie - Pattern recognition in raman spectroscopy data for a faster labelling of subjects in multiple domains</li>
</ul>


(2018 – 2019)
<ul>
<li>K. D'haeyer - Towards a data-driven identification of the microbial "Rammanome"</li>
<li>B. De Clercq - Forecasting tidal surge in the Lower Sea Scheldt using machine learning techniques</li>
<li>G. De Clercq - Deep learning for classification of DNA functional sequences</li>
<li>N. Goeders - Fight the illegal wood trade through chemical fingerprints: The power of mathematics and mass spectrometry</li>
<li>S. Top - Vertical farming of lettuce: the influence of rhizosphere bacteria and substrates</li>
<li>M. V. Haeverbeke - Detection of m6a modifications in native RNA using Oxford Nanopore Technology</li>
</ul>


(2017 – 2018)
<ul>
<li>A. De Graeve - Detecting climate drivers for vegetation extremes</li>
<li>R. Ingels - Understanding vegetation anomalies with machine learning methods</li>
<li>M. Misonne - Prediction of RNA polymerase-DNA interactions in Escherichia Coli</li>
<li>T. Vanlerberghe - Hierarchical multi-label classification of food products</li>
</ul>


(2016 – 2017)
<ul>
<li>L. Bodyn - Exploration of deep autoencoders for collaborative filtering on cooking recipes</li>
<li>S. Decubber - Spatiotemporal optimization of Granger causality methods for climate change attribution</li>
<li>J. Heyse - Development and application of single-cell analysis tools for the study of sympatric bacterial populations</li>
<li>T. Mortier - Modeling of climate-vegetation dynamics using machine learning techniques in a non-linear Granger causality framework</li>
<li>D. Schaumont - Een integratieve benadering gebaseerd op random forest voor de verbeterde predictie van exon-intron juncties</li>
<li>X. Yin - Discovering relationships in climate-vegetation dynamics using dynamic feature selection techniques</li>
<li>C. Zhang - Visualization and unsupervised learning of flow cytometry data for bacterial identification</li>
</ul>

(2009 – 2016)
<ul>
<li>F. Ramon - A data-driven analysis of ingredients in cooking recipes</li>
<li>L. Tilleman - In silico engineering van cytochroom P450 via machine learning technieken</li>
<li>J. De Reu - Analyse van voorspellingsmodellen voor aardappelziekten en hun toepasbaarheid in Vlaanderen</li>
<li>W.K. Tsang - Assessing pathogen invasion based on community evenness and metabolic similarity</li>
<li>M. De Clercq - Prediction of ingredient combinations using machine learning techniques</li>
<li>A. De Paepe - The prediction of interaction between mRNA and miRNA using machine learning techniques</li>
<li>M. Stock - Learning pairwise relations in bioinformatics: three case studies</li>
<li>J. Vandepitte - Voorspellen van Fusarium spp. aanwezigheid en DON concentraties in wintertarwe met machine learning technieken</li>
</ul>
