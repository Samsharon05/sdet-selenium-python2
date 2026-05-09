# Flakiness Hunt Project

## Purpose

Demonstrate root-cause analysis of flaky Selenium tests and show how to stabilize them.

**Two unstable tests analyzed and fixed:**

1. **Employee Add** - Modal persistence race condition
2. **Employee Delete** - Row count timing race

---

## Project Structure

```
flakiness_hunt_project/
├── analysis/
│   ├── cookie_banner_analysis.py    # Example: another common flakiness pattern
│   ├── employee_add_analysis.py     # BEFORE/AFTER code for add employee
│   └── delete_flakiness_analysis.py # BEFORE/AFTER code for delete
├── pages/
│   ├── base_page.py                 # BasePage with explicit waits
│   └── employee_page.py             # Locators for Web Tables page
├── tests/
│   ├── test_employee_flakiness.py   # Contains both flaky (@pytest.mark.flaky) and stable (@pytest.mark.stable) versions
│   └── test_delete_flakiness.py     # Same pattern for delete operation
├── data/                            # (empty - no shared data used)
├── conftest.py                      # driver fixture + screenshot on failure
├── pytest.ini                       # markers: flaky, stable
└── requirements.txt
```

---

## How to Use

### Run only flaky tests (failures expected)
```bash
pytest -m flaky -v
```

### Run only stable tests (should all pass)
```bash
pytest -m stable -v
```

### Run both (default: all tests)
```bash
pytest -v
```

### Run with parallel workers
```bash
pytest -n 4 -m stable -v   # stable tests only, parallel
pytest -n 2 -v             # all tests (flaky will fail)
```

### Output interpretation
```
tests/test_employee_flakiness.py::TestFlakyEmployeeAdd::test_add_employee_UNSTABLE_version FAILED
tests/test_employee_flakiness.py::TestFlakyEmployeeAdd::test_add_employee_STABLE_version PASSED
```
- `UNSTABLE` tests: demonstrate the bug (expect failures)
- `STABLE` tests: demonstrate the fix (expect passes)

---

## Flakiness Analysis Summaries

### Test 1: Add Employee Modal Race Condition

**Flaky Test:** `test_add_employee_UNSTABLE_version`

**Observed failures:**
- `TimeoutException` waiting for table visibility
- `StaleElementReferenceException` when counting rows
- Intermittent assertion failures (row count didn't increase)

**Root Cause:**
- Modal close has CSS transition (~500ms)
- After clicking Submit, the modal doesn't disappear instantly
- Test uses `time.sleep(0.5)` — arbitrary, not guaranteed to cover animation
- Test immediately queries table DOM while modal still animating/closing
- DOM mutation causes stale references or incomplete refresh

**Fix:**
```python
# BEFORE (flaky):
import time; time.sleep(0.5)
new_rows = len(driver.find_elements(By.XPATH, ep.TABLE_ROWS))

# AFTER (stable):
bp.wait_for_invisible("//div[@class='modal-content']")
new_rows = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
```

**Why it works:**
- `wait_for_invisible` polls until modal `display: none` or removed from DOM
- Covers animation duration + any network latency
- Guarantees table is fully interactive before proceeding

---

### Test 2: Delete Employee Race Condition

**Flaky Test:** `test_delete_employee_UNSTABLE_version`

**Observed failures:**
- `AssertionError: Expected 2 rows but got 3` (deletion not yet registered)
- Inconsistent row count after delete
- More failures under load/slow CPU

**Root Cause:**
- Clicking delete triggers React state update (not instant DOM removal)
- Row fades out (~300ms) then removed from DOM
- Test uses fixed `time.sleep(0.7)` — arbitrary, sometimes too short
- Querying row count before state fully updated gives stale count

**Fix:**
```python
# BEFORE (flaky):
time.sleep(0.7)
after = len(driver.find_elements(By.XPATH, ep.TABLE_ROWS))

# AFTER (stable):
bp.wait.until(
    lambda d: len(d.find_elements(By.XPATH, ep.TABLE_ROWS)) == initial - 1
)
after = len(bp.driver.find_elements(By.XPATH, ep.TABLE_ROWS))
```

**Why it works:**
- Lambda condition polls every 0.5s until row count actually decreases
- Dynamic wait adapts to actual system speed (not hardcoded sleep)
- Returns fresh count only after DOM reflects deletion

---

## Patterns for Stabilizing Flaky Tests

### Always use dynamic waits, never hardcoded sleep
```python
# ❌ Bad
import time; time.sleep(2)

# ✅ Good
wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
```

### Wait for state changes, not time intervals
```python
# ❌ Bad
time.sleep(1)  # Assume modal closed by now
assert new_row_count > old

# ✅ Good
wait.until(lambda d: count_rows(d) > initial_count)
```

### Avoid holding element references across page changes
```python
# ❌ Bad (stale after DOM update)
row = driver.find_element(By.XPATH, "//tr[1]")
driver.find_element(By.ID, "delete").click()
row.text  # StaleElementReferenceException!

# ✅ Good (fresh lookup after DOM change)
driver.find_element(By.ID, "delete").click()
wait.until(EC.staleness_of(old_row))
new_row = driver.find_element(By.XPATH, "//tr[1]")
```

### Use invisibility for closing elements
```python
# ❌ Bad
submit.click()
time.sleep(1)  # Modal may still be visible

# ✅ Good
submit.click()
wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal']")))
```

### Prefer explicit conditions over implicit assumptions
```python
# ❌ Bad
assert "success" in driver.page_source

# ✅ Good
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "success"))
```

---

## Running the Analysis

```bash
# Install
pip install -r requirements.txt

# Run flaky tests (expect failures)
pytest -m flaky -v --tb=short

# Run stable tests (expect passes)
pytest -m stable -v --tb=short

# Compare side-by-side
pytest -m "flaky or stable" -v --tb=line
```

---

## Test Results (Expected)

### Flaky tests (demonstrating the bug)
```
test_add_employee_UNSTABLE_version   FAILED ~40% of runs
test_delete_employee_UNSTABLE_version FAILED ~30% of runs
```

### Stable tests (demonstrating the fix)
```
test_add_employee_STABLE_version     PASSED 100%
test_delete_employee_STABLE_version  PASSED 100%
```

---

## Extra Analysis Files

- `analysis/cookie_banner_analysis.py` — Another common flakiness pattern (dynamic banners)
- `analysis/employee_add_analysis.py` — Detailed before/after for add operation
- Both files show side-by-side unstable vs stable implementations

---

## Key Takeaway

Flakiness is rarely "random." It's always caused by:
1. **Timing assumptions** (sleep vs wait)
2. **DOM mutations** (stale references)
3. **Race conditions** (state not settled before assertion)
4. **Environment variance** (different machine speeds)

**Fix:** Replace assumptions with explicit conditions. Use WebDriverWait to sync test with actual application state.