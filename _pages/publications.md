---
layout: page
permalink: /publications/
title: Publications
description: Patents and Publications in reversed chronological order.
years: [2023, 2020, 2019, 2018]
---

{% for y in page.years %}
  <h3 class="year">{{y}}</h3>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

<h2 style="color:#9b0000;">Service</h2>
<ul>
          <li>Artifact Evaluation committee member: <ul> 
            <li> <a href="https://sysartifacts.github.io/organizers.html"><u>27th ACM Symposium on Operating Systems Principles (SOSP) 2019</u></a></li>
            <li><a href="https://asplos-conference.org/calls/#artifacts"><u>25th ACM Architectural Support for Programming Languages and Operating Systems (ASPLOS) 2020</u></a></li>
        </ul> </li>
        <li>Review committee member: HPE TechCon 2020</li>
        <li>Invited speaker: <a href="https://www.virtueinsight.com/technology/Blockchain-2019/"> Virtue insight Blockchain 2019 conference -- How GDPR is a double edged sword for Blockchain</a>, HPE TechCon 2019 -- Preemptive compatibility failure detection using graph structure learning in datacenters, HPE Software Defined Cloud Group Technical Symposium -- Generic DMTF Redfish device management in datacenters</li>
        <li>Open source contributions: Apache Ratis, Postgresql and YCSB</li>
        <li>Technical reviewer of the book <a href="http://www.informit.com/store/effective-cybersecurity-a-guide-to-using-best-practices-9780134772806">"Effective Cybersecurity: A Guide to Using Best Practices and Standards"</a> by <a href="http://williamstallings.com/">Dr. William Stallings</a> released on June 2018 (Acknowledged in Preface).</li>
</ul>