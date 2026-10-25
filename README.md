# Rayls On-Chain Investigation: Tokenized Deposits vs. Stablecoins
## Public Reproduction Suite & Empirical Audit Harness

[![Network](https://img.shields.io/badge/Network-Rayls%20Public%20Chain-cyan)](https://mainnet-rpc.rayls.com)
[![Chain ID](https://img.shields.io/badge/Chain%20ID-72957-blue)](https://chainlist.org/chain/72957)
[![Execution Client](https://img.shields.io/badge/Client-Paradigm%20Reth%201.4.1-orange)](https://github.com/paradigmxyz/reth)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This repository contains the standalone, fully reproducible testing and diagnostic code supporting the research paper:  
**"Tokenized Deposits vs. Stablecoins: The Structural, Legal, and Architectural Divergence in Banking Settlement"**.

---

## 📂 Repository Contents

```text
rayls-tokenized-deposits-vs-stablecoins/
├── scripts/
│   ├── verify_rayls_public_state.py      # Live RPC state, consensus cadence, and precompiles audit
│   ├── test_permissioned_transfer_gates.py # 5-scenario negative & tampering test suite
│   ├── benchmark_settlement_cost_and_gas.py # Settlement gas and economic reconciliation
│   └── generate_week_4_visual_assets.py  # Pillow graphics generator (1920x1080)
├── diagrams/
│   ├── cover_image_tokenized_deposits.png
│   ├── diagram_1_balance_sheet_comparison.png
│   ├── diagram_2_negative_test_gates.png
│   └── evidence_boundary_matrix_table.png
├── TOKENIZED_DEPOSITS_VS_STABLECOINS_INVESTIGATION.md # Full master research paper (~2,800 words)
├── CROSS_POST_SUMMARY.md                             # Executive cross-post summary (~650 words)
├── requirements.txt                                  # Dependency list
└── README.md                                         # This documentation file
```

---

## 🚀 Quickstart & Reproduction Guide

### Prerequisites
- Python 3.9+ installed on your system.
- Standard libraries: `urllib`, `json`, `math`, `time`.
- Optional: `Pillow` (only if regenerating PNG visual assets).

### 1. Live On-Chain Telemetry Audit
Queries the live Rayls Public Chain (`https://mainnet-rpc.rayls.com`, Chain ID `72957`):
```bash
python scripts/verify_rayls_public_state.py
```
**Expected Output:**
- Canonical head height (`Block #13,031,708+`).
- Canonical gas limit ceiling: `500,000,000 gas`.
- Measured block cadence: `~1.34s` ($\sigma \approx 0.47\text{s}$) across 30 consecutive transitions.
- FeeAggregator implementation pointer and balance check.
- Active status across EVM precompiles (`0x01` through `0x08`).

---

### 2. Empirical Negative & Tampering Gate Test Suite
Simulates 5 real-world compliance and transfer scenarios against an ERC-3643 identity registry and compliance engine:
```bash
python scripts/test_permissioned_transfer_gates.py
```
**Test Coverage:**
- **Test 1 (Positive):** Compliant institution-to-client transfer $\to$ **SUCCESS**.
- **Test 2 (Negative):** Transfer to non-whitelisted address $\to$ **REVERT** (`0xd3b34208: RecipientNotIdentityVerified`).
- **Test 3 (Negative):** Overspend attempt (\$15M from \$9M balance) $\to$ **REVERT** (`0x78a1bc40: ComplianceRuleViolation`).
- **Test 4 (Negative):** Sanctioned jurisdiction transfer $\to$ **REVERT** (`0x78a1bc40: ComplianceRuleViolation`).
- **Test 5 (Negative):** Sizing limit violation (\$7.5M against \$5M cap) $\to$ **REVERT** (`0x78a1bc40: ComplianceRuleViolation`).

---

### 3. Settlement Gas & Cost Reconciliation
Calculates gas overhead and dollar costs across public ERC-20, permissioned ERC-3643, and Rayls Sovereign Subnet execution:
```bash
python scripts/benchmark_settlement_cost_and_gas.py
```

---

## 🏛️ Statutory Citations & Authorities
- **Bank for International Settlements (BIS):** Bulletin No. 73 (*"Stablecoins versus tokenised deposits: implications for the singleness of money"*, Garratt & Shin, 2023).
- **BIS Project Agorá:** Shared programmable ledger platform uniting 7 central banks and 40+ commercial banks.
- **European Union:** Regulation (EU) 2023/1114 (MiCA), Article 2(2)(b) [Exclusion of bank deposits] and Recital 12 [Electronic money tokens].
- **United States:** Federal Deposit Insurance Act (FDI Act), 12 U.S.C. § 1813(l).
- **Federal Reserve Bank of New York:** Regulated Liability Network (RLN) U.S. Proof of Concept (July 2023).

---

## 📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
