# CLAUDE.md — Due Diligence Analyzer

## Project

Helps Peter evaluate potential business acquisitions and franchise opportunities by extracting key numbers, risks, and red flags from FDDs, financial statements, contracts, and business listings, then turning them into a concise due-diligence report for conversations with brokers, owners, lenders, and potential partners.

## Key Context

TBD — no specific architectural principles or constraints have been set yet. Update this section as real deals and documents come in.

## Data Sources

| System / File | Data | Format |
|---------------|------|--------|
| FDDs (Franchise Disclosure Documents) | Franchise terms, fees, financial performance representations | PDF |
| Financial statements | Revenue, expenses, cash flow for target businesses | PDF / spreadsheet |
| Contracts | Terms, obligations, potential red flags | PDF |
| Business listings | Deal summaries from brokers | PDF / TBD |

## Milestones

1. Gather real documents for one live deal into `data/raw/`
2. Build extraction scripts that pull key numbers, risks, and red flags into `data/processed/`
3. Generate a first concise due-diligence report in `reports/`
4. Iterate the report format based on what's actually useful in broker/owner/lender conversations

## Rules

- Language: English (comments, variable names, and output).
- Environment: Windows 11, commands run in Git Bash. Forward slashes in config paths.
- Data files → `data/`; scripts → `scripts/`; generated reports → `reports/`; documentation → `docs/`.
- Explain what you're doing and why before writing code.
- Ask before complex tasks — don't assume.

## Where My Notes Live

- **Vault:** `C:/Users/retep/OneDrive/Documents/PuravidaDesigns/`
- **Project brief:** `C:/Users/retep/OneDrive/Documents/PuravidaDesigns/01 PROJECTS/Due Diligence Analyzer/Due Diligence Analyzer.md`
- **AIAC Journey brief:** `C:/Users/retep/OneDrive/Documents/PuravidaDesigns/01 PROJECTS/AI Acceleration/Peter/AI Acceleration Club - Peter Journey.md`

Read the project brief before any non-trivial work in this repo. At the end of a
session, log what was accomplished back to the brief's Log table.
