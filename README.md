# Reverse Engineering Labs

A practical learning portfolio covering binary analysis,
debugging, executable formats, and defensive malware
analysis.

## Objectives
- Understand binary structures and program behavior.
- Practice static and dynamic analysis.
- Develop defensive detection and analysis skills.
- Document findings in reproducible technical reports.

## Tools
Ghidra, GDB, x64dbg, Python, YARA

## Safety
Analyze only authorized samples in isolated lab
environments. Do not commit live malware or confidential
data to this repository.

**This tree contains no malware.** `malware-analysis/safe-samples/` holds a **benign** C program (`lab_hello.c`) used to practise strings, Ghidra, GDB, and YARA. Do not download “real” samples into this Git repo.

## Layout

| Path | Topic |
|------|--------|
| `fundamentals/assembly-basics/` | Registers, calling, branches |
| `fundamentals/executable-formats/` | ELF and PE headers |
| `static-analysis/ghidra-labs/` | Ghidra exercise on `lab_hello` |
| `static-analysis/strings-and-symbols/` | `file` / `strings` lab |
| `dynamic-analysis/gdb-labs/` | GDB breakpoints on `lab_hello` |
| `dynamic-analysis/sandbox-analysis/` | Isolated VM checklist |
| `malware-analysis/safe-samples/` | Benign source only |
| `malware-analysis/behavior-reports/` | How to write a behaviour note |
| `yara/detection-rules/` | Rule for the lab banner string |
| `python-tools/binary-inspector/` | Magic-byte inspector |
| `reports/sample-analysis-report.md` | Worked example on `lab_hello` |

## Author

Gitsimbanyi Prosper — Ag. Senior Manager, Cybersecurity & Compliance
