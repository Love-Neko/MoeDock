import tempfile
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image

from scripts.remove_bg import remove_white_background
from scripts.convert_ico import convert_png_to_ico


class PipelineTest(unittest.TestCase):
    def test_remove_bg_preserves_alpha_and_convert_ico(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source.png'
            transparent = root / 'transparent.png'
            ico = root / 'icon.ico'

            image = Image.new('RGBA', (32, 24), 'white')
            image.putpixel((16, 12), (255, 0, 0, 128))
            image.save(source)

            remove_white_background(str(source), str(transparent))
            result = Image.open(transparent)
            self.assertEqual(result.mode, 'RGBA')
            self.assertGreater(result.getpixel((16, 12))[3], 0)
            self.assertEqual(result.getpixel((0, 0))[3], 0)

            convert_png_to_ico(str(transparent), str(ico))
            self.assertTrue(ico.exists() and ico.stat().st_size > 0)

    def test_transparent_input_and_seeds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'ring.png'
            out = root / 'out.png'

            # 40x40 transparent canvas with a black ring and white center
            image = Image.new('RGBA', (40, 40), (0, 0, 0, 0))
            for y in range(40):
                for x in range(40):
                    d = ((x - 20)**2 + (y - 20)**2)**0.5
                    if d < 8:
                        image.putpixel((x, y), (255, 255, 255, 255))
                    elif 8 <= d <= 16:
                        image.putpixel((x, y), (0, 0, 0, 255))
            image.save(source)

            # with center seed, the white inner hole is hollowed out
            remove_white_background(str(source), str(out), extra_seeds=[(20, 20)])
            result = Image.open(out)
            self.assertEqual(result.mode, 'RGBA')
            self.assertEqual(result.getpixel((0, 0))[3], 0)
            self.assertEqual(result.getpixel((20, 8))[3], 255)
            self.assertLessEqual(result.getpixel((20, 20))[3], 15)

    def test_pipeline_runner(self):
        from scripts.pipeline import process_single_icon
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / 'raw.png'
            Image.new('RGB', (64, 64), 'white').save(raw)

            png_p, ico_p = process_single_icon(
                raw_path=str(raw),
                icon_name='SampleApp',
                png_dir=str(root / 'PNG'),
                ico_dir=str(root / 'ICO')
            )
            self.assertTrue(Path(png_p).exists())
            self.assertTrue(Path(ico_p).exists())

if __name__ == '__main__':
    unittest.main()
