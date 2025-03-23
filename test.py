import json
import pathlib as p

import dcx_pd as dcx
from tcrutils.console import c

PATHS = [
	p.Path(__file__).parent / "gitignored/smallest.json",
	p.Path(__file__).parent / "gitignored/small.json",
	p.Path(__file__).parent / "gitignored/furaski.json",
	(p.Path(__file__).parent / "gitignored/hikari").glob("*.json").__next__(),
	p.Path(__file__).parent / "gitignored/forum/private.json",
	p.Path(__file__).parent / "gitignored/forum/public.json",
	p.Path(__file__).parent / "gitignored/forum/pub-thread.json",
]

for path in PATHS:
	export = dcx.Export.from_path(path)

	c(export, depth_limit=2)
