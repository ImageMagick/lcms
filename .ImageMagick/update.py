#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Tools"))

from dependency_updater import Step, Updater

URL = "https://github.com/mm2/Little-CMS/releases/download/lcms{version_short}/lcms2-{version_short}.tar.gz"


def update_source(updater):
    updater.replace_source()
    updater.remove(".github")
    updater.update_config()


def apply_patches(updater):
    updater.apply_patches()


updater = Updater(__file__, "lcms", URL)
updater.run([
    Step("Replace the source with the release and update Config.txt", update_source,
        "Update lcms to version {version}"),
    Step("Apply the patches", apply_patches,
        "Changes to lcms."),
    updater.clone_dependencies_step(),
])
