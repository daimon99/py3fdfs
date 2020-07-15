help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

patch:
	bumpversion patch

minor:
	bumpversion minor

major:
	bumpversion major

release: ## 发布到 pypi
	-rm -rf dist
	python3 setup.py sdist
	twine upload dist/*.gz
