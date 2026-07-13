#!/bin/sh
# Build the arXiv submission tarball: main tex + ancillary files.
set -e
cd "$(dirname "$0")"
tar czf arxiv-submission.tar.gz paper.tex anc/
echo "wrote arxiv-submission.tar.gz:"; tar tzf arxiv-submission.tar.gz
