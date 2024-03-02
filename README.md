# Continuous Integration and Developement Machine Learning Repo

This repo works as a github action that appends a small evaluation report to pull requests. It is a working example of [this tutorial](https://www.youtube.com/watch?v=9BgIDqAzfuA).

The toy example consiste of delling a Kaggle dataset of [red wine properties and quality ratings](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009).

## Setting up the GitHub token

To replicate this repository on another machine or in another repository, you need to set up a GitHub token. This token is used by the Continuous Machine Learning (CML) tool to post comments on your pull requests with the results of your machine learning workflows.

Here's how to set up the GitHub token:

1. Generate a new token in GitHub:
   - Go to your GitHub settings.
   - Click on "Developer settings".
   - Click on "Personal access tokens".
   - Click on "Generate new token".
   - Give your token a descriptive name, and select the scopes (or permissions) your token should have. For CML, you need to select the `repo` scope.
   - Click on "Generate token" at the bottom of the page.
   - Copy the token.

2. Add the token to your GitHub Actions workflow:
   - Go to your GitHub repository settings.
   - Click on "Secrets".
   - Click on "New repository secret".
   - Name the secret (in this example, `REPO_TOKEN`), and paste your token as the value.
   - Click on "Add secret".

3. The Github action should now work correctly
