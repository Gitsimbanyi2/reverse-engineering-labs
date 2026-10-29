# Sandbox / isolated VM checklist

- Snapshot before the run; revert after
- No shared clipboard/folders with the host if the sample is untrusted
- Host-only or disconnected NIC for unknown files
- Record: process tree, files written, network attempts

This repo’s sample is **benign C**. Treat unknown files from the internet as hostile anyway — and **do not add them to Git**.
