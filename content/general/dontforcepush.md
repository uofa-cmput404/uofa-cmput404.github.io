Title: How to Avoid Force Push and Rebase
date: 2026-02-09
tags: policy, labs, project
authors: Hazel Victoria Campbell
status: published
summary: How to Avoid Force Push and Rebase

----

[TOC]

# What about Force Push?

In this class, destructive git operations such as force push (`git push --force`) and rebase (`git rebase`, `git pull --rebase`) are forbidden because they remove git history that is important for marking. 

Force push should never be used in any case, because it will break every one else's git repo that is working on the same project.

## What about Rebase?

Rebase is often used in very large open-source projects with 100s-1000s of developers such as the Linux kernel. It is used in these large projects to reduce the number of commits Linux kernel git repository that has over a million commits! It does this by "flattening" the pull request to a single commit. However, it is not appropriate for the assignments, labs, and projects in this course. In addition, github's pull request UI makes viewing the "flat" diff easy, even if the pull request itself is composed of several commits.

# What to do: "warning: Pulling without specifying how to reconcile divergent branches is discouraged."

Make sure you are on the branch you want to pull to.

Use `git pull --no-rebase` instead of `git pull`. This will start the merge process. Make sure to edit any files with conflicts to make them the way you want them! Then `add` & `commit`.

Use `git config pull.rebase false` to have `git` remember this for the repository. Use `git config --global pull.rebase false` to have `git` remember this for all repositories.

# What to do: "fatal: Not possible to fast-forward, aborting."

Try `git pull --no-rebase` as described in the previous section, or:

Use `git fetch --all` to download all of the remote branches, then `git branch -a` to see all of the branches. Find the name of the branch that is in conflict, it should be something like `remotes/origin/source_branch_name`. 

Make sure you are on the branch you want to merge to, e.g.: `git checkout destination_branch_name`

Then, start the merge process with `git merge remotes/origin/source_branch_name`. Make sure to edit any files with conflicts to make them the way you want them! Then `add` & `commit`.

# What to do: "refusing to merge unrelated histories"

Follow the steps from the previous section but add `--allow-unrelated-histories` argument to `git merge`:

```
git checkout destination_branch_name
git merge remotes/origin/source_branch_name --allow-unrelated-histories
```

Make sure to edit any files with conflicts to make them the way you want them! Then `add` & `commit`.
