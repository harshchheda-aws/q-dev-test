# q-dev-test

## Project Overview
This repository contains the q-dev-test project, which includes workflows and configurations for GitHub issue management.

## Workflow Permissions

### Issue Labeling
This project implements specific permissions for issue labeling:

- **Human Users**: Maintainers and contributors with appropriate roles can label issues
- **Generative AI Assistants**: Do not have permission to label issues

### Workflow Files
- `.github/workflows/issue-labeling.yml`: Defines the issue labeling workflow and permission checks
- `.github/workflows/test-issue-permissions.yml`: Test workflow to verify permission settings

### Issue Templates
- Bug report and feature request templates are available in the `.github/ISSUE_TEMPLATE` directory
- Templates include notes about labeling permissions

## Testing Permissions
You can test the issue labeling permissions using the `test-issue-permissions.yml` workflow:

1. Go to the Actions tab
2. Select "Test Issue Labeling Permissions" workflow
3. Click "Run workflow"
4. Enter a test user and select the user type (human or ai)
5. Review the results to verify permissions are working correctly