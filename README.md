# Python CI practice: Grade calculator

This command-line program averages scores and assigns a letter grade. It uses
only Python's standard library, so there are no packages to install.

Run it from this directory:

```bash
python3 grades.py 80 90 100
python3 -m unittest discover -v
```

The first command prints `Average: 90.0 | Grade: A`. The second runs four tests.

## CI exercise

Create `.github/workflows/python.yml` in this directory. Trigger the workflow
on pushes and pull requests. Give it a job that uses an Ubuntu runner, checks
out the repository, sets up Python, and runs:

```bash
python -m unittest discover -v
```

Try changing a grade boundary in `grades.py`, pushing the change, and reading
the failed test in GitHub Actions. Fix the boundary and push again.

## CD exercise

Once CI works, choose what you want to deliver. For this command-line project,
you could package the program and upload it as a workflow artifact. A server
deployment is unnecessary for this exercise.
