# Strings and symbols

```bash
file lab_hello
strings -n 8 lab_hello | head
nm lab_hello | head    # if not stripped
```

If the binary is stripped, Ghidra still has the string; symbols will not.

**Lab check:** `strings` must show `LAB-HELLO-BANNER` after a debug compile (`gcc -g`).
