"""MkDocs hooks for the English copy of the site (mkdocs-static-i18n, suffix layout).

1. Raw HTML in pages (<video>, <img>, <a> in kb-figure rows) carries paths
   relative to the page URL, and MkDocs does not rewrite them. English pages are
   served one folder deeper (/en/...), while the assets stay shared at the site
   root, so a path like ../../assets/x.png breaks there. After rendering, every
   relative src/href/poster on an /en/ page that points to a missing file but
   works with one more "../" gets that "../". Markdown links are already right
   and are left alone, so page sources keep the same paths in both languages.
2. The toc permalink title is a Markdown extension option, which the i18n plugin
   cannot override per language: it is set here from the build language.
"""
import posixpath
import re
from urllib.parse import unquote, urlsplit

from mkdocs.plugins import event_priority

EN = "en"
PERMALINK_TITLE = {"ru": "Прямая ссылка на раздел", "en": "Link to this section"}

TAG = re.compile(r"<(?:img|video|source|audio|track|iframe|a)\b[^>]*>", re.I)
ATTR = re.compile(r'(\s(?:src|href|poster)=")([^"]*)(")', re.I)
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.I)


@event_priority(-110)  # after the i18n plugin has set theme.language
def on_config(config):
    lang = config.theme.get("language") or "ru"
    toc = config.mdx_configs.setdefault("toc", {})
    toc["permalink_title"] = PERMALINK_TITLE.get(lang, PERMALINK_TITLE["ru"])
    return config


def _target(page_url, url):
    path = unquote(urlsplit(url).path)
    if not path:
        return None
    base = page_url if page_url.endswith("/") else posixpath.dirname(page_url) + "/"
    joined = posixpath.normpath(posixpath.join(base, path))
    if path.endswith("/") or joined in (".", ""):
        joined = posixpath.join(joined, "index.html") if joined not in (".", "") else "index.html"
    return joined


def on_page_content(html, page, config, files):
    if not page.url.startswith(EN + "/"):
        return html
    known = {f.dest_uri for f in files}

    def fix_attr(m):
        url = m.group(2)
        if not url or url.startswith(("/", "#")) or SCHEME.match(url):
            return m.group(0)
        here = _target(page.url, url)
        if here is None or here in known:
            return m.group(0)
        deeper = _target(page.url, "../" + url)
        if deeper in known:
            return m.group(1) + "../" + url + m.group(3)
        return m.group(0)

    return TAG.sub(lambda t: ATTR.sub(fix_attr, t.group(0)), html)
