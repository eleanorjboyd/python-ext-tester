# python-ext-tester
a repository to use when testing various functionalities of the vscode-python extension


## Organization Guide
- All example workspaces should be nested in a folder related to the functionality they test (python-testing, python-debugging etc)
- All example workspaces should be named `*-workspace` for clarity


## Contents

### python-testing
- **inc-dec-workspace** : This workspace is a catch-all for example tests written in unittest and pytest
- **multi-root-workspace** : This is a multi-root workspace containing 3 folders with their setup / settings included. Open `test3.code.workspace` as workspace to use.