---
title: Home
---
{% include section.html full=true %}
<br>
<section 
  style="
    background-size: cover;
    background-position: center;
    padding: 1rem 1rem;
    text-align: center;
    color: #4fc067;
    align-items: center;
  "
>
  <h2 
    style="
      font-size: 3rem;
      font-weight: bold;
      margin-bottom: 1rem;
    "
  >
    <strong>BioML - Machine Learning for Life Sciences</strong>
  </h2>

 <br>
</section>

<style>
/* Override any theme container restrictions */
.container,
.wrapper {
  max-width: 90% !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* Center the two-column section on the page */
.two-column-section-index {
  display: flex;
  width: 90%;
  max-width: none;
  margin: 0 auto;  /* Center horizontally */
  padding: 0;
}

/* Keep the content wrapper full width */
.content-wrapper {
  display: flex;
  width: 100%;
  max-width: none;
  margin: 0;
  padding: 0;
}

/* LEFT COLUMN: 60% */
.left-side {
  flex: 0 0 60%;
  padding: 2rem;
  background-color: white;
  color: #000000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

/* RIGHT COLUMN: 40% */
.right-side {
  flex: 0 0 40%;
  padding: 2rem;
  background-color: white;
  color: #000000;
  display: flex;
  align-items: center;
  position: relative;
}

/* Green vertical divider (if needed) */
/* Uncomment if you want the divider back in the right column */
/*
.right-side .divider {
  width: 4px; 
  background-color: #000000;
  height: 100%;
  position: absolute;
  left: 0;
  top: 0;
}
*/

/* Image takes the full width of the right column */
.right-side img {
  width: 100%;
  height: auto;
  margin-left: 1rem;
  display: block;
}

/* Button group styling */
.button-group {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

/* Button styling */
.btn {
  display: inline-block;
  background-color: #4fc067;
  color: #ffffff;
  padding: 0.75rem 1.5rem;
  text-decoration: none;
  border-radius: 4px;
  font-size: 1.5rem;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #3ea055;
}
</style>

<section class="two-column-section-index">
  <div class="content-wrapper">
    <!-- LEFT SIDE: Title, Text, and Buttons -->
    <div class="left-side">
      <p
        style="
          font-size: 1.5rem;
          line-height: 1.6;
          max-width: 600px;
          margin: 0 auto;
          text-align: justify;
        "
      >
        The BIO-ML research group of <strong>Ghent University</strong> focusses on the 
        development of <strong>machine learning methods</strong> for the life sciences. 
        Specific research areas of interest are <strong>multi-target prediction</strong>, 
        <strong>sequence learning</strong>, <strong>time series analysis</strong>, 
        <strong>uncertainty quantification</strong> and <strong>probabilistic models</strong>. 
      </p>
<br>
<br>
      <div class="button-group">
        <a href="/bioml/research" class="btn">Our Research</a>
        <a href="/bioml/team" class="btn">Our Team</a>
        <a href="/bioml/contact" class="btn">Contact Us</a>
      </div>
    </div>
    <!-- RIGHT SIDE: Image -->
    <div class="right-side">
      <img src="images/people/collage.png" alt="Section Image" />
    </div>
  </div>
</section>

{% include section.html %}
