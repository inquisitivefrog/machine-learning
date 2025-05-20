
(py3ml) tim@Tims-MacBook-Pro quantum-circuit % git remote -v
origin	git@github.com:inquisitivefrog/machine-learning.git (fetch)
origin	git@github.com:inquisitivefrog/machine-learning.git (push)
(py3ml) tim@Tims-MacBook-Pro quantum-circuit % git config --global --list
user.email=inquisitivefrog@gmail.com
user.name=Tim Stilwell

git remote -v
git status
find src/ -type f -name "*.py" -exec wc -l {} \;
git add src/
git commit -m "Prepare src/ for CodeGuru analysis"
git push origin main

aws codecommit create-repository --repository-name quantum-circuit-src --region us-east-1
git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
git checkout -b codeguru-src
git rm -r --cached scripts/ backups/ docs/ logs/ README.grok README.md
git add src/
git commit -m "Include only src/ for CodeGuru"
git remote add codecommit codecommit::us-east-1://quantum-circuit-src
git push codecommit codeguru-src
git checkout main
aws codeguru-reviewer associate-repository \
  --repository CodeCommit={Name=quantum-circuit-src} \
  --region us-east-1

aws codeguru-reviewer list-repository-associations --region us-east-1
aws codeguru-reviewer create-code-review \
  --name quantum-src-review-$(date +%s) \
  --type RepositoryAnalysis \
  --repository-analysis CodeCommit={RepositoryName=quantum-circuit-src,BranchName=codeguru-src} \
  --region us-east-1
aws codeguru-reviewer describe-code-review \
  --code-review-arn arn:aws:codeguru-reviewer:us-east-1:084375569056:code-review:your-code-review-arn \
  --region us-east-1
aws codeguru-reviewer list-recommendations \
  --code-review-arn arn:aws:codeguru-reviewer:us-east-1:084375569056:code-review:your-code-review-arn \
  --region us-east-1 > codeguru_recommendations.txt
vi src/quantum_circuit_ghz_check.py
git add src/quantum_circuit_ghz_check.py
git commit -m "Apply CodeGuru recommendations"
git push origin main
vi ./scripts/delete_resources.sh 
vi ./scripts/verify_cleanup.sh
./scripts/delete_resources.sh us-east-1
./scripts/verify_cleanup.sh us-east-1

Attempted CodeGuru Reviewer analysis, but AWS CodeCommit is unavailable to new customers 
(as of July 25, 2024). Used Pylint locally to analyze src/ files (249 lines). Applied 
fixes: added docstrings, handled S3 exceptions, simplified expressions.

(py3ml) tim@Tims-MacBook-Pro quantum-circuit % pylint src/*.py > pylint_report.txt
(py3ml) tim@Tims-MacBook-Pro quantum-circuit % wc -l pylint_report.txt 
      67 pylint_report.txt

