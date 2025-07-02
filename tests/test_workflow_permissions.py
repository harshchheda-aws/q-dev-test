import unittest
import os
import yaml
import re

class TestWorkflowPermissions(unittest.TestCase):
    """Test suite to verify workflow permissions are correctly implemented."""
    
    def setUp(self):
        """Set up test environment."""
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.workflows_dir = os.path.join(self.base_dir, '.github', 'workflows')
        self.templates_dir = os.path.join(self.base_dir, '.github', 'ISSUE_TEMPLATE')
        
    def test_workflow_directory_exists(self):
        """Test that the workflows directory exists."""
        self.assertTrue(os.path.exists(self.workflows_dir), 
                        "Workflows directory does not exist")
    
    def test_issue_labeling_workflow_exists(self):
        """Test that the issue labeling workflow file exists."""
        workflow_file = os.path.join(self.workflows_dir, 'issue-labeling.yml')
        self.assertTrue(os.path.exists(workflow_file), 
                        "Issue labeling workflow file does not exist")
    
    def test_issue_labeling_workflow_content(self):
        """Test that the issue labeling workflow contains necessary permissions checks."""
        workflow_file = os.path.join(self.workflows_dir, 'issue-labeling.yml')
        
        with open(workflow_file, 'r') as f:
            content = f.read()
            
        # Check for AI assistant permission check
        self.assertIn("generative AI assistant", content, 
                      "Workflow should check for generative AI assistant")
        
        # Check for permission denial for AI assistants
        self.assertIn("can_label::false", content, 
                      "Workflow should deny labeling permissions to AI assistants")
    
    def test_issue_templates_contain_permission_notes(self):
        """Test that issue templates contain notes about labeling permissions."""
        for template_file in ['bug_report.md', 'feature_request.md']:
            file_path = os.path.join(self.templates_dir, template_file)
            self.assertTrue(os.path.exists(file_path), 
                            f"Template file {template_file} does not exist")
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            self.assertIn("Generative AI assistants do not have permission", content,
                         f"Template {template_file} should mention AI permission restrictions")
    
    def test_test_workflow_exists(self):
        """Test that the test workflow file exists."""
        test_workflow_file = os.path.join(self.workflows_dir, 'test-issue-permissions.yml')
        self.assertTrue(os.path.exists(test_workflow_file), 
                        "Test workflow file does not exist")
    
    def test_test_workflow_content(self):
        """Test that the test workflow contains necessary test cases."""
        test_workflow_file = os.path.join(self.workflows_dir, 'test-issue-permissions.yml')
        
        with open(test_workflow_file, 'r') as f:
            content = f.read()
            
        # Check for human and AI test cases
        self.assertIn("human", content, "Test workflow should test human permissions")
        self.assertIn("ai", content, "Test workflow should test AI permissions")
        
        # Check for correct permission logic
        self.assertIn("AI assistants do not have permission", content,
                     "Test workflow should verify AI assistants don't have permission")

if __name__ == '__main__':
    unittest.main()