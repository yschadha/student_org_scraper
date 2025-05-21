# student_org_scraper

Python Web Scraper for UCLA Registrar: Club Outreach Tool

As part of Adoptimal’s outreach strategy, I built a custom Python-based web scraper designed to extract detailed data from the UCLA Registrar’s official student organization directory. The goal of this tool is to automate the discovery of active clubs on campus that businesses can partner with through the Adoptimal platform.

What It Does
The scraper navigates UCLA’s publicly available registrar site, specifically the student organizations search portal, and collects key information for each club. This includes:

Club Name

Organization Type (e.g., fraternity, academic, cultural, service)

Category

Description or Mission Statement

Primary Contact Info (when available)

Date Founded

Link to Social Media or Club Page

This data is parsed, cleaned, and structured into a usable format (e.g., CSV or JSON), which I then import into our backend database to populate club listings or feed into outreach pipelines.

How It Works: Tech Breakdown
Python 3: The main programming language used to build the scraper.

Selenium: Used to automate interaction with the dynamic content on the registrar page. This was necessary because the site uses JavaScript to load data as you scroll.

BeautifulSoup: For parsing and extracting HTML elements like divs, spans, and links once the content has fully loaded.

Chrome WebDriver (managed with webdriver_manager): Runs headlessly to simulate browsing and automate scroll-to-load functionality.

Time + Regex: For wait control and cleaning up unstructured or malformed dataWhy It Matters
This scraper is a critical part of our lead generation process. Rather than manually visiting the registrar page and copying info one club at a time, we can now:

Scrape hundreds of clubs in minutes

Identify high-engagement categories (e.g., business, cultural, or Greek life)

Feed the data into outreach workflows or AI agents that can enrich it with Instagram handles, email contacts, and engagement stats

Eventually, we plan to integrate this scraper directly into our n8n automation workflows so it can run on a schedule and update our club database continuously.

In short: This Python scraper automates the labor-intensive process of discovering and cataloging student organizations at UCLA—giving Adoptimal a powerful edge in scaling outreach and onboarding the right partners for campus-based advertising.







