#!/usr/bin/env python3

import sys
from git import Repo
import os
import glob
import time
import subprocess

import logging
logger = logging.getLogger(__name__)
DEBUG = logger.debug
INFO = logger.info
WARNING = logger.warning
ERROR = logger.error
CRITICAL = logger.critical

HEADER="HEADER --------------------------"
FOOTER="FOOTER --------------------------"

def get_file_list(pattern):
    return [glob.glob(pattern)]

def clean(file_list):
    repo = Repo(os.getcwd())
    assert not repo.bare
    uncommitted=False
    for f in file_list:
        if not f in repo.head.commit.tree:
            CRITICAL(f + " is untracked by git. Refusing to proceed!")
            sys.exit(1)
    if repo.is_dirty():
        CRITICAL("Git repo is dirty. Refusing to proceed. Commit and retry.")
        sys.exit(2)
    return repo

def get_date_last_modified_git(fname):
    # Taken from https://stackoverflow.com/questions/13104495/get-time-of-last-commit-for-git-repository-files-via-python, 2019-01-14
    """
    Start a git process to get file info. Return a string containing the
    filename, the abbreviated commit hash and the author date in ISO 8601
    format.

    Arguments:
        fname: Name of the file to check.

    Returns:
        A 3-tuple containing the file name, latest short hash and latest
        commit date.
    """
    args = ['git', '--no-pager', 'log', '-1', '--format=%h|%at', fname]
    try:
        b = subprocess.check_output(args)
        data = b.decode()[:-1]
        h, t = data.split('|')
        t = time.gmtime(float(t))
    except (subprocess.CalledProcessError, ValueError):
        CRITICAL("No date?")
        sys.exit(3)
    return t

def find_latest(file_list, repo):
    latest_time = time.gmtime(0)
    latest_file = None
    for f in file_list:
        assert f in repo.head.commit.tree
        t = get_date_last_modified_git(f)
        WARNING(f + ": " + str(t))
        if t > latest_time:
            latest_file = f
            latest_time = t
        elif t == latest_time:
            if os.path.getmtime(f) > os.path.getmtime(latest_file):
                latest_file = f
                latest_time = t
    assert latest_file is not None
    return latest_file

def extract_header_footer(from_):
    with open(from_, 'r') as fromfile:
        fromhtml = fromfile.read()
    (h, hb_sep, bf) = fromhtml.partition(HEADER)
    assert hb_sep == HEADER
    (b, bf_sep, f) = bf.rpartition(FOOTER)
    assert bf_sep == FOOTER
    return (h, hb_sep, b, bf_sep, f)

def modify_header_footer(from_, to):
    assert HEADER not in from_[0]
    assert HEADER not in to[0]
    assert from_[1] == HEADER
    assert to[1] == HEADER
    assert HEADER not in from_[2]
    assert HEADER not in to[2]
    assert from_[3] == FOOTER
    assert to[3] == FOOTER
    assert FOOTER not in to[4]
    assert FOOTER not in from_[4]
    assert len(from_) == 5
    assert len(to) == 5
    return (
        from_[0],
        to[1],
        to[2],
        to[3],
        from_[4])

def write_hbf(hbf, filename):
    with open(filename, 'w') as outfile:
        outfile.write(
            "".join(hbf)
            )

def copy_header_footer(from_, to):
    from_hbf = extract_header_footer(from_)
    for f in to:
        WARNING("Copying header/footer from " + from_ + " to " + f)
        to_hbf = extract_header_footer(f)
        new_hbf = modify_header_footer(from_hbf, to_hbf)
        write_hbf(new_hbf, f)

def main():
    #file_list = get_file_list("*.html")
    file_list = sys.argv[1:]
    repo = clean(file_list)
    latest = find_latest(file_list, repo)
    del file_list[file_list.index(latest)]
    copy_header_footer(latest, file_list)

if __name__=="__main__":
    main()
