__author__ = 'xyang'
import mwparserfromhell
import pywikibot
enwp = pywikibot.Site('en','wikipedia')
page = pywikibot.Page(enwp, 'Sam Raimi')
wikitext = page.get()
wikicode = mwparserfromhell.parse(wikitext)
templates = wikicode.filter_templates()
infobox_film = templates[1]
# birth_place=infobox_film['birth_place']
print templates
print infobox_film
# print birth_place