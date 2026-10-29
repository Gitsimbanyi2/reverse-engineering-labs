# Assembly fundamentals (lab)

Enough to read Ghidra / GDB, not a full ISA course.

| Idea | x86-64 (System V / typical Linux) |
|------|-------------------------------------|
| Instruction | opcode + operands (`mov`, `add`, `call`, `ret`, `jmp`, `cmp`/`jcc`) |
| Registers | `rax` result; `rdi, rsi, rdx, rcx, r8, r9` integer args; `rsp` stack |
| Control flow | `call` / `ret`; conditional jumps after `cmp`/`test` |
| Data | immediates, stack locals, global `.data` / `.rodata` strings |

**Exercise:** In Ghidra, find `main` of `lab_hello`, list the calls, and name the function that prints the banner. Write the answers in `reports/sample-analysis-report.md`.
