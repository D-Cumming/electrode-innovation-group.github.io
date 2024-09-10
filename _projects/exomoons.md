---
layout: page
title: Exomoons
description: Searching for moons outside the Solar system
img: assets/img/exomoons/iohotspot.jpg
importance: 3
category: exomoons
related_publications: true
---

Header image: Io as imaged by JUNO from 80,000 km (NASA/JPL-Caltech/SwRI/ASI/INAF/JIRAM)

## Looking for moons around worlds beyond our Solar system

I've been interested in the possibility of detecting exomoons, both directly through their thermal radiation, and indirectly through their effect on sculpting the circumplanetary disk during their formation (see [my research on J1407b](projects/j1407b) which may be indirect evidence of exomoon sculpting in action).

A paper by Peters-Limbach and Turner in 2013 titled [On the Direct Imaging of Tidally Heated Exomoons](https://ui.adsabs.harvard.edu/abs/2013ApJ...769...98P/abstract) (THEMs) suggested that, for nearby exoplanet systems with multiple moons in resonance, there could be a tidally heated exomoon that could be directly imaged at thermal infrared wavelengths - think Io, the tidally heated moon of Jupiter, that has sulphur volcanoes.

Building on the original paper, Elina Kleisioti has been investigating the tidal heating properties of exomoons using more realistic models of the internal structure and heat flow within them.

<div class="row mt-2">
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/exomoons/moon_structure.png" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/exomoons/heat_models.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="caption">
Interior structure of an exomoon and flowchart of the heat in the model {% cite 2023A&A...675A..57K %}.
</div>

In order to see the thermal emission from a THEM, the exoplanet system has to be very close to the Solar system, and you also need to make sure that the gas giant exoplanet that the exomoon is orbiting around has cooled off: it's entirely possible that for a gigayear old system, the exoplanet can be fainter than the tidally heated exomoon at some wavelengths!

Since multiple moons are present around all the gas giant exoplanets in our system, it seems reasonable that there are exomoons elsewhere in the Universe.

We then chose a suitably nearby exoplanet that was orbiting far enough from its parent star that we had a chance of separating the light from the exoplanet/moon system, and ϵ Eridani fits the bill quite nicely. Elina carried out a study for what a THEM around this exoplanet would look like
{% cite 2023A&A...675A..57K %}.


<div class="row mt-2">
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/exomoons/them_spectrum.png" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/exomoons/them_e_versus_a.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="caption">
The spectral energy distribution for exomoone around Epsilon Eridani b, showing that a large exomoon can be brighter than the exoplanet, and a plot with the expected temperature of the exomoon as a function of orbital eccentricity and semimajor axis {% cite 2023A&A...675A..57K %}.</div>


Elina worked together with then Masters studen Quirijn van Woerkom to look at the spectroastrometric detectability of nearby Solar System-like exomoons {% cite 2024A&A...684A..72V %}. By using a spectrograph they showed that an additional astrometric shift should be possible to detect.

THEMs have to be close to their parent exoplanet in order to have strong tidal heating, and there is a non-negligible probability that the exomoon might transit the exoplanet, providing distinctive eclipses that could be seen by photometric monitoring of the exoplanet.... but then Elina pointed out that we don't need to have the exomoon transit at all! Instead, if there is an active volcano on the tidally locked side of the exomoon facing the exoplanet, then the volcano appearing and disappearing on modestly inclined orbits provides an additional detection opportunity for exomoons {% cite 2024A&A...687A.125K %}.

<div class="row mt-2">
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/exomoons/exomoon_modulation.png" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/exomoons/exomoon_detectability.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="caption">
The light curve of a tidally locked exomoon with a volcano on the exoplanet facing side, and the detectability rate for a tidally locked exomoon for different hotspot temperatures and orbital periods. Aliasing with the exoplanet's rotation period causes changes in detection rate {% cite 2024A&A...687A.125K %}.</div>

