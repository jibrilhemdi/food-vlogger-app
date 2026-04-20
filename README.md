# FeedChef 🍳

FeedChef is an AI-powered web application that helps food creators and vloggers generate content ideas based on the ingredients they have, their creator style, and current food trends. The system produces structured, ready-to-use ideas including dish concepts, creative reasoning, expected social media performance, and optimized hashtags.

This project was built for **RoyalHacks 2026** in **Copenhagen, Denmark**.

---

## 🚀 Project Overview

Food creators often struggle with deciding *what to cook* and *how to present it* for social media. FeedChef solves this by combining AI-driven creativity with structured outputs, turning simple ingredients into high-performing content ideas in seconds.

The application focuses on:
- Reliability (structured AI output)
- Speed (local AI inference)
- Practicality for real creators

---

## ✨ Features

- **Ingredient-based idea generation**  
  Generate content ideas using only the ingredients you already have.

- **Creator persona awareness**  
  Tailors ideas to different creator styles (e.g. cozy home, fine dining, viral street food).

- **Trend-aware suggestions**  
  Incorporates current food and social media trends into idea generation.

- **Structured AI output**  
  Produces clean, predictable data including:
  - Dish name
  - Creative reasoning
  - Expected likes, viewers, and followers
  - Optimized hashtags

- **Reliable AI pipeline**  
  Uses prompt templating and defensive JSON extraction to ensure stable results even when AI output is noisy.

- **Modern, minimal UI**  
  Clean, responsive frontend designed for fast interaction and clarity.

---

## 🏗 Architecture

FeedChef uses a **multi-step AI pipeline** designed for robustness and clarity.

### Frontend
- Built with **React + Vite**
- Collects user inputs (ingredients and creator persona)
- Displays structured results in a card-based layout
- Supports interactions such as copying hashtags

### Backend
- Built with **FastAPI**
- Orchestrates AI prompts and data flow
- Uses a structured prompting strategy:
  1. **Idea Generation** – creative, persona-aware content generation
  2. **Extraction & Formatting** – converts AI output into strict, structured JSON
- Applies defensive parsing to guarantee valid API responses

### AI Layer
- Uses **Qwen 3.5 4B** as the local Large Language Model
- Runs locally for fast inference and offline capability
- Combines template-driven prompts with strict JSON extraction
- Designed to tolerate imperfect or noisy LLM outputs

---

## 🧱 Frameworks

### Frontend
- **React**
- **Vite**
- **CSS (custom styling, no UI framework)**

### Backend
- **FastAPI**
- **Pydantic** (request/response validation)

---

## 🛠 Tech Stack

- **Python** – backend logic and AI orchestration  
- **FastAPI** – REST API framework  
- **Qwen 3.5 4B (Local LLM)** – idea generation and reasoning  
- **React + Vite** – frontend development  
- **HTML / CSS / JavaScript** – UI and interactions  

---

## 🏁 Hackathon

- **Event:** RoyalHacks 2026  
- **Location:** Copenhagen, Denmark  

---