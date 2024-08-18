---
layout: page
title: ASASSN-21js
description: A multi-year transit of a ringed disc
img: assets/img/asassn21js/21js_banner.png
importance: 9
category: exorings
related_publications: true
---


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/ASASSN-21js_final_video.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>

<div class="caption">
    Animation of the ASASSN-21js light curve along with the fitted model {% cite 2024A&A...688L..11P %}. Animation by T. Pramono.
</div>

I’ve been looking at the light curves that the [ASAS-SN survey](https://www.astronomy.ohio-state.edu/asassn/index.shtml) releases on their [transients page](https://www.astronomy.ohio-state.edu/asassn/transients.html) - these are light curves that show curious dimmings caused by stellar variability or by something moving in front of the star. One of these light curves, named ASASSN-21js, showed a sudden dimming in 2021, and over the past three years, has faded and then brightened up again. Theo worked on analyzing this light curve with me as a Masters thesis project here in Leiden: after some experimentation, the light curve is exactly matched by a highly tilted and inclined disk with two rings with different transmissions. What’s particularly impressive is that the residuals after the model fit are consistent with noise. This model explains the data almost perfectly.

<div class="row mt-2">
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/asassn21js/onetwodiscs.png" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-2 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/asassn21js/21jsmodels.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="caption">
photometry of the star showing model fits with a single disk, a ring and a double ring system model. The double ring system model works the best, and an image of a star moving behind a tilted ring/disk system, showing the light curve geometry at different parts of the eclipse. When the star moves behind the ring edges, the light curve changes shape.
</div>

Using a MCMC fitting package, he was able to determine the confidence intervals on the parameters, with the outermost ring about 1.12 au in radius. Due to the geometry of the eclipse, we only see these two rings - there may be more material interior to this radius, but the star’s motion will not reveal this. What’s more amazing is that the eclipse is still ongoing, finishing only in May 2027!

Okay, so what are the challenges here? First, the star itself is very large star with a mass of 4.5 times that of the Sun. Those are relatively rare, but are seen long distances across the Galaxy. Second, the transverse velocity is less than one kilometre per second! If this is orbiting around this star, then it’s at a distance of over 13000 au from the star! Deep into Oort Cloud territory. This means that the chance of seeing such an eclipse is tiny, around one in ten thousand for all the solar type stars in the ASAS-SN survey size and duration. That’s an uncomfortable problem and we don’t know the answer as to why we’re seeing this now.

What’s tantalizing is that the MCMC fitting also found solutions with a cleared ring gap between the two main rings (squint at around 59200 days to see this additional gap in the rings). It’s compelling, but not confirmed. There is also multi band data coming in as well, so in future research we can see if the material is sub-micron sized or not. More of these unusual systems are being discovered in ASAS-SN, and with other large survey telescopes coming online soon (think the [Vera C. Rubin Observatory](https://rubinobservatory.org/)) many more of these systems might be discovered.

