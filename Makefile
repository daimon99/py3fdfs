help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

release: ## 发布到 pypi
	-rm -rf dist
	bumpversion minor
	python3 setup.py sdist
	twine upload dist/*.gz
