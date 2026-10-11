# Capital Management Copilot

## Project Vision

Build a Python-based Capital Management platform capable of:

- Modelling a simplified universal bank
- Loading a granular balance sheet
- Calculating regulatory capital metrics
- Calculating RWA consumption
- Projecting NII and earnings
- Performing capital planning
- Simulating balance-sheet scenarios
- Performing liquidity and IRRBB analysis
- Evaluating shareholder value creation
- Supporting CFO, Treasury and Capital Management decisions
- Providing AI-driven natural language explanations

---

# Architecture

Exposure Master
        ↓
Balance Sheet Engine
        ↓
Risk Engines
(Credit / Market / CVA)
        ↓
RWA Engine
        ↓
NII Engine
        ↓
Net Income Engine
        ↓
Capital Planning
        ↓
CET1 / Tier1 / TCR
        ↓
SVA Analysis
        ↓
AI Copilot

---

# Phase 1 - Project Setup

## Repository Setup

- [x] Create GitHub repository
- [x] Clone repository locally
- [x] Create Python virtual environment
- [x] Install dependencies
- [x] Create project structure
- [x] Push initial commit

## Folder Structure

- [x] Create app/
- [x] Create data/
- [x] Create docs/
- [x] Create engine/
- [x] Create models/
- [x] Create tests/

## Initial Dataset

- [x] Create exposure_master_golden_dataset.csv
- [x] Create data_dictionary.txt
- [ ] Implement CSV loader
- [ ] Implement data validation rules
- [ ] Load dataset into Pandas DataFrame

---

# Phase 2 - Balance Sheet Engine

## Core Classes

- [ ] Create Exposure class
- [ ] Create BalanceSheet class
- [ ] Create Portfolio class
- [ ] Create Bank class

## Exposure Loader

- [ ] Read exposure_master_golden_dataset.csv
- [ ] Validate schema
- [ ] Validate mandatory fields
- [ ] Handle missing values

## Balance Sheet Construction

- [ ] Aggregate assets
- [ ] Aggregate liabilities
- [ ] Aggregate capital instruments
- [ ] Calculate total assets
- [ ] Calculate total liabilities
- [ ] Calculate total equity
- [ ] Perform balance sheet consistency check

## Reporting

- [ ] Asset breakdown by portfolio
- [ ] Liability breakdown by portfolio
- [ ] Product mix analysis
- [ ] Country analysis
- [ ] Sector analysis

---

# Phase 3 - Credit Risk Engine

## Expected Loss

- [ ] Calculate EAD
- [ ] Calculate Expected Loss

Formula:

EL = PD × LGD × EAD

## Aggregation

- [ ] EL by business unit
- [ ] EL by country
- [ ] EL by sector
- [ ] EL by rating
- [ ] EL by portfolio

## Outputs

- [ ] expected_loss_results.csv

---

# Phase 4 - RWA Engine

## Credit RWA

- [ ] Calculate exposure-level Credit RWA

Formula:

Credit RWA = Carrying Value × Risk Weight

## Aggregation

- [ ] Retail RWA
- [ ] Corporate RWA
- [ ] Treasury RWA
- [ ] Markets RWA
- [ ] Total Credit RWA

## Outputs

- [ ] rwa_results.csv

---

# Phase 5 - Capital Engine

## Regulatory Capital Extraction

- [ ] CET1 extraction
- [ ] AT1 extraction
- [ ] Tier2 extraction

## Capital Metrics

- [ ] CET1 Ratio
- [ ] Tier1 Ratio
- [ ] Total Capital Ratio
- [ ] Leverage Ratio
- [ ] RWA Density

## Supporting Metrics

- [ ] Capital surplus
- [ ] Capital deficit
- [ ] Buffer consumption
- [ ] Distance to target CET1

## Unit Tests

- [ ] CET1 Ratio tests
- [ ] Tier1 Ratio tests
- [ ] Total Capital Ratio tests
- [ ] Capital planning tests

---

# Phase 6 - NII Engine

## Asset Side

- [ ] Asset volume analysis
- [ ] Asset yield analysis
- [ ] Fixed / floating analysis
- [ ] Repricing analysis

## Liability Side

- [ ] Deposit cost analysis
- [ ] Funding cost analysis
- [ ] Capital instrument cost analysis

