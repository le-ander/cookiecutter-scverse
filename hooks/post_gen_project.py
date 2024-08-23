#!/bin/env python3
from subprocess import run
{% if not cookiecutter._render_devdocs %}
from pathlib import Path

# Post processing
Path("docs/template_usage.md").unlink()
{% endif %}

# Update pre commit hooks
run("pre-commit autoupdate -c .pre-commit-config.yaml".split(), check=True)
run("pre-commit install".split(), check=True)

# The following output was generated using rich
# The formatted output is included here directly, because I don't want
# rich as another dependency for initalizing the repo.
# Regenerate using `cd scripts; hatch run python -m scverse_template_scripts.make_rich_output`
print("""




┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        \x1b[1mSet-up online services\x1b[0m                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

\x1b[1mYour repository is now ready.\x1b[0m\x1b[1m \x1b[0m\x1b[1mHowever, to use all features of the \x1b[0m
\x1b[1mtemplate you will need to set up the following online services.\x1b[0m Clicking
on the links will take you to the respective sections of the developer
documentation. The developer documentation is also shipped as part of
the template in docs/developer_docs.md.

\x1b[1;33m 1 \x1b[0m\x1b]8;id=994867;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html#pre-commit-checks\x1b\\\x1b[4;34mpre-commit.ci\x1b[0m\x1b]8;;\x1b\\ to check for inconsistencies and to enforce a code
\x1b[1;33m   \x1b[0mstyle
\x1b[1;33m 2 \x1b[0m\x1b]8;id=697682;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html#documentation-on-readthedocs\x1b\\\x1b[4;34mreadthedocs.org\x1b[0m\x1b]8;;\x1b\\ to build and host documentation
\x1b[1;33m 3 \x1b[0m\x1b]8;id=723197;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html#coverage-tests-with-codecov\x1b\\\x1b[4;34mcodecov\x1b[0m\x1b]8;;\x1b\\ to generate test coverage reports

All CI checks should pass, you are ready to start developing your new
tool!

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                         \x1b[1mInstall the package\x1b[0m                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

To run tests or build the documentation locally, you need to install
your package and its dependencies. You can do so with

\x1b[40m                                                                        \x1b[0m
\x1b[40m \x1b[0m\x1b[97;40mpip\x1b[0m\x1b[97;40m \x1b[0m\x1b[97;40minstall\x1b[0m\x1b[97;40m \x1b[0m\x1b[93;40m".[test,dev,doc]"\x1b[0m\x1b[40m                                         \x1b[0m\x1b[40m \x1b[0m
\x1b[40m                                                                        \x1b[0m

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                            \x1b[1mCustomizations\x1b[0m                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Further instructions on using this template can be found in the \x1b]8;id=736137;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html\x1b\\\x1b[4;34mdev docs\x1b[0m\x1b]8;;\x1b\\
\x1b]8;id=736137;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html\x1b\\\x1b[4;34mincluded in the project\x1b[0m\x1b]8;;\x1b\\.

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                              \x1b[1mCommitment\x1b[0m                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

We expect developers of scverse ecosystem packages to

\x1b[1;33m • \x1b[0m\x1b]8;id=213267;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html#writing-tests\x1b\\\x1b[4;34mwrite unit tests\x1b[0m\x1b]8;;\x1b\\
\x1b[1;33m • \x1b[0m\x1b]8;id=972096;https://cookiecutter-scverse-instance.readthedocs.io/en/latest/developer_docs.html#writing-documentation\x1b\\\x1b[4;34mprovide documentation\x1b[0m\x1b]8;;\x1b\\, including tutorials where applicable
\x1b[1;33m • \x1b[0msupport users through github and the \x1b]8;id=997067;https://discourse.scverse.org/\x1b\\\x1b[4;34mscverse discourse\x1b[0m\x1b]8;;\x1b\\

""")
