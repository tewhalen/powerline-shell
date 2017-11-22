import os
from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        env = os.getenv('VIRTUAL_ENV') \
            or os.getenv('CONDA_ENV_PATH') \
            or os.getenv('CONDA_DEFAULT_ENV')
        if not env:
            return
        env_name = os.path.basename(env)
        bg = self.powerline.theme.VIRTUAL_ENV_BG
        fg = self.powerline.theme.VIRTUAL_ENV_FG
        sepa,sepb = (" "," ")
        if self.powerline.segment_conf("virtual_env","style") == "parens":
            sepa, sepb = ("(",")")
        self.powerline.append(sepa + env_name + sepb, fg, bg)
