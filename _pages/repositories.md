---
layout: page
permalink: /repositories/
title: repos
description: GitHub repositories of software and academic papers that I have written.
nav: false
nav_order: 10
---

{% if site.data.repositories.github_repos %}

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}
