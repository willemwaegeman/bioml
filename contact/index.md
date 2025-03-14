---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
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
    Contact
  </h2>

  <p style="
    font-size: 1.5rem;
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
color: #000000;
  ">
Our lab is part of the <a href="https://kermit.ugent.be/index.php">Kermit Research Unit</a>, at the faculty of <a href="https://www.ugent.be/bw/en">Bioscience Engineering</a> of Ghent University.


  </p>
</section>
{%
  include link.html
  type="email"
  icon=""
  text="willem.waegeman@ugent.be"
  tooltip=""
  link="willem.waegeman@ugent.be"
  style="button"
%}
{%
  include link.html
  type="phone"
  icon=""
  text="(+32) 9 264.92.00"
  tooltip=""
  link="+32-92649200"
  style="button"
%}
{%
  include link.html
  type="address"
  icon=""
  text="Google Maps"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://www.google.com/maps/dir//Coupure+Links+653,+9000+Gent/@51.0527795,3.7067699,17z/data=!4m9!4m8!1m0!1m5!1m1!1s0x47c3716be33c0fdb:0x13de981a81d5c757!2m2!1d3.7087226!2d51.053703!3e0?hl=nl"
  style="button"
%}
{:.center}

{% include section.html %}

<!---
### <i class="fas fa-mail-bulk"></i>Mailing Address
-->

Ghent University
Department of Data Analysis and Mathematical Modelling
Coupure Links 653  
9000 Ghent
Belgium
{:.center}

{% capture col1 %}
{%
  include figure.html
  image="images/coupure_2.jpg"
  caption="Campus Coupure"
width=300

%}
{% endcapture %}
{% capture col2 %}
{%
  include figure.html
  image="images/coupure_3.jpg"
  caption="Campus Coupure"
width=300

%}
{% endcapture %}


{%
include figure.html
image="images/coupure_3.jpg"
caption="Campus Coupure"
width=300

%}