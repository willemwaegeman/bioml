---
title: Research
nav:
  order: 1
  tooltip: Published works
---

# <i class="fas fa-microscope"></i>Research


{% capture text %}


{%
  include link.html
  link="research"
  text="See what we've published"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/research2.png"
  link="research"
  title="Multi-target prediction"
  text=text
%}

{% capture text %}
In addition to publishing scientifc papers, we also develop software that is freely available on Github. 

{%
  include link.html
  link="tools"
  text="Browse our tools"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/software.jpg"
  link="resources"
  title="Our Resources"
  flip=true
  text=text
%}

{% capture text %}
We are a small but dedicated team and our members have complementary expertise in data science, computer science, mathematics, physics, engineering and biology. 

{%
  include link.html
  link="team"
  text="Meet our team"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  text=text
%}

{% capture text %}
At Ghent University, we are responsible for teaching several courses to bachelor and master students. We organize courses in mathematics and machine learning.   

{%
  include link.html
  link="teaching"
  text="See our courses"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/our_research.jpg"
  link="resources"
  title="Our Courses"
  flip=true
  text=text
%}



**Multi-target prediction**
<br>
This is an umbrella-term that comprises various complex machine learning settings, such as multi-label classification, multivariate regression, pairwise learning, dyadic prediction, matrix completion, zero-shot learning, etc. Together with other researchers, Willem Waegeman has organized many tutorials and workshops on multi-target prediction in the last ten years, and he has published numerous papers on this topic. It is also the topic he is most often talking about in invited lectures. Currently, the research focus is on the development of a flexible Auto-ML software package for various multi-target prediction problems.

**Sequence models and time series analysis**
<br>
This is a research line that was started five years ago, and that has been expanded since then. Specific interests include sequence labelling, autoregressive models, time series forecasting, causal inference in time series, feature learning for sequential data and spatio-temporal problems.

**Uncertainty quantification and probabilistic modelling** 
<br>
This is a research line that was started ten years ago, with, at that stage, a focus on Bayes-optimal inference from probabilistic models. Recently, the interests have been extended to topics such as quantifying epistemic and aleatoric uncertainty, classifier calibration, set-valued prediction, prediction intervals, conformal prediction, open-set recognition and out-of-distribution detection.  

**Applications in the life sciences**
<br>
Over the last decade, the research focus has been on developing machine learning solutions for all sorts of -omics data. This includes genomics, epigenomic, transcriptomics and proteomics data, as well as specific phenotyping technologies, with applications in environmental sciences and medicine. One large project also involved the analysis of climate time series. 

{% include section.html %}

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" %}