## NII Calculation

- [ ] Interest Income
- [ ] Interest Expense
- [ ] Net Interest Income

## Scenarios

- [ ] +100bp rates
- [ ] -100bp rates
- [ ] Base case

---

# Phase 7 - Earnings Engine

## Income Statement

- [ ] Net Interest Income
- [ ] Fee Income
- [ ] Operating Expenses
- [ ] Expected Losses
- [ ] Taxes

## Earnings

- [ ] Pre-Tax Profit
- [ ] Net Income
- [ ] Retained Earnings

## Scenarios

- [ ] Bull Case
- [ ] Base Case
- [ ] Stress Case

---

# Phase 8 - Market Risk Engine

## New Dataset

- [ ] Create market_sensitivities.csv

Columns:

- exposure_id
- DV01
- CS01
- FX_DELTA
- VEGA

## Risk Calculations

- [ ] Interest Rate Risk
- [ ] Credit Spread Risk
- [ ] FX Risk

## Stress Testing

- [ ] Parallel Up Shock
- [ ] Parallel Down Shock
- [ ] Credit Spread Widening
- [ ] FX Shock

## Outputs

- [ ] market_risk_results.csv

---

# Phase 9 - Scenario Engine

## New Dataset

- [ ] Create stress_scenarios.csv

## Balance Sheet Scenarios

- [ ] Loan growth
- [ ] Deposit growth
- [ ] Asset mix changes
- [ ] Funding mix changes

## Capital Scenarios

- [ ] Earnings accretion
- [ ] Dividend payout
- [ ] Share buybacks
- [ ] Extraordinary losses

---

# Phase 10 - Liquidity Engine

## HQLA Inventory

- [ ] Identify HQLA assets
- [ ] Apply encumbrance adjustments
- [ ] Calculate available HQLA

## LCR

- [ ] Cash outflows
- [ ] Cash inflows
- [ ] Net cash outflows
- [ ] LCR calculation

## NSFR

- [ ] ASF calculation
- [ ] RSF calculation
- [ ] NSFR calculation

---

# Phase 11 - Economic Capital Engine

## Datasets

- [ ] Create market_sensitivities.csv
- [ ] Create stress_scenarios.csv

## Credit Economic Capital

- [ ] Unexpected Loss proxy
- [ ] Credit stress loss

## Market Economic Capital

- [ ] Rate stress losses
- [ ] Spread stress losses
- [ ] FX stress losses

## Counterparty Risk

- [ ] Simplified EPE
- [ ] CVA loss estimate

## Aggregation

- [ ] Credit EC
- [ ] Market EC
- [ ] CVA EC
- [ ] Total Economic Capital

---

# Phase 12 - SVA Engine

## Capital Allocation

- [ ] Allocate RWA
- [ ] Allocate Regulatory Capital
- [ ] Allocate Economic Capital

## Value Creation

- [ ] Cost of Equity
- [ ] Cost of Capital
- [ ] Economic Profit
- [ ] Shareholder Value Added
- [ ] RAROC

## Business Unit Analysis

- [ ] Retail Banking
- [ ] Corporate Banking
- [ ] Treasury
- [ ] Markets

## Ranking

- [ ] Value creators
- [ ] Value destroyers

---

# Phase 13 - Streamlit Dashboard

## Executive Dashboard

- [ ] Balance Sheet Overview
- [ ] RWA Overview
- [ ] Capital Overview
- [ ] NII Overview
- [ ] Earnings Overview

## Scenario Dashboard

- [ ] Loan Growth Slider
- [ ] Deposit Growth Slider
- [ ] Dividend Slider
- [ ] RWA Growth Slider

## Visualizations

- [ ] Balance Sheet Composition
- [ ] CET1 Evolution
- [ ] Capital Waterfall
- [ ] Earnings Waterfall
- [ ] SVA Decomposition

---

# Phase 14 - AI Copilot

## Natural Language Interface

Examples:

- What happens if RWA increase by 10%?
- How much CET1 do I need to support 5bn loan growth?
- What dividend can I distribute?
- Which business unit destroys value?
- Why did my CET1 ratio decline?
- How does a 100bp rate shock affect NII?

## AI Features

- [ ] Scenario explanations
- [ ] Capital planning explanations
- [ ] SVA explanations
- [ ] Management recommendations