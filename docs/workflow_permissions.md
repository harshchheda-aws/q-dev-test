# Workflow Permissions Documentation

## Overview

This document provides detailed information about the workflow permissions implemented in this project, with a specific focus on issue labeling permissions for generative AI assistants.

## Issue Labeling Permissions

### Human Users

Human users with the following roles have permission to label issues:
- Repository administrators
- Repository maintainers
- Contributors with write access

These permissions are managed through the GitHub permissions system and the workflow defined in `.github/workflows/issue-labeling.yml`.

### Generative AI Assistants

Generative AI assistants, including but not limited to:
- Amazon Q-Dev
- GitHub Copilot
- Other AI-based assistants

**Do not have permission to label issues in this project.**

This restriction is implemented through:
1. The issue labeling workflow that checks the actor's identity
2. Notes in issue templates informing users of this restriction
3. Documentation in the README files

## Implementation Details

### Workflow Implementation

The issue labeling workflow (`.github/workflows/issue-labeling.yml`) implements the following logic:

1. Triggers on issue and pull request events (opened, edited, reopened)
2. Checks if the actor is a generative AI assistant
3. If the actor is identified as an AI assistant, denies permission to label
4. For human users, checks their role in the repository
5. Allows or denies labeling based on the user's role

### Testing

The implementation includes a test workflow (`.github/workflows/test-issue-permissions.yml`) that allows testing the permission logic:

1. Can be manually triggered with parameters
2. Tests both human and AI user scenarios
3. Verifies that permissions are correctly applied

## Rationale

This permission structure is implemented because:

1. Issue labeling requires contextual understanding and project knowledge
2. Human maintainers should review and categorize issues
3. AI assistants can help with other tasks but should not make categorization decisions

## How to Modify Permissions

If you need to modify these permissions:

1. Edit the `.github/workflows/issue-labeling.yml` file
2. Update the `AUTHORIZED_ROLES` array to include or exclude roles
3. Modify the actor detection logic if needed
4. Run the test workflow to verify changes

**Note:** Any changes to permission structures should be reviewed by a repository administrator.