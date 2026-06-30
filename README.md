# CDAC C-CAT Mock Test 🎯

> **Free, browser-based mock exams for C-CAT 2026 — no login, no install, just practice.**

[![Live Site](https://img.shields.io/badge/🔗_Live_Site-wamiquemohd.github.io-4CAF50?style=for-the-badge)](https://wamiquemohd.github.io/cdac-ccat-practice-sets/)
[![Sets Available](https://img.shields.io/badge/Practice_Sets-7_Available-2196F3?style=for-the-badge)](#practice-sets)
[![No Login](https://img.shields.io/badge/Access-No_Login_Required-FF9800?style=for-the-badge)](#how-to-use)

*Built and maintained by **Mohd Wamique (ex-CDACian)*** — someone who's been through the exam and wants to make your prep easier.

---

## What is C-CAT?

The **C-CAT (C-DAC Common Admission Test)** is a national-level entrance exam for admission to C-DAC's PG Diploma programmes — **PG-DAC**, **PG-DBDA**, **PG-DITISS**, **PG-DESD**, **PG-DVLSI**, **PG-DIoT**, and more.

| Section | Topics | Time |
|---------|--------|------|
| **A** | English, Quant, Reasoning | 1 hr |
| **B** | C, Data Structures, OOP, OS, Networking, Big Data & AI | 1 hr |
| **C** | Digital Electronics, Microprocessors, Embedded Systems *(DESD/DVLSI/DIoT only)* | 1 hr |

**Marking:** +3 for correct, −1 for wrong, 0 for skipped.

---

## Practice Sets

Seven sets, progressively harder — start at your level and push up.

| # | Set | Difficulty | Sections | Questions | Time |
|---|-----|-----------|----------|-----------|------|
| 1 | Practice Set 1 | 🟢 Normal | A + B | 100 | 2 hrs |
| 2 | Practice Set 2 | 🟡 Advanced | A + B | 100 | 2 hrs |
| 3 | Practice Set 3 | 🟠 Advanced + C | A + B + C | 150 | 3 hrs |
| 4 | Practice Set 4 | 🟡 Advanced | A + B | 100 | 2 hrs |
| 5 | Practice Set 5 | 🟡 Advanced | A + B | 100 | 2 hrs |
| 6 | Practice Set 6 | 🔴 Advanced Pro | A + B | 100 | 2 hrs |
| 7 | Practice Set 7 | 🔥 Hardest | A + B | 100 | 2 hrs |

All sets include:
- Reading Comprehension passages (Cloud, Neural Networks, AI Ethics)
- Big Data & AI questions (Hadoop, MapReduce, Spark, ML)
- Section C (Set 3) covers: Digital Electronics, 8085/8086, Embedded C, RTOS, ARM, I2C/SPI/UART/CAN, IoT

---

## Features

| Feature | Details |
|---------|---------|
| ⏱ **Timed sections** | 60-minute countdown per section, auto-submit on timeout |
| 🎨 **Question palette** | Colour-coded: Not Visited / Not Answered / Answered / Marked |
| 📊 **Results breakdown** | Score, section-wise analysis, time spent, full solutions |
| 📄 **PDF export** | Save your results as a printable report |
| 🔒 **Answer protection** | XOR + Base64 encoded keys; DevTools detection during exam |
| 📱 **Mobile friendly** | Works on phones and tablets — no app needed |
| 💾 **Mid-exam save** | Refreshing won't lose your progress |
| 🏷️ **Nickname** | Personalise your exam session and result card |

---

## How to Use

1. Go to **[wamiquemohd.github.io/cdac-ccat-practice-sets](https://wamiquemohd.github.io/cdac-ccat-practice-sets/)**
2. Pick a Practice Set (start with Set 1 if you're new, jump to Set 6–7 to stress-test yourself)
3. Enter your nickname
4. Attempt Section A → Section B (→ Section C for Set 3)
5. View your detailed results and download the PDF

No signup. No ads. Works entirely offline after the page loads.

---

## Tech Stack

- **Single-file** HTML/CSS/JS — no frameworks, no build tools, no dependencies
- Hosted on **GitHub Pages** (free, forever)
- Results submitted via **Formspree**
- Questions encoded and bundled by `generate.py` (Python 3)

```
├── index.html      ← The complete exam (all 7 sets, all logic, ~274 KB)
├── generate.py     ← Rebuilds index.html from question data + templates
└── README.md
```

To rebuild after editing questions:

```bash
python3 generate.py
```

---

## Disclaimer

Unofficial practice resource for educational purposes. Questions are based on the publicly known C-CAT syllabus — not sourced from official C-DAC papers. For official info, visit [cdac.in](https://www.cdac.in).
