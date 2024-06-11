



.github/workflows/main.yml

```
name: test

on:
  push:
    branches: [ python-shell ]

jobs:
  test-job:
    name: 测试任务
    runs-on: ubuntu-latest

    steps:
      - name: action-test
        uses: shuxuecode/github-action@python-shell

#      - name: push dist file to the output branch
#        uses: crazy-max/ghaction-github-pages@v2.6.0
#        with: 
#          target_branch: output
#          build_dir: dist
#        env:
#          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: /dist
```

入口文件  todo

action.yml

```
name: "github-action-python-shell"
author: MarkZ
description: "test"

runs:
  using: "docker"
  image: "Dockerfile"

branding:
  icon: "info"
  color: "blue"

```


