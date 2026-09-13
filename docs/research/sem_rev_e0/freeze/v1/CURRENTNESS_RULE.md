## 8. Currentness rule

No freely writable `is_current` flag.

At query time `T`, assertion is temporally applicable iff:

```text
valid_from <= T
AND
(valid_to IS NULL OR T < valid_to)
```

Then revision state applies.

A predecessor is not current if an effective `retracts` / `invalidates` / `supersedes` relation applies at `T`.

A successor may be current only if its own interval applies and it has not itself been retracted/invalidated/superseded.

```text
CURRENTNESS = DERIVED PROJECTION, NOT STORED ANSWER FLAG
```

