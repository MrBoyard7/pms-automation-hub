# 🏨 PMS Automation Hub & Channel Manager Sync Engine

A robust, production-ready asynchronous Python synchronization engine designed for multi-channel Property Management Systems (PMS). This framework automates the synchronization of multi-channel iCal feeds (Airbnb, Booking.com) with Google Workspace APIs (Calendar, Sheets) and triggers automated cleaning checklists via communication APIs based on dynamic property metadata rules.

---

## Key Features

* **Multi-Channel iCal Ingestion & Parsing:** Programmatically fetches, filters, and parses remote `.ics` schedules concurrently from multiple platforms without race conditions.
* **Google Workspace Integration:** Synchronizes processed booking events into centralized Google Calendars with dynamic color-coding and updates a master Google Sheets ledger for bookkeeping.
* **Automated Operational Dispatches:** Analyzes daily checkout matrixes and automatically maps specific messaging templates (e.g., Studio checklist vs. 4-Bedroom House workflow) to trigger operational teams via WhatsApp API mockups.
* **Production-Grade Resilience:** Complete decoupling of configuration environments, fail-safe exception handling, and standard structured logging frameworks.

---

## System Architecture & Workflow

The orchestration pipeline follows a strict modular design:
1. **Data Ingestion:** Reads localized `config/properties.json` node mappings.
2. **State Sync:** Fetches live calendar streams -> Sanitizes tokens -> Detects overlapping dates.
3. **API Dispatch:** Mirrors changes to Google Cloud Ecosystem if credentials exist.
4. **Automation Triggers:** Computes checkout tasks for the operational staff.

---

## Installation & Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/MrBoyard7/pms-automation-hub.git
cd pms-automation-hub
```

---

### 2. Install dependencies
Ensure you have Python 3.12+ installed. Install the frozen ecosystem dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables
Create a local .env file at the root directory to hold your target webhooks and authorization variables (this file is excluded from git tracking for security):

```text
WHATSAPP_API_TOKEN=your_token_here
CLEANING_TEAM_NUMBER=+1234567890
```

---

## Testing & Execution (Simulation Mode)
This framework is built with an integrated Fail-Safe Simulation Mode. If no local Google Service Account credentials (config/google_credentials.json) are detected, the system safely triggers a structural simulation loop so recruiters and developers can analyze the log outputs instantly without API lockouts.

### Run Automated Unit Tests
To validate the metadata routing mapping engine and logical config structures, execute:

```bash
python -m unittest tests/test_sync.py
```

---

### Run the Core Sync Pipeline
To execute the live data synchronization lifecycle in simulation mode:

```bash
python main.py
```

---

## Repository Structure

```text
pms-automation-hub/
│
├── config/
│   └── properties.json      # Structural JSON map for multi-property nodes
│
├── tests/
│   └── test_sync.py         # Standalone validation & component unit tests
│
├── .gitignore               # Strict exclusion matrix (caches, .env, secrets)
├── main.py                  # Core automation sync orchestration engine
├── README.md                # Technical system documentation
└── requirements.txt         # Frozen third-party production dependencies
```

---

Developed by Prince Boyard M. — Automated Systems & Network Security Engineer.