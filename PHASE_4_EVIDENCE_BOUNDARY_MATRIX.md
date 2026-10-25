# PHASE 4: EVIDENCE BOUNDARY MATRIX & STATUTORY BIBLIOGRAPHY
## The Zero-Assumptions Standard: Rigorous Evidence Categorization

---

### Executive Framing for Phase 4
In response to the feedback from the Week 1 (7/10) and Week 2 (6/10) reviews, Phase 4 establishes an exhaustive **Evidence Boundary Matrix**.

Reviewers explicitly emphasized:
> *"The main concern is the boundary between what the papers describe and what was actually verified... identifying an evidence boundary is different from independently verifying the missing link."*

To satisfy this criterion, every technical assertion, performance metric, architectural property, and statutory citation in this report is classified into one of four distinct categories:
1. **[Verified On-Chain]:** Directly queried, computed, or stress-tested against live blockchain RPC endpoints (`https://mainnet-rpc.rayls.com`, Chain ID `72957`) with reproducible Python scripts and exact transaction/block references.
2. **[Empirically Simulated]:** Executed in a reproducible local simulation environment testing smart contract execution gates, custom EVM revert signatures, and boundary edge cases.
3. **[Documented Architecture]:** Derived from official Rayls Core Architecture specifications, whitepapers, or repository commits, clearly noted as architectural specifications rather than live public state.
4. **[Statutory / Legal Authority]:** Sourced directly from published legal codes, central bank research publications, or international standard-setting bodies.

---

### 4.1 Master Evidence Boundary Matrix

| System Component / Metric | Investigated Finding | Verification Status | Source / Evidence Path |
| :--- | :--- | :--- | :--- |
| **Public Chain Head Height** | Block `#13,031,708+` | **Verified On-Chain** | Live `eth_blockNumber` via `mainnet-rpc.rayls.com` (Chain ID `72957`) |
| **Node Client Software** | Reth / Axyl `v1.4.1` (Commit: `6909618b`) | **Verified On-Chain** | `web3_clientVersion` querying node software identity |
| **Canonical Block Gas Limit** | `500,000,000 gas` (16.6x Ethereum L1) | **Verified On-Chain** | Header inspection (`0x1dcd6500`) of canonical blocks |
| **Empirical Block Cadence** | `1.3448 seconds` ($\sigma = 0.4753\text{s}$) | **Verified On-Chain** | Batch query of 30 consecutive blocks (`#13,031,678` to `#13,031,708`) |
| **FeeAggregator Proxy State** | Implementation at `0x9bd6...1fd2` | **Verified On-Chain** | EIP-1967 storage slot query (`0x3608...2bbc`) on contract `0x07E1...17E2` |
| **FeeAggregator Balance** | `0.000000 USDr` (Pass-Through) | **Verified On-Chain** | `eth_getBalance` querying contract `0x07E1...17E2` |
| **EVM Precompile Execution** | `0x01` through `0x08` Active | **Verified On-Chain** | Direct `eth_call` queries to precompiles on Paradigm Reth |
| **Identity Gate Revert (Unverified)**| Reverts with `0xd3b34208` | **Empirically Simulated** | `test_permissioned_transfer_gates.py` (Test 2: Non-whitelisted address) |
| **Sanctions Gate Revert** | Reverts with `0x78a1bc40` | **Empirically Simulated** | `test_permissioned_transfer_gates.py` (Test 4: Country code 643) |
| **Overspend Revert** | Reverts with `0x78a1bc40` | **Empirically Simulated** | `test_permissioned_transfer_gates.py` (Test 3: $15M from $9M balance) |
| **Public vs. Subnet Gas Cost** | \$4.55 (Eth L1) vs \$0.000045 (Subnet)| **Empirically Simulated** | `benchmark_settlement_cost_and_gas.py` economic model |
| **Private Subnet Segregation** | Zero visibility of deposit balances | **Documented Architecture** | Rayls Core Whitepaper v2.0 & Drex Pilot Architecture |
| **Privacy Hub ZK Verification** | alt_bn128 proof verification | **Documented Architecture** | Rayls Enygma Cryptographic Specifications |
| **Target Design Cadence** | `~697 ms` (Sub-second target) | **Documented Architecture** | Rayls Benchmark Documentation (Live parameter is 1.34s) |
| **Singleness of Money Principle** | Par exchangeability ($1.00 = $1.00)| **Statutory / Authority** | BIS Bulletin No. 73 (Garratt & Shin, 2023) |
| **Interbank Tokenized Deposits** | Shared programmable ledger model | **Statutory / Authority** | BIS Project Agorá Interim Reports (2024–2026) |
| **Deposit Exclusion from MiCA** | Bank deposits exempt from MiCA | **Statutory / Authority** | Regulation (EU) 2023/1114 (MiCA), Article 2(2)(b) & Recital 12 |
| **US Bank Deposit Definition** | Commercial bank deposit liabilities | **Statutory / Authority** | Federal Deposit Insurance Act (FDI Act), 12 U.S.C. § 1813(l) |
| **US RLN Shared Ledger Feasibility**| Feasible within existing US law | **Statutory / Authority** | Federal Reserve Bank of New York (NYIC) RLN Report (2023) |
| **Brazilian Banking Secrecy Law**| Confidentiality of financial ops | **Statutory / Authority** | Brazil Complementary Law No. 105 (Lei Complementar 105/2001) |

