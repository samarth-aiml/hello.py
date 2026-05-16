{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPRhC5GJMvF2wEoPzgcF/mw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/samarth-aiml/learning.py/blob/main/day-02/project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from PIL import Image, ImageDraw\n",
        "import re\n",
        "from io import BytesIO\n",
        "\n",
        "def parse_bill_prompt(prompt):\n",
        "    \"\"\"Parses ANY: \"make Ramesh luxury shirt bill ₹2500\" → customer/items\"\"\"\n",
        "    customer_match = re.search(r'makes+([A-Za-zs]+?)(?:s+(?:luxurys+shirt|saree|bill))?', prompt, re.IGNORECASE)\n",
        "    customer = customer_match.group(1).strip().title() if customer_match else \"Customer\"\n",
        "\n",
        "    price_match = re.search(r'₹?([\\d,]+)', prompt)\n",
        "    price = int(price_match.group(1).replace(',', '')) if price_match else 5000\n",
        "\n",
        "    item = \"Luxury Shirt\" if \"shirt\" in prompt.lower() else \"Silk Saree\"\n",
        "\n",
        "    return customer, [{\"name\": item, \"price\": price}]\n",
        "\n",
        "def create_bill_image(customer, items):\n",
        "    img = Image.new('RGB', (450, 650), 'white')\n",
        "    draw = ImageDraw.Draw(img)\n",
        "\n",
        "    # Fancy header\n",
        "    draw.rectangle([10, 10, 440, 80], fill='#4B0082')\n",
        "    draw.text((30, 25), \"🧵 LUXURY SILKS PUNE 🧵\", fill='white', size=22)\n",
        "\n",
        "    # Customer\n",
        "    draw.text((30, 100), f\"Bill for: {customer}\", fill='black', size=18)\n",
        "\n",
        "    # Items\n",
        "    subtotal = sum(i['price'] for i in items)\n",
        "    gst = subtotal * 0.18\n",
        "    total = subtotal + gst\n",
        "\n",
        "    draw.text((30, 160), \"ITEM:\", fill='#4B0082', size=14)\n",
        "    draw.text((30, 190), f\"{items[0]['name']}\", fill='black', size=16)\n",
        "    draw.text((30, 230), f\"₹{subtotal:,}\", fill='black', size=20)\n",
        "\n",
        "    # Totals\n",
        "    draw.rectangle([30, 280, 420, 380], fill='#f0f0f0')\n",
        "    draw.text((40, 295), \"GST (18%):\", fill='gray', size=14)\n",
        "    draw.text((300, 295), f\"₹{gst:,.0f}\", fill='black', size=14)\n",
        "    draw.text((40, 330), \"TOTAL:\", fill='#4B0082', size=20)\n",
        "    draw.text((300, 330), f\"₹{total:,.0f}\", fill='#4B0082', size=20)\n",
        "\n",
        "    draw.text((30, 420), \"UPI: luxury.silks@pay\", fill='green', size=14)\n",
        "    draw.text((30, 450), \"WhatsApp: +91 98765 43210\", fill='blue', size=12)\n",
        "\n",
        "    # Save + preview\n",
        "    img.save('bill.png')\n",
        "    print(\"✅ 'bill.png' saved! VS Code auto-preview → WhatsApp ready!\")\n",
        "    print(f\"📄 {customer} bill: ₹{total:,.0f}\")\n",
        "\n",
        "    return img\n",
        "\n",
        "# 🔥 VS CODE RUNNER - Paste & F5\n",
        "prompts = [\n",
        "    \"make Ramesh luxury shirt bill ₹2500\",\n",
        "    \"make Priya silk saree bill ₹7500\",\n",
        "    \"make Anil banarasi saree ₹12000\"\n",
        "]\n",
        "\n",
        "for prompt in prompts:\n",
        "    print(f\"\\n--- '{prompt}' ---\")\n",
        "    customer, items = parse_bill_prompt(prompt)\n",
        "    create_bill_image(customer, items)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DLLmPf3A3jN0",
        "outputId": "14e94366-363f-4d8b-dc4f-61366c47d190"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- 'make Ramesh luxury shirt bill ₹2500' ---\n",
            "✅ 'bill.png' saved! VS Code auto-preview → WhatsApp ready!\n",
            "📄 Customer bill: ₹2,950\n",
            "\n",
            "--- 'make Priya silk saree bill ₹7500' ---\n",
            "✅ 'bill.png' saved! VS Code auto-preview → WhatsApp ready!\n",
            "📄 Customer bill: ₹8,850\n",
            "\n",
            "--- 'make Anil banarasi saree ₹12000' ---\n",
            "✅ 'bill.png' saved! VS Code auto-preview → WhatsApp ready!\n",
            "📄 Customer bill: ₹14,160\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Compound Interest Calculator - FinCAT.inc\n",
        "\n",
        "p = float(input(\"Enter your principal (₹): \"))\n",
        "\n",
        "t = float(input(\"Enter time in years: \"))\n",
        "\n",
        "r = float(input(\"Enter rate of interest (%): \"))\n",
        "\n",
        "a = p * (1 + r/100)**t\n",
        "\n",
        "ci = a - p\n",
        "\n",
        "print(f\"\\n--- FinCAT Results ---\")\n",
        "\n",
        "print(f\"Principal Amount:  ₹{p:,.2f}\")\n",
        "\n",
        "print(f\"Rate of Interest:  {r}%\")\n",
        "\n",
        "print(f\"Time Period:       {t} years\")\n",
        "\n",
        "print(f\"Final Amount:      ₹{round(a, 2):,.2f}\")\n",
        "\n",
        "print(f\"Compound Interest: ₹{round(ci, 2):,.2f}\")"
      ],
      "metadata": {
        "id": "0SpGvruIjJUp"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}