help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

patch: ## 升级补丁版本号
	bumpversion patch

minor: ## 升级小版本号
	bumpversion minor

major: ## 升级主版本号
	bumpversion major

release: ## 发布到 pypi
	-rm -rf dist
	python3 setup.py sdist
	twine upload dist/*.gz
	git push
