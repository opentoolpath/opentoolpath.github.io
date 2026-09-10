#!/usr/bin/env python3
"""Check the small public portal's links and publication boundaries without dependencies."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlparse, unquote

PRIVATE = {'spec', 'otp-rs', 'otp-py', 'conformance', 'viewer', 'fusion360-otp', 'irbcam-plugin', 'otp-marketing'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag != 'iframe', 'The public discussion portal must not embed experimental apps'
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'img':
            assert 'alt' in attrs, 'Images require alternative text (empty for decorative images)'
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


def check(root):
    parser = Page()
    parser.feed((root / 'index.html').read_text())
    assert parser.h1 == 1, 'Expected one primary heading'
    for source in [root / 'index.html', root / 'README.md', *sorted((root / 'development').glob('*.md'))]:
        links = parser.links if source.suffix == '.html' else re.findall(r'\]\(([^)]+)\)', source.read_text())
        for link in links:
            url = urlparse(link)
            parts = url.path.strip('/').split('/')
            if url.netloc == 'github.com' and len(parts) >= 2 and parts[0] == 'opentoolpath':
                assert parts[1] not in PRIVATE, f'{source.name}: link to private repo {link}'
                if parts[1:] and len(parts) >= 5 and parts[2:4] == ['blob', 'main'] and parts[1] == 'opentoolpath.github.io':
                    assert (root / '/'.join(parts[4:])).is_file(), f'Missing public document: {link}'
            if url.netloc or url.scheme:
                continue
            if url.path:
                path = (source.parent / unquote(url.path)).resolve()
                assert path.is_relative_to(root.resolve()), f'Link escapes publication: {link}'
                assert path.is_file(), f'Missing local link: {source.name}: {link}'
                assert path.suffix != '.otp', 'Experimental package download in public portal'
            elif url.fragment and source.suffix == '.html':
                assert url.fragment in parser.ids, f'Missing section: {link}'
    assert not list(root.rglob('*.otp')), 'Experimental sample packages remain in public repository'
    for template in ('use-case.yml', 'review.yml'):
        assert (root / '.github' / 'ISSUE_TEMPLATE' / template).is_file(), f'Missing contribution form: {template}'
    print('PASS: local links, public document targets, contribution forms and publication boundaries')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    check(ap.parse_args().root)
