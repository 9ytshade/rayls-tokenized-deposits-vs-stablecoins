# PHASE 1 FACT-CHECK & PRIMARY EVIDENCE DOSSIER
## Verification of Legal, Macroeconomic, and Technical Citations

Every assertion in Phase 1 has been cross-referenced against official statutory texts, central bank research publications, and primary project documentation. Below is the verified evidence matrix.

---

### 1. The "Singleness of Money" & Stablecoin Critique
* **Primary Citation:** Bank for International Settlements (BIS) Bulletin No. 73 (11 April 2023).  
  *Authors:* Rodney Garratt and Hyun Song Shin.  
  *Title:* *"Stablecoins versus tokenised deposits: implications for the singleness of money"*.  
  *URL:* `https://www.bis.org/publ/bisbull73.htm`
* **Verified Findings from Text:**
  - Stablecoins circulate as digital **bearer instruments** without direct ledger updates by the issuing bank.
  - Secondary market pricing deviates under liquidity strain (failing par value $\text{Exchange Rate} = 1.0$), which directly violates the singleness of money.
  - Tokenized deposits represent commercial bank money that settles interbank claims in risk-free central bank money (M0), natively preserving par value.

---

### 2. BIS Project Agorá (Cross-Border Interbank Tokenized Deposits)
* **Primary Citation:** Bank for International Settlements (BIS) & Institute of International Finance (IIF) Project Agorá Announcements and Interim Reports (2024–2026).  
  *URL:* `https://www.bis.org/about/bisih/topics/cbdc/agora.htm`
* **Verified Findings from Text:**
  - Public-private collaboration uniting **7 major central banks** (Bank of England, Bank of France / Eurosystem, Bank of Japan, Bank of Korea, Bank of Mexico, Swiss National Bank, and the Federal Reserve Bank of New York) and over **40 global commercial banks**.
  - Explicit mandate: Building a shared programmable platform co-locating **wholesale tokenized central bank money (reserves)** and **tokenized commercial bank deposits**.
  - Concluded that tokenization does **not** alter the underlying legal obligations of commercial bank deposits or central bank reserves, enabling atomic cross-border settlement without unbacked stablecoins.

---

### 3. Statutory Classifications & Exclusions (MiCA & US FDI Act)
* **European Union (MiCA):**
  - **Exclusion of Deposits:** *Article 2(2)(b) of Regulation (EU) 2023/1114 (MiCA)* explicitly exempts crypto-assets that qualify as deposits under Directive 2014/49/EU.
  - **Electronic Money Tokens (EMTs):** Regulated under *Title IV of MiCA*. Recital 12 explicitly states that funds received for EMTs are not deposits and do not benefit from Deposit Guarantee Schemes (DGS).
* **United States Banking Law:**
  - **FDI Act Section 3(l):** *12 U.S.C. § 1813(l)* defines bank deposits eligible for FDIC coverage. Stablecoins do not qualify and explicitly disclaim FDIC pass-through coverage in their user agreements.

---

### 4. Regulated Liability Network (RLN) U.S. Proof of Concept
* **Primary Citation:** Federal Reserve Bank of New York (NYIC) & U.S. Financial Services Sector Report (July 2023).  
  *Title:* *"Regulated Liability Network U.S. Proof of Concept: Business, Technical, and Legal Reports"*.
* **Verified Findings from Text:**
  - Successfully demonstrated wholesale settlement on a shared multi-entity distributed ledger using **deposit tokens** settled via wholesale central bank money.
  - Proved atomic settlement across commercial banks (Citi, BNY Mellon, HSBC, Wells Fargo, etc.) within existing U.S. commercial law and payment finality frameworks.

---

### 5. Banco Central do Brasil (Drex Pilot) & Rayls Architecture
* **Primary Citation:** Banco Central do Brasil (BCB) Technical Reports on the Drex Pilot (Phase 1 & 2) & BIS Innovation Hub case studies (2023–2026).
* **Verified Findings from Text:**
  - Drex encountered the "Privacy Trilemma": standard permissioned EVM chains (Hyperledger Besu) violated Brazilian Banking Secrecy Law (*Lei Complementar 105/2001*).
  - Rayls (developed by Parfin) was formally introduced and evaluated in the Drex pilot to solve this via segregated **Private Subnets** communicating through a privacy and cryptographic hub, ensuring that tokenized deposits and federal public bonds (TPFt) settle confidentially without public data leakage.
