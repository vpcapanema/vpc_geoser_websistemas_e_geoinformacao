"""Approved Exo 2 typography; vector outlines need no installed font."""
from functools import lru_cache
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = Path(__file__).resolve().parents[1] / 'assets/identidade-visual/tipografia/exo-2/Exo2[wght].ttf'
NS = 'http://www.w3.org/2000/svg'

def font(size, weight=600):
    result = ImageFont.truetype(str(FONT), size)
    result.set_variation_by_axes([weight])
    return result

@lru_cache(maxsize=2)
def outline_font(weight):
    return instantiateVariableFont(TTFont(FONT), {'wght': weight}, inplace=False)

def svg_text(text, x, baseline, size, color, weight=600, spacing=1):
    face = outline_font(weight)
    glyphs = face.getGlyphSet()
    cmap = face.getBestCmap()
    scale = size / face['head'].unitsPerEm
    measure = font(size * 4, weight)
    group = ET.Element(f'{{{NS}}}g', {'aria-label': text, 'data-font-family': 'Exo 2', 'data-font-weight': str(weight), 'fill': color})
    for i, char in enumerate(text):
        glyph_name = cmap[ord(char)]
        pos = x + measure.getlength(text[:i]) / 4 + i * spacing
        pen = SVGPathPen(glyphs)
        glyphs[glyph_name].draw(TransformPen(pen, (scale, 0, 0, -scale, pos, baseline)))
        path = pen.getCommands()
        if path:
            ET.SubElement(group, f'{{{NS}}}path', {'d': path})
    return group
