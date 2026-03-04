#!/usr/bin/env python3
"""
GHOSTBYTE Test Suite 👻

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from unicode_generator import UnicodeExploitGenerator
from ascii_obfuscator import ASCIIObfuscator
from string_mixer import StringMixer
from unicode_analyzer import UnicodeAnalyzer


class TestGhostByte(unittest.TestCase):
    """Test GHOSTBYTE functionality"""

    def test_homoglyph(self):
        gen = UnicodeExploitGenerator(seed=42)
        result = gen.homoglyph_replace("password", intensity=1.0)
        self.assertNotEqual(result, "password")

    def test_zero_width(self):
        gen = UnicodeExploitGenerator(seed=42)
        result = gen.insert_zero_width("test", density=1.0)
        self.assertIn('\u200B', result)

    def test_fingerprint(self):
        gen = UnicodeExploitGenerator(seed=42)
        marked = gen.fingerprint_embed("Hello", 1234)
        extracted = gen.extract_fingerprint(marked)
        self.assertEqual(extracted, 1234)

    def test_ascii_box(self):
        obf = ASCIIObfuscator()
        result = obf.create_box("test", 'single')
        self.assertIn('┌', result)
        self.assertIn('└', result)

    def test_glitch(self):
        obf = ASCIIObfuscator()
        result = obf.create_glitch_text("test", 0.5)
        self.assertNotEqual(result, "test")

    def test_mix(self):
        mixer = StringMixer(seed=42)
        result = mixer.mix("test", layers=2)
        self.assertEqual(result['layers'], 2)

    def test_analyze_clean(self):
        analyzer = UnicodeAnalyzer()
        analysis = analyzer.analyze("Hello World")
        self.assertEqual(analysis['risk_score'], 0)

    def test_analyze_suspicious(self):
        analyzer = UnicodeAnalyzer()
        analysis = analyzer.analyze("test\u202E")
        self.assertGreater(analysis['risk_score'], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
