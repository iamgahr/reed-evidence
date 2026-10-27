# Commitments

These commitments bind the published results to documents and data that are not published, without revealing their contents.

## Task identities
- **How a task's commitment is made:** each `task_commitment` in `data/` is `sha256("<salt_i>:<task_id_i>")`.
- **The salt:** every task has its own 256-bit secret salt.
- **Opening a task:** revealing one task's id and salt opens that task alone. The other tasks stay hidden.
- **Across files:** the same task has the same commitment in both files. So the E181 tasks can be seen to be a subset of the 638, which the README states.

## Private documents and data, by SHA-256

| item | SHA-256 | registered or finalised (UTC, from our private version history) |
|---|---|---|
| E180 step 1 pre-registration (Anthropic's agent) | `b80d2ad38a23d3ad8077903e0e8b0b9bf9b559d1a872c38997f81328652cd633` | 2026-10-20 17:33 |
| E180 step 1 result | `11e3331e984ce869241ef1607eeb4241ac5955947a179f47e68ed594ecdcfbe0` | 2026-10-20 19:18 |
| E180b pre-registration (gpt-6-astra) | `eb023643bbabc3e941e4f5d86e9c88bbe0bc74054bdf73d15736ae33cf66f6f6` | registered 2026-10-20 22:55; amendments through 2026-10-21 17:32; read once 2026-10-25 14:33 |
| E180b result | `8e9086308d368bc2d034923196dc57e755b356ff0b77caef9331974c59a58b00` | 2026-10-25 14:53 |
| E181 pre-registration | `d550918bd31a3a9cdf1e7e23d9453cd0ff406aa3b9d4f8a5c1ae51d31ccf1c67` | registered 2026-10-20 19:53; amendments through 2026-10-22 04:46; read 2026-10-23 |
| E181 result | `a7dfa32d7f6534a42031cec2f658f584483576b1e6a59c24150674624484b0f1` | 2026-10-23 08:00 |

**These timestamps are not externally notarised.** The hashes fix each document's content as of this repository's first commit, and future pre-registrations will have their hashes published before they run.
