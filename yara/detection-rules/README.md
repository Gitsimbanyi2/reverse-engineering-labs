# YARA (lab)

```bash
yara yara/detection-rules/lab_hello_banner.yar malware-analysis/safe-samples/lab_hello.c
```

Expect a match on the source file. After compile, run the same rule on the binary — the ASCII banner should still be present unless you stripped strings on purpose.
