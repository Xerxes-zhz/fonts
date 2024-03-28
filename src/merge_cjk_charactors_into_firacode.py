from os.path import dirname, join

import fontforge

DataDir = join(dirname(dirname(__file__)), "data")
MainFont = join(DataDir, "FiraCodeNerdFont-Retina.ttf")
MergedFont = join(DataDir, "LXGWWenKaiMono-Regular.ttf")
FontName = "FiraCodeNerdFont-Ret-WithLXGWCN-Xerxes"
Output = join(DataDir, f"{FontName}.ttf")
print("Main:", MainFont)
print("Merged:", MergedFont)

CJKRanges = [
    (0x4E00, 0x9FFF),  # CJK Unified Ideographs
    (0x3400, 0x4DBF),  # CJK Unified Ideographs Extension A
    (0x20000, 0x2A6DF),  # CJK Unified Ideographs Extension B
    (0x2A700, 0x2B73F),  # CJK Unified Ideographs Extension C
    (0x2B740, 0x2B81F),  # CJK Unified Ideographs Extension D
    (0x2B820, 0x2CEAF),  # CJK Unified Ideographs Extension E
    (0x2CEB0, 0x2EBEF),  # CJK Unified Ideographs Extension F
    (0x30000, 0x3134F),  # CJK Unified Ideographs Extension G
    (0x31350, 0x323AF),  # CJK Unified Ideographs Extension H
]

if __name__ == "__main__":
    main_font = fontforge.open(MainFont)
    merged_font = fontforge.open(MergedFont)
    output_font = fontforge.font()

    merged_font.upos = -125
    merged_font.em = 1950
    merged_font.ascent = 1560
    merged_font.descent = 390
    main_font.selection.none()
    merged_font.selection.none()

    for start, end in CJKRanges:
        main_font.selection.select(("ranges", "more"), start, end)
        merged_font.selection.select(("ranges", "more"), start, end)
        # output_font.selection.select(("ranges", "more"), start, end)
    merged_font.copy()
    main_font.paste()
    main_font.fontname = FontName
    main_font.validate()
    main_font.save(Output)
    # merged_font.copy()
    # output_font.paste()

    # main_font.selection.invert()
    # output_font.selection.invert()

    # main_font.copy()
    # output_font.paste()

    # output_font.fontname = FontName
    # output_font.save(Output)

    # main_font.close()
