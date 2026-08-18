# Due Diligence Analyzer

Helps Peter Dib evaluate potential business acquisitions and franchise opportunities by extracting key numbers, risks, and red flags from FDDs, financial statements, contracts, and business listings — and turning them into a concise due-diligence report he can use when talking with brokers, owners, lenders, and potential partners.

## Folder Structure

- `data/raw/` — original source files, exactly as received. Never edited. Gitignored.
- `data/working/` — intermediate files produced while processing
- `data/processed/` — clean, final data ready to use. Committed.
- `scripts/` — Python scripts for extraction and analysis
- `reports/` — generated reports and output
- `docs/` — project documentation

## Data Sources

- FDDs (Franchise Disclosure Documents)
- Financial statements
- Contracts
- Business listings
- Broker, owner, and lender documents

Formats are mostly large PDFs and spreadsheets — TBD as specific deals come in.
