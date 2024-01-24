---
layout: archive
title: "Puslanef"
permalink: /publications/
author_profile: true
---
AAAAAAAAAAAAAYES

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/citations?user=wnkr0FYAAAAJ&hl=en}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
