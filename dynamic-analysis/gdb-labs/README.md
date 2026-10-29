# GDB lab — `lab_hello` (Linux VM)

```bash
gcc -g -O0 -o lab_hello malware-analysis/safe-samples/lab_hello.c
gdb ./lab_hello
(gdb) break main
(gdb) run
(gdb) info registers
(gdb) next
(gdb) continue
```

On Windows, use x64dbg against a lab-built PE of the same source. Same idea: break on entry, step, observe the print.

Never attach a debugger to production SACCO/CBS processes from this write-up.