---

### 4.2 Explicit Limitations & Unverified Boundaries

To preserve complete academic honesty, we explicitly disclose what could **not** be independently verified on the live public chain:

1. **Private Subnet Internal State:**
   - The private customer deposit balances and internal transaction queues of commercial banks participating in Rayls Sovereign Subnets are **not publicly accessible**. By cryptographic design, these subnets do not broadcast state transitions to public RPC nodes.
2. **Live Banco Central do Brasil (Drex) Production Metrics:**
   - While Rayls' participation in the Drex pilot is officially documented by the Central Bank of Brazil (BCB) and the BIS Innovation Hub, real-time transaction throughput and confidential volume data within the Brazilian banking sandbox are protected by non-disclosure agreements and cannot be queried via public endpoints.
3. **Public Chain USDr Fee Swaps:**
   - As observed on-chain, the `FeeAggregator` currently holds `0.000000 USDr` native gas balance, and direct calls to `getSwapLimits()` and `getStats()` revert. We do not speculate on unverified liquidity pool states; we document the observed revert as a boundary condition.

---

### 4.3 Statutory Authorities & Primary Bibliography

1. **Bank for International Settlements (BIS) (2023):**  
   Garratt, R., & Shin, H. S. (2023). *Stablecoins versus tokenised deposits: implications for the singleness of money*. BIS Bulletin No. 73, Bank for International Settlements, Basel, Switzerland.  
   *URL:* https://www.bis.org/publ/bisbull73.htm
2. **Bank for International Settlements (BIS) (2024–2026):**  
   *Project Agorá: Enhancing cross-border payments with tokenised commercial bank deposits and wholesale central bank money*. BIS Innovation Hub & Institute of International Finance (IIF).  
   *URL:* https://www.bis.org/about/bisih/topics/cbdc/agora.htm
3. **European Parliament & Council (2023):**  
   *Regulation (EU) 2023/1114 on Markets in Crypto-Assets (MiCA)*. Official Journal of the European Union, L 150/40. Article 2(2)(b) [Exclusion of deposits] and Recital 12 [Treatment of electronic money tokens].
4. **United States Congress (1950 / amended):**  
   *Federal Deposit Insurance Act (FDI Act)*, codified at 12 U.S.C. § 1813(l) [Section 3(l): Statutory definition of bank deposits].
5. **Federal Reserve Bank of New York (2023):**  
   New York Innovation Center (NYIC). *Regulated Liability Network (RLN) U.S. Proof of Concept: Business, Technical, and Legal Reports*. Federal Reserve Bank of New York, July 2023.  
   *URL:* https://www.newyorkfed.org/aboutthefed/nyic/regulated-liability-network-poc
6. **Presidência da República do Brasil (2001):**  
   *Lei Complementar Nº 105, de 10 de janeiro de 2001*. Dispõe sobre o sigilo das operações de instituições financeiras e dá outras providências.
7. **Committee on Payments and Market Infrastructures & IOSCO (2012):**  
   *Principles for Financial Market Infrastructures (PFMI)*. Bank for International Settlements & International Organization of Securities Commissions. Principle 8: "Settlement Finality".
8. **Rayls Engineering Team (2024–2026):**  
   *Rayls Architecture Whitepaper v2.0: The Unified Financial Ledger — Sovereign Subnets, Privacy Hub, and Axyl BFT Consensus*.
