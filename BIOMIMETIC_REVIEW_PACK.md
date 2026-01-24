# Review Pack — biomimetic-inventions-public

**Date:** January 22, 2026  
**Analyst:** AI Systems Integrator  
**Scope:** License detection fix, dual licensing clarity, professionalism, security/maintenance scaffolding

---

## A) License State Summary

### Current License Files

1. **`LICENSE`** (root)
   - Contains: Standard MIT License text (lines 1-21)
   - Also contains: Additional IP notice appended (lines 23-41)
   - Issue: GitHub license detection expects pure MIT text. The appended IP notice may cause "Unknown license" detection.

2. **`LICENSE.md`** (root)
   - Contains: Single line "MIT License + Ethical IP Tiers (see README.md). No misuse."
   - Issue: Not standard format, very brief, doesn't help GitHub detection.

3. **Subproject LICENSE files:**
   - `golden-angle-antenna-GAFAA-public/LICENSE` - MIT
   - `PNM-public/LICENSE` - MIT
   - `PhiKey-public/LICENSE` - MIT
   - Status: These are fine, subprojects can have their own licenses.

4. **`COPYRIGHT`** (root)
   - Contains: Copyright notice
   - Status: Separate copyright file is fine, doesn't interfere with license detection.

### Why GitHub Might Show "Unknown License"

**Primary Issue:** The `LICENSE` file contains MIT text but has additional content appended. GitHub's license detection algorithm looks for exact MIT text patterns. When additional content is appended, it may not recognize the license.

**Secondary Issue:** `LICENSE.md` exists but is non-standard and doesn't help detection.

**Solution:** Keep `LICENSE` as pure MIT text, move IP notice to separate file, create clear dual-licensing structure.

---

## B) Proposed License Structure

### Files to Keep/Modify

1. **`LICENSE`** (root) - **MODIFY**
   - Keep: Standard MIT License text only (lines 1-21)
   - Remove: IP notice section (lines 23-41)
   - Purpose: GitHub license detection

2. **`LICENSE.md`** - **RENAME to `LICENSE-IP-NOTICE.md`**
   - Move IP notice content here
   - Purpose: Intellectual property notice (separate from license)

3. **`DOCS_LICENSE.md`** - **CREATE NEW**
   - Content: CC BY-SA 4.0 for documentation
   - Purpose: Clarify documentation licensing

4. **`LICENSE_SUMMARY.md`** - **CREATE NEW**
   - Content: Explains dual licensing structure
   - Purpose: Human-readable licensing guide

### Final Structure

```
LICENSE                    # Pure MIT (for GitHub detection)
LICENSE-IP-NOTICE.md       # IP notice (renamed from LICENSE.md)
DOCS_LICENSE.md            # CC BY-SA 4.0 for docs
LICENSE_SUMMARY.md         # Summary guide
```

---

## C) Tone/Professionalism Items Found

### ✅ Good Practices (No Changes Needed)

- Appropriate disclaimers: "not clinical devices", "not production-grade", "simulation-based"
- Qualified language: "intended to spark ideas", "design goals", "theoretical or simulated"
- No "bombshell" language found
- "Guaranteed" used appropriately in disclaimers ("Nothing in this repository guarantees...")

### ⚠️ Minor Items (Optional Improvements)

1. **README.md License Section:**
   - Current: "MIT License + Ethical IP Tiers (see README.md). No misuse."
   - Issue: Brief, could be clearer
   - Recommendation: Add dedicated "Licensing" section with links

2. **Image References:**
   - Status: All appear correct and consistent
   - No changes needed

3. **Cross-References:**
   - PRIOR_ART.md, PATENTS.md, INVENTION_DISCLOSURE.md link to each other
   - Status: Clean, no changes needed

---

## D) Security/Maintenance Checklist

### ✅ Already Present

- [x] `SECURITY.md` - Exists, well-structured, calm tone
- [x] `.github/dependabot.yml` - Exists, configured for pip and github-actions
- [x] `.github/workflows/reproducibility.yml` - Image generation verification
- [x] `.github/workflows/lint.yml` - Markdown linting
- [x] `.github/workflows/links.yml` - Link checking

### ✅ Status

All security and maintenance scaffolding is already in place from previous work. No additions needed.

---

