{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e508a7a9",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# -------------------------------------------\n",
    "# 1. INSERT THE LINK OF THE PAGE YOU WANT TO SCRAPE\n",
    "# -------------------------------------------\n",
    "url = \"YOUR_LINK_HERE\"\n",
    "\n",
    "# -------------------------------------------\n",
    "# 2. SEND GET REQUEST\n",
    "# -------------------------------------------\n",
    "headers = {\n",
    "    \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\"\n",
    "}\n",
    "\n",
    "response = requests.get(url, headers=headers)\n",
    "\n",
    "if response.status_code != 200:\n",
    "    print(\"Failed to load page:\", response.status_code)\n",
    "    exit()\n",
    "\n",
    "# -------------------------------------------\n",
    "# 3. PARSE PAGE HTML\n",
    "# -------------------------------------------\n",
    "soup = BeautifulSoup(response.text, \"lxml\")\n",
    "\n",
    "# -------------------------------------------\n",
    "# 4. FIND ALL PROPERTY CARDS\n",
    "# (You must change the CSS class names based on the website)\n",
    "# -------------------------------------------\n",
    "items = soup.select(\".property-card\")   # Example selector\n",
    "\n",
    "for item in items:\n",
    "\n",
    "    # ----- PRICE -----\n",
    "    price = item.select_one(\".price\")\n",
    "    price = price.get_text(strip=True) if price else \"N/A\"\n",
    "\n",
    "    # ----- TYPE -----\n",
    "    type_ = item.select_one(\".type\")\n",
    "    type_ = type_.get_text(strip=True) if type_ else \"N/A\"\n",
    "\n",
    "    # ----- LOCATION -----\n",
    "    location = item.select_one(\".location\")\n",
    "    location = location.get_text(strip=True) if location else \"N/A\"\n",
    "\n",
    "    # ----- SIZE / AREA -----\n",
    "    area = item.select_one(\".area\")\n",
    "    area = area.get_text(strip=True) if area else \"N/A\"\n",
    "\n",
    "    # ----- PRINT RESULTS -----\n",
    "    print(\"Price:\", price)\n",
    "    print(\"Type:\", type_)\n",
    "    print(\"Location:\", location)\n",
    "    print(\"Area:\", area)\n",
    "    print(\"-\" * 40)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
