# backend/app/utils/cleaner.py

import re
from bs4 import BeautifulSoup, Comment


def clean_html_for_design_replication(raw_html: str) -> str:
    """
    Cleans raw HTML to remove unnecessary scripts, styles, ads, and analytics,
    while preserving the overall structure and essential styles for design replication.
    """

    # Parse with BeautifulSoup
    soup = BeautifulSoup(raw_html, "html.parser")

    # 1️⃣ Remove all <script> tags
    for script in soup.find_all("script"):
        script.decompose()

    # 2️⃣ Remove all <style> tags (optional)
    # for style in soup.find_all("style"):
    #     style.decompose()

    # 3️⃣ Remove tracking <link> tags (analytics or unnecessary fonts)
    for link in soup.find_all("link"):
        rel = link.get("rel")
        href = link.get("href", "")
        if rel and ("stylesheet" in rel or "icon" in rel):
            continue  # Keep CSS and favicon
        link.decompose()

    # 4️⃣ Remove inline JS event handlers (onclick, onload, etc.)
    for tag in soup.find_all(True):
        attrs_to_remove = []
        for attr in tag.attrs:
            if attr.startswith("on"):  # onload, onclick, etc.
                attrs_to_remove.append(attr)
        for attr in attrs_to_remove:
            del tag.attrs[attr]

    # 5️⃣ Remove analytics and ad-related IDs or classes
    for tag in soup.find_all(True):
        class_list = tag.get("class", [])
        id_attr = tag.get("id", "")
        keywords = ["ad", "ads", "advertisement", "tracker", "analytics"]
        if any(kw in id_attr.lower() for kw in keywords):
            tag.decompose()
        if any(kw in " ".join(class_list).lower() for kw in keywords):
            tag.decompose()

    # 6️⃣ Remove comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Optional: collapse excessive whitespace
    cleaned_html = re.sub(r'\s+', ' ', str(soup))

    return cleaned_html.strip()