## E) CI Feasibility

### Current Workflows

1. **reproducibility.yml**
   - Runs: Image generation scripts
   - Status: Safe, fast, non-flaky
   - Recommendation: Keep as-is

2. **lint.yml**
   - Runs: Markdown linting
   - Status: Safe, fast, uses `continue-on-error: true`
   - Recommendation: Keep as-is

3. **links.yml**
   - Runs: Link checking (internal and external)
   - Status: Safe, uses `continue-on-error: true` for externals
   - Recommendation: Keep as-is

### Additional CI Checks (Not Needed)

- Python syntax/import checks: Not needed (scripts are simple
- Ruff/Black formatting: Not needed (repo doesn't use these tools)
- Long-running tests: Not needed (no test suite)

**Conclusion:** Current CI setup is appropriate. No changes needed.

---

## F) Dangling Signals (Manual Review Required)

### GitHub UI Items (Cannot Modify Here)

1. **Open Pull Requests:**
   - Check: https://github.com/phibronotchi-beep/biomimetic-inventions-public/pulls
   - Action: Review manually, merge/close as appropriate

2. **Open Issues:**
   - Check: https://github.com/phibronotchi-beep/biomimetic-inventions-public/issues
   - Action: Review manually, address as appropriate

3. **GitHub Settings to Verify:**
   - Secret scanning: Enable if not already
   - Dependabot alerts: Enable if not already
   - License detection: Should work after LICENSE file fix

4. **Repository Topics/Tags:**
   - Verify: Appropriate topics set for discoverability
   - Action: Review manually in GitHub UI

### Files Requiring Manual Review

1. **`README ALT.md`**
   - Purpose: Unclear (alternative README?)
   - Action: User should decide if still needed

2. **`The Phyllitactic Commons`**
   - Purpose: Unclear (file or directory?)
   - Action: User should document or remove

3. **Audit/Review Files:**
   - `ALIGNMENT_NOTES.md`, `AUDIT_NOTES.md`, `REVIEW_PACK.md`, `FINAL_ALIGNMENT_REPORT.md`
   - Purpose: Historical audit records
   - Action: Keep for documentation, no changes needed

---

## G) Summary of Proposed Changes

### High Priority (License Detection)

1. **Modify `LICENSE`**
   - Remove IP notice section (keep pure MIT)
   - File: `LICENSE` (modify)

2. **Rename `LICENSE.md` to `LICENSE-IP-NOTICE.md`**
   - Move IP notice content here
   - File: `LICENSE.md` → `LICENSE-IP-NOTICE.md` (rename + modify)

3. **Create `DOCS_LICENSE.md`**
   - CC BY-SA 4.0 for documentation
   - File: `DOCS_LICENSE.md` (new)

4. **Create `LICENSE_SUMMARY.md`**
   - Dual licensing explanation
   - File: `LICENSE_SUMMARY.md` (new)

5. **Update `README.md`**
   - Add "Licensing" section with links
   - File: `README.md` (small addition)

### Medium Priority (Clarity)

6. **Verify image references**
   - Status: Already correct, no changes needed

7. **Verify cross-references**
   - Status: Already correct, no changes needed

### Low Priority (Optional)

8. **Document unclear files**
   - `README ALT.md`, `The Phyllitactic Commons`
   - Action: User decision

---

## H) What Will NOT Be Changed

- ❌ No deletion of prior art documentation
- ❌ No modification of core demonstration code
- ❌ No changes to PPA disclaimers
- ❌ No rewriting of major sections
- ❌ No removal of audit/review files
- ❌ No changes to subproject LICENSE files
- ❌ No modification of existing workflows (they're good)

---

## I) Expected Outcome

After changes:

1. **GitHub License Detection:**
   - Should detect: MIT License
   - Badge should appear: ✅ MIT
   - Status: "Unknown" → "MIT"

2. **Dual Licensing Clarity:**
   - Code: MIT (clear from LICENSE)
   - Documentation: CC BY-SA 4.0 (clear from DOCS_LICENSE.md)
   - IP Notice: Separate file (clear from LICENSE-IP-NOTICE.md)

3. **Professionalism:**
   - Clear licensing section in README
   - All licenses properly documented
   - No ambiguity about what applies where

---

**End of Review Pack**
