---
title: CI/CD
description: Use Kosli in CI Systems like GitHub Actions, GitLab CI, and more.
---

  This section provides how-to guides showing you how to use Kosli to report changes from
  different CI systems.

  <Note>
  Note that **all** CLI command flags can be set as environment variables by adding the the `KOSLI_` prefix and capitalizing them.
  </Note>

  ## Defaulted Kosli command flags from CI variables

  The following flags are **defaulted** (which means you don't need to provide the flags, they'll be automatically set to values listed below) as follows in the CI systems below:

  <Tabs>
   <Tab title="GitHub" icon="github">

  View defaulted Kosli command flags in Github Actions.
  | Flag | Default |
  | :--- | :--- |
  | --build-url | `<GITHUB_SERVER_URL>/<GITHUB_REPOSITORY>/actions/runs/<GITHUB_RUN_ID>` |
  | --commit-url | `<GITHUB_SERVER_URL>/<GITHUB_REPOSITORY>/commit/<GITHUB_SHA>` |
  | --commit | `<GITHUB_SHA>` |
  | --git-commit | `<GITHUB_SHA>` |
  | --repository | `<GITHUB_REPOSITORY>` |
  | --repo-id | `<GITHUB_REPOSITORY_ID>` |
  | --repo-url | `<GITHUB_SERVER_URL>/<GITHUB_REPOSITORY>` |
  | --repo-provider | `github` |
  | --github-org | `<GITHUB_REPOSITORY_OWNER>` |

  Where `<PLACEHOLDERS>` are Github Actions predefined variables. See [here](https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables) for more details.

  ## Use Kosli in Github Actions

  To use Kosli in [Github Actions](https://docs.github.com/en/actions) workflows, you can use the kosli [CLI setup action](https://github.com/marketplace/actions/setup-kosli-cli) to install the CLI on your Github Actions Runner.
  Then, you can use all the [CLI commands](/client_reference) in your workflows.

  ### GitHub Secrets

  Keep in mind that secrets in Github actions are not automatically exported as environment variables. You need to add required secrets to your GITHUB environment explicitly. E.g. to make kosli_api_token secret available for all cli commands as an environment variable use following:

  ```yaml
  env:
    KOSLI_API_TOKEN: ${{ secrets.kosli_api_token }}
  ```

  ### Example

  Here is an example Github Actions workflow snippet using `kosli-dev/setup-cli-action` running `kosli create flow` command:

  ```yaml
  jobs:
    example:
      runs-on: ubuntu-latest
      env:
        KOSLI_API_TOKEN: ${{ secrets.MY_KOSLI_API_TOKEN }}
        KOSLI_ORG: my-org
      steps:
        - name: setup kosli
          uses: kosli-dev/setup-cli-action@v2
        - name: create flow
          run: kosli create flow my-flow --template pull-request,artifact,test
  ```

  For a complete example of a Github workflow using Kosli, please check the Kosli CLI's [own workflow](https://github.com/kosli-dev/cli/blob/main/.github/workflows/docker.yml).

  </Tab>
  <Tab title="GitLab" icon="gitlab">
  | Flag | Default |
  | :--- | :--- |
  | --build-url | `<CI_JOB_URL>` |
  | --commit-url | `<CI_PROJECT_URL>/-/commit/<CI_COMMIT_SHA>` |
  | --commit | `<CI_COMMIT_SHA>` |
  | --git-commit | `<CI_COMMIT_SHA>` |
  | --repository | `<CI_PROJECT_NAME>` |
  | --repo-id | `<CI_PROJECT_ID>` |
  | --repo-url | `<CI_PROJECT_URL>` |
  | --repo-provider | `gitlab` |
  | --gitlab-org | `<CI_PROJECT_NAMESPACE>` |

  Where `<PLACEHOLDERS>` are GitLab predefined variables. See [here](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html) for more details.

  ## Use Kosli in Gitlab pipelines

  For a complete example of a Gitlab pipeline using Kosli, please check [this cyber-dojo pipeline](https://gitlab.com/cyber-dojo/creator/-/blob/main/.gitlab/workflows/main.yml).

  ### CI runner image (Alpine)

  The Kosli CLI repository ships an Alpine-based [`Dockerfile.alpine`](https://github.com/kosli-dev/cli/blob/main/Dockerfile.alpine) intended for use as a CI runner image. Unlike the default `ghcr.io/kosli-dev/cli` image (which has the `kosli` binary as its entrypoint), the Alpine variant has no entrypoint and bundles `git`, `curl`, and `ca-certificates` alongside the CLI — so it can be used as a general-purpose job image where you also need to clone repos, hit HTTP APIs, or run other shell tooling next to `kosli`.

  Build and push it to your own registry, pinning the CLI version you want:

  ```bash
  # Clone or copy Dockerfile.alpine from https://github.com/kosli-dev/cli
  docker build \
    --build-arg KOSLI_VERSION=2.13.2 \
    -f Dockerfile.alpine \
    -t registry.example.com/ci/kosli-runner:2.13.2 .
  docker push registry.example.com/ci/kosli-runner:2.13.2
  ```

  Then use it as the job image in `.gitlab-ci.yml`:

  ```yaml
  variables:
    KOSLI_ORG: my-org
    KOSLI_HOST: https://app.kosli.com

  attest:
    image: registry.example.com/ci/kosli-runner:2.13.2
    script:
      - kosli version
      - kosli attest generic
          --flow my-flow
          --trail "$CI_COMMIT_SHA"
          --name build
          --compliant=true
    # KOSLI_API_TOKEN should be set as a masked GitLab CI/CD variable
  ```

  The image runs as the non-root `kosli` user with `/workspace` as the working directory. `KOSLI_ORG` and `KOSLI_HOST` are exposed as environment variables so they can be overridden in your CI configuration; `KOSLI_API_TOKEN` should be supplied via a masked CI variable rather than baked into the image.

  </Tab>
  <Tab title="Azure DevOps">
    View defaulted Kosli command flags in Azure DevOps.

    | Flag | Default |
    | :--- | :--- |
    | --build-url | `<System.CollectionUri>/<System.TeamProject>/_build/results?buildId=<Build.BuildId>` |
    | --commit-url | `<System.CollectionUri>/<System.TeamProject>/_git/<Build.Repository.Name>/commit/<Build.SourceVersion>` |
    | --commit | `<Build.SourceVersion>` |
    | --git-commit | `<Build.SourceVersion>` |
    | --repository | `<Build.Repository.Name>` |
    | --repo-id | `<Build.Repository.Id>` |
    | --repo-url | `<Build.Repository.Uri>` |
    | --repo-provider | `azure-devops` |
    | --project | `<System.TeamProject>` |
    | --azure-org-url | `<System.CollectionUri>` |

    Where `<PLACEHOLDERS>` are Azure DevOps predefined variables. See [here](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml) for more details.
  </Tab>
  <Tab title="Bitbucket Cloud">
    View defaulted Kosli command flags in Bitbucket Cloud.

    | Flag | Default |
    | :--- | :--- |
    | --build-url | `https://bitbucket.org/<BITBUCKET_WORKSPACE>/<BITBUCKET_REPO_SLUG>/addon/pipelines/home#!/results/<BITBUCKET_BUILD_NUMBER>` |
    | --commit-url | `https://bitbucket.org/<BITBUCKET_WORKSPACE>/<BITBUCKET_REPO_SLUG>/commits/<BITBUCKET_COMMIT>` |
    | --commit | `<BITBUCKET_COMMIT>` |
    | --git-commit | `<BITBUCKET_COMMIT>` |
    | --repository | `<BITBUCKET_REPO_SLUG>` |
    | --repo-id | `<BITBUCKET_REPO_UUID>` |
    | --repo-url | `<BITBUCKET_GIT_HTTP_ORIGIN>` |
    | --repo-provider | `bitbucket` |
    | --bitbucket-workspace |  `<BITBUCKET_WORKSPACE>` |

    Where `<PLACEHOLDERS>` are Bitbucket Cloud predefined variables. See [here](https://support.atlassian.com/bitbucket-cloud/docs/variables-in-pipelines/) for more details.

  </Tab>
  <Tab title="AWS CodeBuild">
    View defaulted Kosli command flags in AWS CodeBuild.
    | Flag | Default |
    | :--- | :--- |
    | --build-url | `<CODEBUILD_BUILD_URL>` |
    | --commit-url | `<CODEBUILD_SOURCE_REPO_URL>/commit(s)/<CODEBUILD_RESOLVED_SOURCE_VERSION>` |
    | --commit | `<CODEBUILD_RESOLVED_SOURCE_VERSION>` |
    | --git-commit | `<CODEBUILD_RESOLVED_SOURCE_VERSION>` |
    | --repo-url | `<CODEBUILD_SOURCE_REPO_URL>` |

    Where `<PLACEHOLDERS>` are AWS CodeBuild predefined variables. See [here](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html) for more details.
  </Tab>
  <Tab title="CircleCI">
  View defaulted Kosli command flags in CircleCI.

  | Flag | Default |
  | :--- | :--- |
  | --build-url | `<CIRCLE_BUILD_URL>` |
  | --commit-url | `<CIRCLE_REPOSITORY_URL>(converted to https url)/commit(s)/<CIRCLE_SHA1>` |
  | --commit | `<CIRCLE_SHA1>` |
  | --git-commit | `<CIRCLE_SHA1>` |
  | --repository | `<CIRCLE_PROJECT_REPONAME>` |
  | --repo-url | `<CIRCLE_REPOSITORY_URL>` |

  Where `<PLACEHOLDERS>` are CircleCI predefined variables. See [here](https://circleci.com/docs/env-vars/#built-in-environment-variables) for more details.
  </Tab>

  <Tab title="Teamcity">
  View defaulted Kosli command flags in Teamcity.

  | Flag | Default |
  | :--- | :--- |
  | --git-commit | `<BUILD_VCS_NUMBER>` |

  Where `<PLACEHOLDERS>` are Teamcity predefined variables. See [here](https://www.jetbrains.com/help/teamcity/predefined-build-parameters.html) for more details.
  </Tab>
</Tabs>