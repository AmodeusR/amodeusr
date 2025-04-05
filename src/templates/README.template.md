<!-- markdownlint-disable-file MD009 MD041 -->

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Outfit&weight=500&size=52&duration=3200&pause=1000&color=F52559&center=true&vCenter=true&width=1000&height=82&lines=Ol%C3%A1+pessoas!+Como+vai%3F;Hello+everyone!+How's+it+going%3F;%E5%A7%8B%E3%82%81%E3%81%BE%E3%81%97%E3%81%A6%E3%80%81%E7%9A%86%E3%81%95%E3%82%93%EF%BC%81%E3%81%8A%E5%85%83%E6%B0%97%E3%81%A7%E3%81%99%E3%81%8B%EF%BC%9F)](https://git.io/typing-svg)

<div align="center">
{% if lang != default_lang %}
  <a href="../README.md">{{ header_langs[default_lang]}}</a>
  •
{% endif %}
{% for code, language in header_langs.items() %}
  {% if code != lang and code != default_lang %}
  {% if lang == default_lang %}
  <a href="./langs/README.{{ code }}.md">{{ language }}</a>
  {% else %}
  <a href="./README.{{ code }}.md">{{ language }}</a>
  {% endif %}
  {% if not loop.last %}•{% endif %}
  {% endif %}
{% endfor %}
</div>
&nbsp;
<div align="center">
<a href="https://github.com/amodeusr">
  <img width="47%" height="195px" alt="Amodeus' Github stats" alt="" src="https://github-readme-stats.vercel.app/api?username=amodeusr&locale={{ lang }}&count_private=true&show_icons=true&title_color=f52559&text_color=b2b2b2&bg_color=1e2025&border_color=f52559&icon_color=f52559&custom_title={{ custom_message }}" /></a>
<a href="https://wakatime.com/@AmodeusR">
  <img width="51.2%" alt="Amodeus' Wakatime stats" height="195px" src="https://github-readme-stats.vercel.app/api/wakatime?username=amodeusr&locale={{ lang }}&layout=compact&hide=text,Git%20Config,Other,Image%20%28svg%29,YAML&langs_count=8&title_color=f52559&text_color=b2b2b2&bg_color=1e2025&border_color=f52559" />
</a>
</div>

## {{ tr[lang].aboutme.title }}

{{ tr[lang].aboutme.description | join("\n\n") }}

## {{ tr[lang].knowledge.title }}

<div display="inline-block">
{% for tech in tr.techs.known %}
  <a href="{{ tech.href }}">
    <img alt="{{ tech.alt }}" src="{{ tech.src }}" width="{{ tech.size|default('38px') }}" /></a>
  {% if not loop.last %}&nbsp;{{ "\n" }}{% endif %}
{% endfor %}
</div>

<br />

[![Amodeus' frequently used languages](https://github-readme-stats.vercel.app/api/top-langs/?username=amodeusr&locale={{lang}}&layout=compact&langs_count=6&title_color=f52559&text_color=b2b2b2&bg_color=1e2025&border_color=f52559)](https://github.com/amodeusr)

## {{ tr[lang].learning.title }}

<div display="inline-block">
{% for tech in tr.techs.learning %}
  <a href="{{ tech.href }}">
    <img alt="{{ tech.alt }}" src="{{ tech.src }}" width="{{ tech.size|default('38px') }}" /></a>
  {% if not loop.last %}&nbsp;{{ "\n" }}{% endif %}
{% endfor %}
</div>

## {{ tr[lang].wantToLearn.title }}

<div display="inline-block">
{% for tech in tr.techs.willLearn %}
  <a href="{{ tech.href }}">
    <img alt="{{ tech.alt }}" src="{{ tech.src }}" width="{{ tech.size|default('38px') }}" /></a>
  {% if not loop.last %}&nbsp;{{ "\n" }}{% endif %}
{% endfor %}
</div>{{ "\n" }}
