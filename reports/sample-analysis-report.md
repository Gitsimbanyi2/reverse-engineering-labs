# Sample analysis report — lab_hello (benign)

| Field | Value |
|-------|--------|
| Analyst | Gitsimbanyi Prosper |
| Date | 29 October 2026 |
| Sample | `malware-analysis/safe-samples/lab_hello.c` |
| Classification | Benign teaching binary (source in Git; compile in the lab VM) |
| Malware family | None |

## Static

- Source is C; `banner()` prints `LAB-HELLO-BANNER`.
- YARA `lab_hello_banner` matches the source.
- Inspector class: C source until compiled; then ELF or PE depending on the lab OS.

## Dynamic (after `gcc -g -O0`)

- Process starts, writes two lines to stdout, exits 0.
- No files dropped, no network, no persistence.

## Detection

- YARA rule in `yara/detection-rules/lab_hello_banner.yar`.
- String hunt in Ghidra Defined Strings.

## Recommendation

Use this file as the template for **private** case notes. Do not publish analyses of live customer incidents on GitHub.
