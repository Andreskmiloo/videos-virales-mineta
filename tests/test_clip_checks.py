from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase, mock

import main


class ClipChecks(TestCase):
    script = {"id": "part", "clips_from": "long", "items": [{"rank": 4, "clip": "goal.mov"}]}

    def test_check_uses_requested_script_and_shared_clip_name(self):
        output = StringIO()
        with mock.patch("main.load_script", return_value=self.script) as load, redirect_stdout(output):
            main.cmd_check(SimpleNamespace(scripts=["one.json"]), {})
        load.assert_called_once_with(Path("one.json"))
        self.assertIn("clips/long/", output.getvalue())
        self.assertIn("goal.mov", output.getvalue())

    def test_render_requires_preview_for_missing_clip(self):
        args = SimpleNamespace(all=False, scripts=["one.json"], preview=False, silent=False)
        with mock.patch("main.load_script", return_value=self.script), mock.patch("src.render.render") as render:
            with self.assertRaisesRegex(SystemExit, "--preview"):
                main.cmd_render(args, {})
            render.assert_not_called()
            args.preview = True
            main.cmd_render(args, {})
            render.assert_called_once_with(self.script, {})
