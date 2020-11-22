---
layout: page
permalink: /adventures/
title: Adventures
description: Books. Treks. Links.
---



{% assign sorted = site.projects | sort: 'date' | reverse %}

{% for project in sorted %}
{% if project.redirect %}
<div class="project">
    <div class="thumbnail">
        <a href="{{ project.redirect }}" target="_ blank">
        {% if project.img %}
        <img src="{{ project.img }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ project.title }}</h1>
            <!-- <br/> -->
            <p>{{ project.description }}</p>
        </span>
        </a>
    </div>
</div>
{% else %}

<div class="project ">
    <div class="thumbnail">
        <a href="{{ project.url | prepend: site.baseurl | prepend: site.url }}">
        {% if project.img %}
        <img src="{{ project.img }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ project.title }}</h1>
            <!-- <br/> -->
            <p>{{ project.description }}</p>
        </span>
        </a>
    </div>
</div>

{% endif %}

{% endfor %}

<!--books -->
<h2>Non-Fiction books</h2>
<p>Best of the books I have read (and recommend) in that corresponding year: <p>
<table cellspacing="0" cellpadding="0">
    <tr>
            <td>2019 (so far)</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.in/Art-Thinking-Clearly-Rolf-Dobelli/dp/144475954X">The Art of Thinking Clearly by Rolf Dobelli</a></td>
        </tr>
        <tr>
            <td>2018</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Structure-Scientific-Revolutions-Thomas-Kuhn/dp/0226458083">The Structure of Scientific Revolutions by Thomas S. Kuhn</a></td>
        </tr>
        <tr>
            <td>2017</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Philosophy-Jean-Paul-Sartre/dp/1400076323">The philosophy of Jean-Paul Sartre by Jean-Paul Sartre</a></td>
        </tr>
        <tr>
            <td>2016</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Sapiens-Humankind-Yuval-Noah-Harari/dp/0062316095">Sapiens: A Brief History of Humankind by Yuval Noah Harari</a></td>
        </tr>
        <tr>
            <td>2015</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Zero-One-Notes-Startups-Future/dp/0804139296">Zero to One: Notes on Startups, or How to Build the Future by Peter Thiel</a></td>
        </tr>
        <tr>
            <td>2014</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Thinking-Fast-Slow-Daniel-Kahneman/dp/0374533555">Thinking, Fast and Slow by Daniel Kahneman</a></td>
        </tr>
        <tr>
            <td>2013</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Audacity-Hope-Thoughts-Reclaiming-American/dp/0307237699">The Audacity of Hope by Barack Obama</a></td>
        </tr>
        <tr>
            <td>2012</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Surely-Feynman-Adventures-Curious-Character/dp/0393316041">Surely You're Joking, Mr. Feynman! by Richard Feynman</a></td>
        </tr>
        <tr>
            <td>2011</td>
            <td><a style="text-decoration:none" target="_blank" href="https://www.amazon.com/Brief-History-Time-Stephen-Hawking/dp/0553380168">A Brief History of Time by Stephen Hawking</a></td>
        </tr>
</table>