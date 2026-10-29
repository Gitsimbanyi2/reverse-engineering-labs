# Executable formats (lab)

| Format | Magic (hex) | Typical OS |
|--------|-------------|------------|
| ELF | `7F 45 4C 46` (`\x7fELF`) | Linux |
| PE | `4D 5A` (`MZ`) then PE signature at `e_lfanew` | Windows |
| Mach-O | `FE ED FA CE` / `CF FA ED FE` | macOS |

Use `python-tools/binary-inspector/inspect_binary.py` on any file. On `lab_hello.c` you will see **text**, not ELF/PE, until you compile it in the lab VM:

```bash
# Linux lab VM only
gcc -g -O0 -o lab_hello malware-analysis/safe-samples/lab_hello.c
python python-tools/binary-inspector/inspect_binary.py lab_hello
```

Do not commit compiled malware. A benign `lab_hello` binary may be kept **local**; this Git repo keeps **source**.
