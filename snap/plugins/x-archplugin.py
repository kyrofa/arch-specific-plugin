import os
import logging
import shutil
import re
import subprocess

import snapcraft

logger = logging.getLogger(__name__)


class ArchPlugin(snapcraft.BasePlugin):

    def pull(self):
        super().pull()

        puller = snapcraft.sources.Tar(
            'https://arch-specific/{}'.format(self.project.deb_arch),
            self.sourcedir)
        puller.pull()
