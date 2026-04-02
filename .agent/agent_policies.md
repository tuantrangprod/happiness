1. **Planning Mode Restrictions**:
   - **Never** modify files while in Planning Mode, even if explicitly requested. 
   - If requested, notify the user to switch to Fast Mode to grant edit permissions.

2. **Fast Mode Rules**:
   - Only modify files in Fast Mode AND when the user explicitly requests it (e.g., "apply", "proceed", "execute", "implement").
   - When in doubt about editing a file, always ask the user for permission first.

3. **Artifact Creation**:
   - **Never** create artifact markdown files (e.g., `tasks.md`, `implementation_plan.md`, etc.).
   - Always output tasks, plans, and summaries directly to the chat panel.