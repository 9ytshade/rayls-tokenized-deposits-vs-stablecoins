# THE RAIL — WEEK 4 MASTER RESEARCH & EXECUTION BLUEPRINT
## Topic: Tokenized Deposits vs. Stablecoins: The Structural, Legal, and Architectural Deep Dive
### Goal: 10/10 Standard (+3 DP Cross-Post & Public Reproducibility Package)

---

## 🏛️ OVERVIEW & STRATEGIC POSITIONING
- **Core Search / LLM Query:** *"Tokenized deposits vs stablecoins: what is the actual legal, balance sheet, and architectural difference for banking settlement?"*
- **Target Audience:** Institutional bankers, central bank digital currency (CBDC) architects, Web3 DeFi developers, regulatory attorneys, and crypto researchers.
- **Rayls Alignment:** Positioning Rayls as the purpose-built Regulated Liability Network (RLN) and UniFi (Unified Financial Infrastructure) solving the "Singleness of Money" trilemma without exposing bank customer data or breaking two-tier commercial banking.
- **Reviewer Target:** Full compliance with the 8–9 RP rubric (negative tests, exact decimal math, network scope separation, public GitHub reproducibility package, and mobile-first diagrams).

---

## 🧭 PHASED EXECUTION ROADMAP

### PHASE 1: MACRO, LEGAL & BALANCE SHEET ARCHITECTURE
- [ ] **1.1 The Singleness of Money & Monetary Sovereignty:**
  - Why the Bank for International Settlements (BIS Project Agorá) and central banks reject public stablecoins for wholesale settlement.
  - The risk of "competing dollar discounts" and monetary fragmentation under private non-bank stablecoins.
- [ ] **1.2 Balance Sheet Mechanics (M0 vs. M1 vs. Private Debt):**
  - Stablecoins (USDC/USDT): Bearer token, private non-bank debt claim, 100% reserve drain, disintermediating commercial bank credit creation.
  - Tokenized Deposits: Direct digital representation of commercial bank deposit liabilities (M1 money), backed by fractional reserves, central bank discount windows, and statutory deposit insurance (FDIC/FSCS).
- [ ] **1.3 Statutory Frameworks Comparison:**
  - EU MiCA (Electronic Money Tokens vs. Credit Institution Deposits).
  - US UCC Article 8/9/12 (Bearer claims vs. Controllable Electronic Records).
  - New York Fed / UK Regulated Liability Network (RLN) PoC findings.

---

### PHASE 2: SMART CONTRACT ANATOMY & CODE-LEVEL COMPARISON
- [ ] **2.1 Standard Stablecoin Code Architecture (ERC-20 + Binary Blacklists):**
  - Bytecode and storage analysis of open stablecoins (USDC FiatTokenV2 / USDr).
  - Analysis of `isBlacklisted[address]` and admin freeze functions.
  - The fatal institutional flaw: Binary cleartext blacklists on public chains leak bank counterparty relationships and freeze entire balances rather than specific disputed transactions.
- [ ] **2.2 Tokenized Deposit Code Architecture (Permissioned State Gating):**
  - Identity-registry-gated transfer hooks (ERC-3643 / ERC-1400 concepts).
  - Conditional transfer logic: How transfers verify sender/receiver KYC credentials on-chain without exposing private identities.
- [ ] **2.3 Rayls Private Sovereign Subnet Implementation:**
  - How commercial banks issue tokenized deposits on dedicated Rayls Private Subnets.
  - How interbank clearing occurs across the Privacy Hub without forcing banks to hold a shared speculative or non-bank stablecoin.
  - **Critical Scope Discipline:** Explicitly distinguishing live Public Chain infrastructure from Private Subnet architecture (avoiding the Week 2 penalty).

---

### PHASE 3: HANDS-ON EMPIRICAL AUDIT & REPRODUCIBLE SCRIPTS
- [ ] **3.1 Live On-Chain Escrow & Collateral Audit (Chain ID: `72957`):**
  - Develop `verify_usdr_collateral.py` to query live Rayls Public Chain (`https://mainnet-rpc.rayls.com` at Block `#12,885,450+`).
  - Calculate exact circulating supply of USDr and reconcile against bridge escrow balances down to 18 decimal places.
- [ ] **3.2 Negative / Tamper Revert Test (The 8–10 Reviewer Standard):**
  - Develop `test_permissioned_transfer_gates.py`.
  - Simulate and execute an intentional permission violation (unauthorized sender, missing identity claim, or frozen sovereign participant) to prove deterministic EVM contract revert with exact error signatures.
- [ ] **3.3 Cost & Gas Settlement Reconciliation:**
  - Measure exact transaction gas consumption for standard stablecoin transfer vs. permissioned compliance transfer on Rayls Reth.
  - Reconcile theoretical transaction cost against empirical block execution.

---

### PHASE 4: EVIDENCE MATRIX & ZERO-ASSUMPTION BOUNDARIES
- [ ] **4.1 Build Section 6 Evidence Matrix:**
  - Categorize every finding: **[Verified On-Chain]**, **[Documented Architecture]**, **[Regulatory Source]**, or **[Implementation Boundary / Unverified]**.
  - Clearly state what is live on Mainnet today vs. what is designed for Private Banking Hubs.
- [ ] **4.2 Statutory References & Academic Citations:**
  - BIS Project Agorá (2024), CPMI-IOSCO PFMI, NY Fed RLN, Basel Committee, EU MiCA.

---

### PHASE 5: ORIGINAL HIGH-CONTRAST MOBILE-FIRST DIAGRAMS
- [ ] **Diagram 1:** *The Balance Sheet Trilemma: Stablecoins (Bearer Debt) vs. Tokenized Deposits (Commercial Bank M1 Liabilities).*
- [ ] **Diagram 2:** *Settlement Pipeline: Cleartext ERC-20 Public Transfer vs. Rayls Private Sovereign Subnet Settlement.*
- [ ] **Diagram 3:** *Negative Test Architecture: Identity Registry Verification Gate & Revert Boundary.*
- [ ] **Evidence Matrix Infographic:** High-contrast table with large typography readable on smartphone screens.

---

### PHASE 6: GITHUB REPRODUCIBILITY SUITE & CROSS-POST DELIVERABLES
- [ ] Build clean, standalone GitHub repository structure:
  - `README.md` (Executive summary, installation instructions, execution guide).
  - `scripts/` (Automated reproduction scripts with zero dependencies).
  - `data/` (Raw JSON-RPC outputs, error receipts, and balance snapshots).
- [ ] Write the Master Deep-Dive Article (`TOKENIZED_DEPOSITS_VS_STABLECOINS_INVESTIGATION.md`).
- [ ] Write the Social Summary & Cross-Post Thread (`CROSS_POST_SUMMARY.md`).
- [ ] Prepare GitHub push commands so the user can deploy to their public profile.
