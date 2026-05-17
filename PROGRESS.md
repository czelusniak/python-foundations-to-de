# Progress

## Module 1 — Python Review

### 1.1 Variables & primitive types
- [x] ex_01 — variables and print
- [x] ex_02 — four scalar types
- [x] ex_03 — type casting
- [x] ex_04 — arithmetic operators
- [x] ex_05 — comparisons and boolean operators
- [ ] **challenge_1_1** — mixed: types, casting, arithmetic, comparisons

### 1.2 Strings
- [ ] ex_06 — concatenation, len, repetition
- [ ] ex_07 — indexing and slicing
- [ ] ex_08 — common methods
- [ ] ex_09 — split and join
- [ ] ex_10 — f-strings and formatting
- [ ] **challenge_1_2** — mixed: string manipulation, slicing, formatting, type casting

### 1.3 Conditional logic
- [ ] ex_11 — if / elif / else
- [ ] ex_12 — truthy and falsy values
- [ ] ex_13 — combining conditions, in operator
- [ ] **challenge_1_3** — mixed: conditionals, strings, booleans, type checking

### 1.4 Lists
- [ ] ex_14 — creating lists, indexing, modifying
- [ ] ex_15 — list methods
- [ ] ex_16 — slicing lists
- [ ] ex_17 — sorted vs sort, key, reverse
- [ ] ex_18 — len, sum, min, max, in
- [ ] **challenge_1_4** — mixed: list operations, slicing, sorting, aggregation

### 1.5 Loops
- [ ] ex_19 — for loop over a list
- [ ] ex_20 — range and indexed iteration
- [ ] ex_21 — enumerate
- [ ] ex_22 — zip
- [ ] ex_23 — while, break, continue
- [ ] **challenge_1_5** — mixed: loops, lists, conditionals, enumerate/zip

### 1.6 Dictionaries & sets
- [ ] ex_24 — dict creation, lookup, add/update
- [ ] ex_25 — .get() with default
- [ ] ex_26 — iterating keys, values, items
- [ ] ex_27 — defaultdict and Counter
- [ ] ex_28 — sets, operations, when to use
- [ ] **challenge_1_6** — mixed: dicts, sets, loops, aggregation, Counter

### 1.7 Tuples & unpacking
- [ ] ex_29 — tuples vs lists
- [ ] ex_30 — unpacking, swap, *rest
- [ ] **challenge_1_7** — mixed: tuples, unpacking, loops, dicts

### 1.8 Functions
- [ ] ex_31 — def, parameters, return
- [ ] ex_32 — default arguments, mutable default trap
- [ ] ex_33 — *args and **kwargs
- [ ] ex_34 — scope: local vs global
- [ ] ex_35 — lambdas as key=
- [ ] **challenge_1_8** — mixed: functions, default args, *args/**kwargs, lambdas

### 1.9 Comprehensions & generators
- [ ] ex_36 — list comprehensions
- [ ] ex_37 — dict and set comprehensions
- [ ] ex_38 — generator expressions
- [ ] ex_39 — yield and generator functions
- [ ] **challenge_1_9** — mixed: comprehensions, generators, functions, data transformation

### 1.10 Files & error handling
- [ ] ex_40 — reading text files with open
- [ ] ex_41 — writing text files
- [ ] ex_42 — try / except / finally
- [ ] ex_43 — raise
- [ ] ex_44 — pathlib.Path
- [ ] **challenge_1_10** — mixed: file I/O, error handling, data parsing

### 1.11 Basic OOP
- [ ] ex_45 — classes, __init__, instance attributes
- [ ] ex_46 — methods, self, __repr__ / __str__
- [ ] ex_47 — single inheritance
- [ ] ex_48 — @dataclass
- [ ] **challenge_1_11** — mixed: classes, dataclasses, inheritance, dunder methods

---

## Module 2 — Python for Data Engineering

### 2.1 File formats
- [ ] ex_49 — CSV (csv module)
- [ ] ex_50 — JSON and JSON Lines
- [ ] ex_51 — Parquet with pyarrow / pandas
- [ ] ex_52 — compressed files (gzip, .csv.gz)
- [ ] **challenge_2_1** — multi-format product feed (csv.gz + json + jsonl → parquet)

### 2.2 pandas fundamentals
- [ ] ex_53 — Series vs DataFrame
- [ ] ex_54 — inspection: head, info, describe, dtypes
- [ ] ex_55 — selection: loc, iloc, boolean masks
- [ ] ex_56 — adding/modifying columns, assign
- [ ] ex_57 — missing data: isna, fillna, dropna
- [ ] **challenge_2_2** — sensor readings triage (sentinel NaNs, assign, masks)

### 2.3 Data manipulation
- [ ] ex_58 — filtering and sorting
- [ ] ex_59 — groupby and aggregation
- [ ] ex_60 — joins with pd.merge
- [ ] ex_61 — reshaping: pivot, melt, stack
- [ ] ex_62 — date handling
- [ ] ex_63 — apply vs vectorize
- [ ] **challenge_2_3** — monthly sales report (merge + groupby + pivot + dates)

### 2.4 Databases
- [ ] ex_64 — SQLite with sqlite3
- [ ] ex_65 — CSV to SQLite
- [ ] ex_66 — pandas read_sql and to_sql
- [ ] ex_67 — PostgreSQL with psycopg2
- [ ] ex_68 — bulk loading patterns
- [ ] **challenge_2_4** — CSV → SQLite ETL with country summary

### 2.5 DE mini-projects
- [ ] ex_69 — log parser
- [ ] ex_70 — CSV deduplicator
- [ ] ex_71 — schema validator
- [ ] ex_72 — API to Parquet
- [ ] ex_73 — incremental loader
- [ ] ex_74 — data quality report
